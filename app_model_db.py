from flask import Flask, request, jsonify
import os
import pickle
from sklearn.model_selection import cross_val_score
import pandas as pd
import sqlite3


app = Flask(__name__)

csv_path = os.path.join(os.getcwd(), 'data', 'Advertising.csv')
db_path = os.path.join(os.getcwd(), 'data', 'Advertising.db')
model_path = os.path.join(os.getcwd(), 'data', 'advertising_model')

os.chdir(os.path.dirname(__file__))

app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a mi API del modelo advertising"


@app.route('/v2/predict', methods=['GET'])
def model_predict():
    model = pickle.load(open(model_path, 'rb'))
    tv = request.args.get('TV', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newpaper', None)
    if tv is None or radio is None or newspaper is None:
        return 'Faltan argumuentos de entrada'
    else:
        prediction = model.predict([[int(tv), int(radio), int(newspaper)]])
        return "La predicción de ventas invirtiendo esa cantidad de dinero en TV, radio y periódicos es: " + str(round(prediction[0], 2)) + 'k €'


@app.route('/v2/ingest_data', methods=['POST'])
def ingest_data():
    # Conectar a la base de datos
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS advertising (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tv REAL,
            radio REAL,
            newspaper REAL,
            sales REAL
        )
    ''')

    # Obtener los datos del cuerpo de la solicitud
    data = request.get_json()

    # Validar los datos
    try:
        tv = float(data['TV'])
        radio = float(data['radio'])
        newspaper = float(data['newpaper'])
        sales = float(data['sales'])
    except ValueError:
        return 'Valores incorrectos. Todos los valores deben ser números.'

    # Insertar los datos en la base de datos
    cursor.execute('INSERT INTO advertising (tv, radio, newpaper, sales) VALUES (?, ?, ?, ?)',
                   (tv, radio, newspaper, sales))

    # Guardar los cambios y cerrar la conexión
    connection.commit()
    connection.close()

    return 'Datos almacenados correctamente'


@app.route('/v2/retrain', methods=['GET'])
def retrain():
    # Cargar el modelo previamente entrenado
    model = pickle.load(
        open(os.path.join(os.getcwd(), 'data', 'advertising_model'), 'rb'))
    # Conectar a la base de datos existente
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Obtener los datos de la base de datos
    cursor.execute('SELECT TV, radio, newpaper, sales FROM advertising')
    data = cursor.fetchall()

    # Convertir los datos a un DataFrame de pandas
    df = pd.DataFrame(data, columns=['TV', 'radio', 'newpaper', 'sales'])

    # Separar las variables independientes y dependientes
    X = df[['TV', 'radio', 'newpaper']]
    y = df['sales']

    X.columns = model.feature_names_in_

    # Reentrenar el modelo con los nuevos datos
    model.fit(X, y)

    # Guardar el modelo reentrenado
    pickle.dump(model, open(os.path.join(
        os.getcwd(), 'data', 'advertising_model'), 'wb'))

    # Cerrar la conexión a la base de datos
    connection.close()

    return 'Modelo reentrenado correctamente'


app.run()

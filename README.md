# Tutorial de uso de la API

Este tutorial te guiará a través de los pasos para usar la API, desde hacer predicciones con valores de entrada nuevos hasta reentrenar el modelo.

## 1. Activar el entorno en la terminal

Para activar el entorno y ejecutar la aplicación Flask, navega hasta el directorio del repositorio en la terminal y ejecuta el siguiente comando:

## 2. Abrir 'localhost' en el navegador

Una vez que la aplicación Flask esté en ejecución, puedes abrir la página de inicio de la API en tu navegador. Para hacerlo, haz clic en el siguiente enlace o cópialo y pégalo en la barra de direcciones de tu navegador:

## 3. Hacer predicciones con valores nuevos de entrada

Para hacer una predicción con valores nuevos de entrada, ingresa la URL de la ruta `/v2/predict` en tu navegador junto con los valores de "TV", "radio" y "newpaper" como argumentos. Por ejemplo:

_Nota: No olvides incluir todos los argumentos y asegúrate de escribir "newpaper" correctamente._

La respuesta de la API será una predicción de ventas basada en los valores de entrada proporcionados.

## 4. Ingestar valores para predecir

Para enviar datos a la API y almacenarlos en la base de datos, puedes usar una herramienta como Postman para enviar una solicitud POST a la ruta `/v2/ingest_data`. Sigue estos pasos para hacerlo:

1. Abre Postman y crea una nueva pestaña de solicitud.
2. Selecciona el método "POST" en el menú desplegable junto a la barra de direcciones.
3. Ingresa la URL de la ruta `/v2/ingest_data` en la barra de direcciones. Por ejemplo, si estás ejecutando la aplicación Flask localmente en el puerto 5000, la URL sería `http://localhost:5000/v2/ingest_data`.
4. Selecciona la pestaña "Body" debajo de la barra de direcciones.
5. Selecciona la opción "raw" y luego selecciona "JSON" en el menú desplegable a la derecha.
6. Ingresa los datos que deseas enviar en el cuerpo de la solicitud en formato JSON. Por ejemplo:

    ```json
    {
        "TV": 100,
        "radio": 200,
        "newpaper": 50,
        "sales": 25
    }
    ```

7. Haz clic en el botón "Send" para enviar la solicitud.

Si todo está configurado correctamente, deberías recibir una respuesta del servidor indicando que los datos fueron almacenados correctamente.

## 5. Reentrenar el modelo

Para reentrenar el modelo con los nuevos datos almacenados en la base de datos, ingresa la URL de la ruta `/v2/retrain` en tu navegador:

## Advertising Model API 🚀

Flask API 🌐 The Flask API has several routes that allow you to make predictions, ingest data, and retrain the model.

This repository contains two main folders: [data](./data) and [ejercicio](./ejercicio). The `data` folder contains the necessary data for the Advertising Model API, while the `ejercicio` folder contains the code for the API and the script to convert a CSV file into an SQLite database.

Advertising Model API 🚀
This repository contains a Flask API for an advertising model and a script to convert a CSV file into an SQLite database.

Flask API 🌐
The Flask API has several routes that allow you to make predictions, ingest data, and retrain the model.

Routes 🛣️
🌈 The / route accepts GET requests and returns a warm welcome message. 🤗

🔮 The /v2/predict route accepts GET requests with values for tv, radio, and newspaper as arguments in the call. When a request is received, the code loads a previously trained model from the data/advertising_model file, gets the values of the arguments, and uses the model to make a prediction. Then, it returns the prediction to the client. 🔮

📬 The /v2/ingest_data route accepts POST requests with data in JSON format in the request body. When a request is received, the code connects to an SQLite database called advertising.db in the data directory, creates a table called advertising if it doesn’t exist, and stores the received data in this table. 📬

🔧 The /v2/retrain route accepts PUT requests. When a request is received, the code loads the previously trained model from the data/advertising_model file, connects to the SQLite database, retrieves the data stored in the advertising table, converts it into a pandas DataFrame, and separates the independent and dependent variables. Then, it retrains the model using this data and saves the retrained model in the same file. 🔧

SQL Database Creator Script 🗄️
The sql_db_creator.py script reads data from a CSV file called Advertising.csv in the data directory, connects to an SQLite database called advertising.db in the same directory, and stores the data from the CSV file in this database.

The script uses pandas to read the CSV file and convert it into a DataFrame. Then, it renames the column newspaper to newpaper, as specified in your requirements. Finally, it uses the to_sql method of pandas to create a table called advertising in the SQLite database and store the data from the DataFrame in this table.

Usage 💻
To use this repository, first make sure you have Python 3 installed on your machine. Then, clone this repository and navigate to its root directory.

To run the Flask API, use the following command:

python app_model_db.py

This will start a local development server at http://127.0.0.1:5000. You can then use your web browser or an HTTP client like cURL or Postman to interact with the API.

To run the SQL database creator script, use the following command:

python csv_to_sqlite.py

This will read data from the CSV file and store it in an SQLite database called advertising.db in the data directory.

# We hope you find this repository useful! 😊

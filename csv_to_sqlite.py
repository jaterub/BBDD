import csv
import sqlite3
import os

db_path = os.path.join(os.getcwd(), 'data', 'Advertising.db')
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS Advertising (TV, radio, newpaper, sales);")

csv_path = os.path.join(os.getcwd(), 'data', 'Advertising.csv')
with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        values = [float(x) for x in row[1:]]
        cur.execute("INSERT INTO Advertising VALUES (?,?,?,?)", values)

con.commit()
con.close()

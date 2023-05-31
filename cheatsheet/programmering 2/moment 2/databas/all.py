# Importerar mysql.connector
import mysql.connector

# Ansluter till databasen
mydb = mysql.connector.connect (
    host="localhost",
    user = "root",
    password = "",
    database = "db_caisaskog"
)

# Ger databasen ett variabelnamn
mycursor = mydb.cursor()

# Hämtar uppgifter ifrån tabellen
mycursor.execute('SELECT * FROM intro_db')
result = mycursor.fetchall()

# Hämtar kolumner för en rad
def print_row(row):
    identification = row[0]
    name = row[1]
    address = row[2]
    age = row[3]
    other = row[4]
    date = row[5]

    # Skriver ut tabellen
    print('{:<5} {:<10} {:<15} {:<8} {:<15} {}'.format(identification, name, address, age, other, date))

# Skriver ut tabellhuvudet
print('{:<5} {:<10} {:<15} {:<8} {:<15} {:20}'.format('ID', 'Name', 'Address', 'Age', 'Other', 'Date Added'))

# Hämtar information per rad
tableLenght = len(result)
for row in range(tableLenght):
    print_row(result[row])
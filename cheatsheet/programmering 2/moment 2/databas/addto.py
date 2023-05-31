# Importerar mysql.connector
import mysql.connector

# Importerar tidsmodul
import datetime

# Ansluter till databasen
mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",  
    database = "db_caisaskog"
)

# Ger databasen ett variabel namn
mycursor = mydb.cursor()

# Dictionary på fråga beroende på vad för information som man vill fråga efter
question = {
    'name': 'Ange ditt namn: ',
    'address': 'Ange din adress: ',
    'age': 'Ange din ålder: ',
    'other': 'Ange övrigt: '
}

# Hämtar data från användaren
def get_input(info):
    while True: 
        response = str(input(question[info]))
        result = not_empty(response)
        if result:
            return response
        else: 
            print('Var vänlig lämna inte fältet tomt')
            continue

# Kollar om svaret är tomt, om det inte är det kan koden fortsätta
def not_empty(i):
    if i == '':
        return False
    elif (i.isspace()):
        return False
    else: 
        return i

# Anger vilken tabell man vill lägga in i och vad för uppgifter som ska läggas in
sql = "INSERT INTO intro_db(id, name, address, age, other, date) VALUES (%s, %s, %s, %s, %s, %s)"

# Lista som informationen man vill lägga in lagras i
val = []

for x in range(10):
    # Hämtar data från användaren (10 stycken olika i detta fall)
    name = get_input('name')
    address = get_input('address')
    age = get_input('age')
    other = get_input('other')
    time = datetime.datetime.now()

    val.append(("NULL", name, address, age, other, time))

# Lägger in alla uppgifter
mycursor.executemany(sql, val)

# Laddar upp dem
mydb.commit()

# Konfirmerar om datan lagrades eller ej
if mycursor:
    print(mycursor.rowcount, "data har lagrats")
else: 
    print('Något gick fel när datan skulle lagrats')
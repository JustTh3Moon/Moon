# Importerar mysql.connector
import mysql.connector

# Importerar datetime modulen
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

# Variabel som håller i alternativen för startmenyn
alt = """
1. Lägg in ny klasskamrat
2. Visa medelåldern
3. Visa längsta eller kortaste
4. Visa vem som fyller först eller sist
5. Visa vem som har högsta eller lägsta favoritnummer
6. Avsluta
"""

# Startmeny som erbjuder alternativ som användaren kan göra
def start():
    response = input('Välkommen! \n\nVad vill du göra, välj mellan alternativen nedan.' + alt)
    return response

# Dictionary på fråga beroende på vad för information som man vill fråga efter
question = {
    'name': 'Ange ditt namn: ',
    'age': 'Ange din ålder: ',
    'length': 'Ange din längd (cm): ',
    'birthday': 'Ange din födelsedag (YYYY/MM/DD): ',
    'fav_num': 'Ange ditt favorit nummer: ',
}

# Funktion som låter användaren mata in ny information/ny kolumn till tabellen
def new_user():

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
    sql = "INSERT INTO min_klass (name, age, length, birthday, fav_num) VALUES (%s, %s, %s, %s, %s)"

    # Hämtar data från användaren
    name = get_input('name')
    age = get_input('age')
    length = get_input('length')
    birthday = get_input('birthday')
    fav_num = get_input('fav_num')

    # Definerar values
    val = (name, age, length, birthday, fav_num)
    
    # Lägger in alla uppgifter
    mycursor.execute(sql, val)

    # Laddar upp dem
    mydb.commit()

    return print(mycursor.rowcount, "data har lagrats")

# Funktion som beräknar medelåldern
def calc_avg_age():
    # Tar fram alla åldrar
    mycursor.execute("SELECT age FROM min_klass")
    result = mycursor.fetchall()

    # Kollar längden på listan av åldrar
    list_len = len(result)

    # Variabel som ska spara summan av åldrarna
    amount = 0

    # Tar fram summan av åldrarna
    for i in range(list_len):
        amount += result[i][0]

    # Räknar ut medelåldern
    avg = amount/list_len

    # Skriver ut medelåldern med formaterat med 2 decimaler
    print(f'Medelåldern är: {avg:.2f}')

# Funktion som returnerar antingen den längsta eller kortaste
def order_length():
    response = input('Välj om du vill visa:\n1. Längsta\n2. Kortaste\n')
    # Om användaren anger längsta
    if response == '1':
        mycursor.execute("SELECT length, name FROM min_klass ORDER BY length DESC LIMIT 1")
        ordern = 'längsta'

    # Om användaren anger kortaste
    if response == '2':
        mycursor.execute("SELECT length, name FROM min_klass ORDER BY length LIMIT 1")
        ordern = 'kortaste'

    # Tar fram vilken det är
    result = mycursor.fetchall()

    # Skriver ut resultatet med formatering med 1 decimal
    print(f'Den {ordern} är {result[0][1]} på {result[0][0]:.1f} cm')

# Funktion som returnerar antingen den som fyller först eller sist
def order_birthday():
    response = input('Välj om du vill visa:\n1. Fyller först\n2. Fyller sist\n')
    # Om användaren anger den som fyller först
    if response == '1':
        mycursor.execute("SELECT birthday, name FROM min_klass ORDER BY birthday DESC LIMIT 1")
        ordern = 'den som fyller först'

    # Om användaren anger den som fyller sist
    if response == '2':
        mycursor.execute("SELECT birthday, name FROM min_klass ORDER BY birthday LIMIT 1")
        ordern = 'som fyller sist'

    # Tar fram vilken det är
    result = mycursor.fetchall()

    # Skriver ut resultatet
    print(f'Den {ordern} är {result[0][1]} och föddes {result[0][0]}')

# Funktion som returnerar antingen det högsta eller lägsta favorit numret
def order_fav_num():
    response = input('Välj om du vill visa:\n1. Högsta\n2. Lägsta\n')
    # Om användaren anger högsta
    if response == '1':
        mycursor.execute("SELECT fav_num, name FROM min_klass ORDER BY fav_num DESC LIMIT 1")
        ordern = 'högsta'

    # Om användaren anger lägsta
    if response == '2':
        mycursor.execute("SELECT fav_num, name FROM min_klass ORDER BY fav_num LIMIT 1")
        ordern = 'lägsta'

    # Tar fram vilken det är
    result = mycursor.fetchall()

    # Skriver ut resultatet med formatering med 1 decimal
    print(f'Den {ordern} är {result[0][1]} som har {result[0][0]} som favoritnummer')

# Dictionary som kopplar respektiva alternativ till funktion
options = {
    '1': new_user,
    '2': calc_avg_age,
    '3': order_length,
    '4': order_birthday,
    '5': order_fav_num,
}

# Loop som låter användaren välja mellan alternativ tills den avslutar programmet
while True:
    choice = start()
    if choice == '6':
        print('Programmet avslutas...')
        break
    
    options[choice]()
    # Printar två tomma linjer
    print('\n')

# Detta är slutet av koden
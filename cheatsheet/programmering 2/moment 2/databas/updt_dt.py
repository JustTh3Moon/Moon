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

# Ber användaren ange vilken användare i tabellen den vill ändra på (genom att ange namnet)
def what_user():
    user = str(input('Ange namnet på användaren du vill ändra: '))
    # Hämtar kolumnen för den användaren
    old_info = mycursor.execute(f'SELECT * FROM intro_db WHERE name = "{user}"')
    old_info = mycursor.fetchall()
    # Returnerar lista av användaren som vill ändras på
    return old_info[0], user

keys = {
    'name': 1,
    'address': 2,
    'age': 3,
    'other': 4,
    'date': 5,
}

# Ber användaren ange vad för kollumn den vill ändra med hjälp av en dictionary
def get_new_info(old_info_list):
    info = input('Ange vilken information du vill ändra: (Name, Address, etc): ')

    # Låter användaren ange vad som ska ersätta den gamla informationen
    new_info = input('Ange vad du vill ersätta med: ')

    # Tar fram den gamla informationen
    index = keys[info.lower()]
    old_info = old_info_list[index]

    # Returnerar den nya information som ska läggas in (samt vad den gamla är)
    return new_info, str(old_info), info.lower()

# Hämtar vilken användare som ska ändras
old_info_list, name = what_user()

user_info = f"""
Name: {old_info_list[1]}
Address: {old_info_list[2]}
Age: {old_info_list[3]}
Other: {old_info_list[4]}
Date: {old_info_list[5]}
"""

# Skriver ut användarens information
print(f'- Här är din information{user_info}')

# Frågar och hämtar den nya informationen som ska ersätta den gamla uppgiften
new_info, old_info, info = get_new_info(old_info_list)

identify = old_info_list[0]

# Anger vilken tabell man vill ändra och vad för uppgift som man vill ändra
sql = f"UPDATE intro_db SET {info} = %s WHERE id = %s"

# Ändra uppgiften
val = (new_info, identify)

# Lägger in de nya uppgiften
mycursor.execute(sql, val)

# Laddar upp dem
mydb.commit()

# Konfirmerar att uppgiften uppdaterades
print(mycursor.rowcount, "record(s) affected")
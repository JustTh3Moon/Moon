# 1. Importera mysql.connector
import mysql.connector
# Importeraa tids modul
import datetime

# 2. Ansluta till databasen
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "te20"
)

# Ger anslutningen ett variabelnamn
mycursor = mydb.cursor()

# 3. Skapa 1 eller flera variabler för att lägga in
username = 'oliva'
email = 'olivia@salo.com'
time = datetime.datetime.now()

# 4. Lägga in uppgifter i tabellen
sql = "INSERT INTO lektion1(id, name, email, dated) VALUES(%s, %s, %s, %s)"
val = ("NULL", username, email, time)
# NULL = ett värde men ändå inte

mycursor.execute(sql, val)
mydb.commit()

# 5. Se ifall data lagts till i tabellen eller inte
if mycursor:
    print(mycursor.rowcount, "Data har lagts in")
else: print("Data kunde inte läggas in")

# Hämta data från tabellen lektion1
mycursor.execute("SELECT * FROM lektion1")
# Hämtar alla uppgifter från tabellen
result = mycursor.fetchall() 
for row in result:
    # print(f'ID: {row[0]}\nUsername: {row[1]}\nEmail: {row[2]}\nDate: {row[3]}')
    print(row)

# Hämta data från tabellen lektion1 men sorterad efter id (i detta fall) ()
mycursor.execute("SELECT * FROM lektion1 ORDER BY id DESC")
# Hämtar endast en uppgift från tabellen
result = mycursor.fetchone()
for i in result:
    print(i)

# Hämta data från tabellen lektion1 men med en limit, så hämta exempelvis bara 2 (av 3)
mycursor.execute("SELECT * FROM lektion1 LIMIT 2")
# Hämta alla uppgifter från tabellen
result = mycursor.fetchall()
for i in result:
    print(i)

# Frågar användaren att ange vad och vart den vill uppdatera
new_name = str(input('Ange nytt namn: '))
id = str(input('Ange ID på den du vill uppdatera: '))

# Uppdatera fält i tabellen
sql_upd = "UPDATE lektion1 SET name = '{name}' WHERE id = '{id}'"
mycursor.execute(sql_upd.format(name = new_name, id = id))

# Laddar upp den nya uppgiften
mydb.commit()

# Konfimerar att uppgiften har uppdaterats
print(mycursor.rowcount, ' has been updated!')


# Frågar användaren att ange vad de nya namn och email adress är och vart den vill uppdatera
new_name = str(input('Ange nytt namn: '))
new_email = str(input('Ange ny email adress: '))
id = str(input('Ange ID på den du vill uppdatera: '))

# Uppdatera fälten i tabellen
sql_upd = "UPDATE lektion1 SET name = '{name}', SET email = '{email}' WHERE id = '{id}'"
mycursor.execute(sql_upd.format(name = new_name, email = new_email, id = id))

# Laddar upp den nya uppgiften
mydb.commit()

# Konfimerar att uppgiften har uppdaterats
print(mycursor.rowcount, ' has been updated!')

# Frågar användaren att ange vad och vart den vill uppdatera
id = str(input('Ange ID som du vill ta bort: '))

# Uppdatera fält i tabellen
sql_delete = "DELETE FROM lektion1 WHERE id = '{id}'"
mycursor.execute(sql_delete.format(id = id))

# Slutför borttagandet av kollumnen
mydb.commit()

# Konfimerar att uppgiften har raderats
print(mycursor.rowcount, ' has been removed!')
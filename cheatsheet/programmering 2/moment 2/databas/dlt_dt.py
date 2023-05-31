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

# Ber användaren ange vilket id som ska tas bort
identity = input('Ange ID på den rad du vill ta bort: ')

# Uppdaterar databasen
sql = f"DELETE FROM intro_db WHERE id = '{identity}'"
mycursor.execute(sql)

# Slutför borttagningen
mydb.commit()

# Konfirmerar att raden tagits bort
print(mycursor.rowcount, " has been deleted!")
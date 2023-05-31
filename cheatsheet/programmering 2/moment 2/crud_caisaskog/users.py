# Importerar mysql.connector
import mysql.connector

# Importerar tidsmodul
import datetime

# Ansluter till databasen
mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",  
    database = "crud_caisaskog"
)

# Ger databasen ett variabel namn
mycursor = mydb.cursor()

# Class for users 
# Creating a new user/sign up
# Log in functions
# Log out functions
# Change username or password functions

class Users:
    def __init__(self) -> None:
        self.user_id = None
        self.username = None
        self.password = None
        self.creation_date = None

    # Creates the user and adds them to the database
    def createUser(self, username, password):
        # Kollar om användarnamnet redan finns
        userExisting = self.userExists(username)

        # Om användarnamnet är taget
        if userExisting == False:
            return print("Användarnamnet är taget, vänligen försök igen")
        # Annars kommer koden fortsätta

        # Lista som informationen lagras i temporärt
        val = []

        # Anger vilken tabell man vill lägga in i och vad för uppgifter som ska läggas in
        sql = "INSERT INTO users(user_id, username, password, creation_date) VALUES (%s, %s, %s, %s)"
        time = datetime.datetime.now()
        val.append(("NULL", username, password, time))
        # Lägger in uppgifter
        mycursor.executemany(sql, val)
        # Laddar upp dem
        mydb.commit()

        # Konfirmerar för användaren att kontot skapats
        if mycursor:
            print(mycursor.rowcount, "konto har skapats")
            # Lägger in informationen i ett objekt och användaren loggas in
            self.username = username
            self.password = password
        else: 
            print("Något gick fel när kontot försökte skapas")

    # Låter en inloggad användare att ändra deras användarnamn
    # (kommer ändras i sessionen också)
    def editUsername(self, newUsername):
        # Kollar om det nya användarnamnet redan är taget
        userExisting = self.userExists(newUsername)

        # Om användarnamnet är taget
        if userExisting == False:
            return print("Användarnamnet är taget, vänligen försök igen")
        # Annars kommer koden fortsätta

        # Anger vilken tabell man vill ändra och vad för uppgift som man vill ändra
        sql = "UPDATE users SET username = %s WHERE user_id = %s"
        mycursor.execute(sql, (newUsername, self.user_id,))
        mydb.commit()

        # Konfirmerar att uppgiften uppdaterades
        if mycursor.rowcount:
            self.username = newUsername
            print(f"Ditt konto har ändrats\nDitt nya användarnamn är {self.username}")
        else: 
            print('Något gick fel, vänligen försök igen')

    # Låter en inloggad användare att ändra deras lösenord
    # (kommer ändras i sessionen också)
    def editPassword(self, newPassword):
        # Kollar om det nya användarnamnet redan är taget
        userExisting = self.userExists(newPassword)

        # Om användarnamnet är taget
        if userExisting == False:
            return print("Användarnamnet är taget, vänligen försök igen")
        # Annars kommer koden fortsätta

        # Anger vilken tabell man vill ändra och vad för uppgift som man vill ändra
        sql = "UPDATE users SET password = %s WHERE user_id = %s"
        mycursor.execute(sql, (newPassword, self.user_id,))
        mydb.commit()

        # Konfirmerar att uppgiften uppdaterades
        if mycursor.rowcount:
            self.password = newPassword
            print(f"Ditt lösenord har ändrats")
        else: 
            print('Något gick fel, vänligen försök igen')

    # Låter användaren ta bort sitt konto helt och hållet
    # (kommer ändras i sessionen också (loggas ut))
    def deleteAccount(self):

        # Kommer implementera detta om jag har tid
        def forceResponse(response):
            pass

        response = input('Är du säker på att du vill ta bort ditt konto? Detta går inte att ångras (Y/N)\n')

        # Om användaren svarar ja
        if response.lower() == "y":
            # Tar bort informationen
            sql = "DELETE FROM users WHERE user_id = %s"
            mycursor.execute(sql, (self.user_id,))
            mydb.commit()

            # Konfimerar att uppgiften har raderats
            print(mycursor.rowcount, ' konto har tagits bort!')
            self.signOut()

        else:
            return print("Återgår till menyn...")


    # Kollar om ett visst användarnamn finns i systemet
    def userExists(self, username):
        # Läser in alla användarnamn som finns i systemet
        mycursor.execute("SELECT username FROM users")
        usernames = mycursor.fetchall()

        for name in usernames:
            # Kollar om användarnamnet finns i listan oavsett stora eller små bokstäver
            if name[0].lower() == username.lower():
                # Returnerar ja eller nej (False = finns )
                return False

    # Kollar om lösenordet matchar
    def passwordMatch(self, password, dbpassword):
        if password == dbpassword:
            return False
        else:
            return True

    # Kollar om angett användarnamn och lösenord matchar
    def matchAccountDetails(self, username, password):
        # Lägger in username i objektet för att koden ska funka 
        # (kommer resettas om användarnamnet inte matchar lösenordet)
        self.username = username

        # Hämtar användarens lösenord
        sql = "SELECT password FROM users WHERE username = %s"
        mycursor.execute(sql, (self.username,))
        # Får lösenordet
        dbpassword = mycursor.fetchone()
        dbpassword = dbpassword[0]

        # Jämför lösenordet
        pwdNotMatch = self.passwordMatch(password, dbpassword)
        return pwdNotMatch

    # Lets an already registrered user to login
    def login(self, username, password):
        # Letar efter användaren efter användarnamnet 
        userExisting = self.userExists(username)

        # Om användarnamnet inte finns
        if userExisting != False:
            return print("Användarnamnet matcher inte med ett konto, vänligen försök igen eller skapa ett nytt konto")
        # Om användarnamnet finns fortsätter koden

        # Kollar om lösenordet matchar lösenordet
        detailsMatch = self.matchAccountDetails(username, password)

        # Om detaljerna inte matchar
        if detailsMatch != False: 
            return print("Användarnamnet och lösenordet matchar inte, vänligen försök igen")
        # Om dem matchar fortsätter koden

        # Lägger in informationen i ett objekt och användaren loggas in
        if detailsMatch == False: 
            self.username = username
            self.password = password
            # Skapar en variabel som kan använda sig av variabler
            sql = "SELECT user_id, creation_date FROM users WHERE username = %s"
            # Hämtar id och creation date
            mycursor.execute(sql, (self.username,))
            result = mycursor.fetchone()
            # Lägger in det i objektet för lättare hämtning (eftersom dessa inte ändras)
            self.user_id = result[0]
            self.creation_date = result[1]
            return print('Inloggning lyckad')
        
        else: 
            self.signOut()
        
        # Det är inte meningen att komma hit, så error message kommer upp
        print("Något gick fel vid inloggningen, vänligen försök igen")


    # Lets a logged in user to sign out of their account
    def signOut(self):
        # Rensar objektet, detta kommer göra så att appen läser en som utloggad och kräver en ny inloggning
        self.username = None
        self.password = None
        self.user_id = None
        self.creation_date = None
        print('Utloggad')
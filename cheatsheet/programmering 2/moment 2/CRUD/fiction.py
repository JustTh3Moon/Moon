# Importerar mysql.connector
import mysql.connector


# Class for fiction
# Subclass for movie and tv-shows
# Add new fiction function 
# (fiction as in a new object to let the user add information about a movie or show)
# Kommentera function

# Ansluter till databasen
mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",  
    database = "crud_caisaskog"
)

# Ger databasen ett variabel namn
mycursor = mydb.cursor()

class Fiction:
    def __init__(self, title, director, fiction_type, status) -> None:
        self.fiction_id = int
        self.title = title
        self.director = director
        self.fiction_type = fiction_type
        self.status = status
        self.rating = str
        self.comment = str

    # Funktion som visar listan på alla titlar användaren har inlagda
    def viewList():
        pass

    # Funktion som kollar om en titel redan finns
    def fictionExists():
        pass

    # Lets a logged in user add new fiction to the database
    def addFiction(user_id):
        # Dictionary på fråga beroende på vad för information som man vill fråga efter
        question = {
            'title': 'Ange titeln: ',
            'director': 'Ange regissör: ',
            'fiction_type': 'Ange typ fiktion (Film/Serie): ',
            'status': 'Ange status: ',
            'length': 'Ange längden: ',
            'season': 'Ange vilken säsong det är: ',
            'episodes': 'Ange hur många avsnitt det är: ',
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

        # Frågar användaren efter varje information som krävs
        title = get_input('title')
        director = get_input('director')
        fiction_type = get_input('fiction_type')
        status = get_input('status')

        if fiction_type.lower() == 'film':
            length = get_input('length')
            season = 'N/A'
            episodes = 'N/A'
        if fiction_type.lower() == 'serie':
            season = get_input('season')
            episodes = get_input('episodes')
            length = 'N/A'

        # Lista som informationen lagras i temporärt
        val = []

        # Anger vilken tabell man vill lägga in i och vad för uppgifter som ska läggas in
        sql = "INSERT INTO fiction(fiction_id, title, director, fiction_type, length, season, episodes) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val.append(("NULL", title, director, fiction_type, length, season, episodes))
        mycursor.executemany(sql, val)
        mydb.commit()

        # Hämtar fiction_id
        sql = "SELECT fiction_id FROM fiction WHERE title = %s"
        mycursor.execute(sql, (title,))
        fiction_id = mycursor.fetchone()
        print(fiction_id)

        # Lägger in status i reviews tabellen 
        # (länkas tillbaka tillbaka med user_id och fiction_id)
        sql = "INSERT INTO reviews(review_id, user_id, fiction_id, status, rating, comment) VALUES (%s, %s, %s, %s, %s, %s)"
        val = ("NULL", user_id, fiction_id[0], status, 'N/A', 'N/A')
        mycursor.executemany(sql, val)
        mydb.commit()

        # Skapar ett nytt objekt bereonde på om det är en film eller serie
        if fiction_type.lower() == 'film':
            nyFiktion = Movie(title, director, fiction_type, status, 'N/A', 'N/A', length)
        elif fiction_type.lower() == 'serie':
            nyFiktion = Show(title, director, fiction_type, status, 'N/A', 'N/A', season, episodes)

        # Konfirmerar om datan lagrades eller ej
        if mycursor:
            print(nyFiktion.title, "har lagts in med", nyFiktion.status)
        else: 
            print('Något gick fel, vänligen försök igen')

    # Lets a user change the status of a title
    def editStatus(self):
        pass

    # Lets a logged in user define a review for a title (rating and comment)
    def review(self):
        pass

class Movie(Fiction):
    def __init__(self, title, director, fiction_type, status, rating, comment, length) -> None:
        super().__init__(title, director, fiction_type, status, rating, comment)
        self.length = length

class Show(Fiction):
    def __init__(self, title, director, fiction_type, status, rating, comment, season, episodes) -> None:
        super().__init__(title, director, fiction_type, status)
        self.season = season
        self.episodes = episodes
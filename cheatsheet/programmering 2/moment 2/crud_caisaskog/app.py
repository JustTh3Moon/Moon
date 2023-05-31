import sys 

sys.dont_write_bytecode = True #prevents random __pycache__ folders to be created 

# Importerar klasser
import fiction
import users
from menus import *

class App:
    def __init__(self) -> None:
        self.running = True

    # Funktion som startar applikationen
    def run(self):
        if user.password == None:
            self.mainMenu()
        # Om användaren är inloggad
        else: 
            self.loggedInMenu()

    # Kollar om en input är en response
    def isInt(self, response):
        while True:
            try:
                if int(response):
                    # Om det en siffra skickas den tillbaka
                    return int(response)
            except:
                return False

    # Funktion som validerar om användaren anger ett giltigt alternativ
    def validResponse(self, question, amount):
        while True:
            # Frågar efter ett svar, kollar om den är en siffra
            response = self.isInt(input(question))
            # Om den är false kommer loopen börja om och fråga på nytt
            if response == False:
                print('Var vänlig ange ett nummer')
                continue

            # Kollar om svaret är inom de giltiga alternativen
            if 0 < response <= amount:
                return response
            else: 
                print('Vänligen ange ett giltigt alternativ')
                continue

    # Huvud menu med alternativ
    def mainMenu(self):
        # Frågar användaren vad den vill göra och svaret går igenom 2 checkar
        response = self.validResponse(mainMenuAlt, 3)

        # Om användaren anger 3 avslutas programmet
        if response == 3:
            self.quit()
            return

        commands = {
            1: user.login,
            2: user.createUser,
        }

        # Låter användaren ange sin login information
        username = input('Username: ')
        password = input('Password: ')

        # Kör kommando bereoende på om användaren vill logga in eller skapa ett konto
        commands[response](username, password)

    def loggedInMenu(self):
        # Frågar användaren vad den vill göra och svaret går igenom 2 checkar
        response = self.validResponse(loggedInMenuAlt.format(user.username), 4)

        # Om användaren anger 4 avslutas programmet
        if response == 4:
            self.quit()
            return

        commands = {
            1: self.fictionMenu,
            2: self.editUser,
            3: user.signOut,
        }

        commands[response]()

    def editUser(self):
        # Frågar användaren vad den vill göra och svaret går igenom 2 checkar
        response = self.validResponse(accountSettingsAlt, 4)

        # Om användaren anger 4 återgår programmet till föregående meny
        if response == 4:
            print('Återgår till menyn...')
            return

        commands = {
            1: user.editUsername,
            2: user.editPassword,
            3: user.deleteAccount,
        }

        accountDetail = {
            1: 'användarnamn',
            2: 'lösenord',
        }

        if response == 3:
            commands[response]()
        else: 
            new = input(f'Ange nytt {accountDetail[response]}: ')
            commands[response](new)

    def fictionMenu(self):
        # Frågar användaren vad den vill göra och svaret går igenom 2 checkar
        response = self.validResponse(fictionMenuAlt, 3)

        # Om användaren anger 3 avslutas programmet
        if response == 3:
            print('Återgår till menyn...')
            return

        commands = {
            1: fiction.Fiction.viewList(),
            2: fiction.Fiction.addFiction(user.user_id),
        }

        commands[response]

    # Om användaren väljar alternativet "Avsluta programmet"
    def quit(self):
        print('Avslutar program...')
        self.running = False

# Main loop

app = App()

# Skapar en ny user för användaren att använda under sessionen
user = users.Users()

while app.running:
    app.run()

# This is the end of the code
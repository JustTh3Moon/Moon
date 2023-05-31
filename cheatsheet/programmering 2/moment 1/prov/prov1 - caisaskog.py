# Prov 1: Uppgift 3 - Caisa Skog 

# Importerar random för att kunna slumpa fram en siffra
import random as r

# Superklass film med egenskaper av titel och längd
class Film:
    def __init__(self, titel = '', längd = 0):
        self.titel = titel
        self.längd = längd

# Subklass till Film, har utöver filmens egenskaper även instansvariabeln fightningsgrad och klassmetoden tittarupplevelsen
class Action(Film):
    def __init__(self, title = '', length = 0, grad = int(1-5)):
        super().__init__(title, length)
        self.fightningsgrad = grad
        
    # Metod som beskriver tittarupplevelsen
    def tittarupplevelse(self, grad):
        if self.fightningsgrad <= 3:
            print('Inte mycket fight här inte!')
        elif self.fightningsgrad > 3:
            print('Här kommer det bli fight minsann!')
    
# Subklass till Film, har utöver filmens egenskaper även instansvariabeln kärleksnivå och klassmetoden tittarupplevel
class Romantik(Film):
    def __init__(self, title = '', length = 0, nivå = 0):
        super().__init__(title, length)
        self.kärleksnivå = nivå

    # Metod som beskriver tittarupplevelsen
    def tittarupplevelse(self, kärleksnivå):
        if self.kärleksnivå < 3:
            print('Här blir det inte mer än att hålla handen.')
        elif self.kärleksnivå > 2:
            print('Här kan vi förvänta oss en puss eller två!')

# Tvingar det att vara en siffra mellan siffror som anges som parametrar
def siffra(start, slut):
    start = int(start)
    slut = int(slut)

    while True: 
        # Kollar så användaren anger en siffra
        try:
            nummer = int(input(f'Vänligen ange en siffra:\n'))
        except ValueError:
            continue

        # Kollar så att siffran möter intervallet som metoden anger från där den blivit kallad
        if nummer > start - 1 and nummer < slut + 1:
            return nummer
        else:
            print(f'Vänligen ange en siffra mellan {start} och {slut}!')       

# Typ en universell printer, (jag vet att det finns ett sätt att få in det under klasserna men jag kan inte komma på hur just nu)
def printer(i, ja):
    
    # Tom linje så det ska se lite bättre ut
    print('')
    print(f'Jag har valt ut följande film åt dig: {bibliotek[i].titel}, den är {bibliotek[i].längd} minuter lång.')
    # Försöker printa tittarupplevelsen
    
    # Om ja är True så kommer genren att skrivas ut här
    if ja:
        print('Såhär säger andra om filmen: ')
        # Om det vore en action film
        try: 
            Action.tittarupplevelse(bibliotek[i], bibliotek[i].fightningsgrad)
        except:
            print('Detta är en romantisk film')

        # Om det vore en action film
        try: 
            Romantik.tittarupplevelse(bibliotek[i], bibliotek[i].kärleksnivå)
        except:
            print('Detta är en action film')
        
        # Tom linje för att det ska se lite bättre ut
        print('')


# Låter användaren lägga till en ny film
def ny():
    
    # Låter användaren få fylla in informationen
    titel = input('Ange titel:\n')

    # Låser användaren så den anger endast siffror
    while True: 
        try: 
            längd = int(input('Ange längd:\n'))
            break
        except ValueError: 
            print('Vänligen ange endast siffror')
            continue

    # Frågar om vilken genre det är
    while True: 
        genre = input('Ange ifall det är en Action eller Romantik film:\n')

        # Är det rätt inskrivet så kan användaren gå vidare
        if genre.lower() == 'romantik' or genre.lower() =='action':
            break
        # Är det inte rätt inskrivet får användaren försöka igen
        else: 
            print('Vänligen ange en giltig genre')
            continue

    # Efterfrågar graden av tittarupplevelsen
    print('Hur är tittarupplevelsen för den här filmen?')
    nummer = siffra(1, 5)
    
    # Skapar filmen beroende på genre
    genre = genre.lower()
    if genre == 'action':
        film = Action(titel, längd, nummer)

    elif genre == 'romantik':
        film = Romantik(titel, längd, nummer)

    # Lägger in filmen i biblioteket
    bibliotek.append(film)

# Visar en meny på ifall genren på filmen spelar roll eller ej
def slumpa():

    while True:
        # Presenterar en meny
        print('Vet du inte vilken film du vill se? I så fall kan jag hjälpa dig! Börja med att välja genre:\n1. Spelar ingen roll\n2. Action\n3. Romantik\n4. Till huvudmenyn') 
        val = siffra(1, 4)
        if val == 4:
            break
        if val == 1: 
            # Slumpar fram en random film
            längd = len(bibliotek) - 1
            rng = r.randint(0, längd)
            # Ja betyder att genre inte är speciferad
            ja = True
            # Går det skrivs information ut
            printer(rng, ja)
        
        # Ifall användaren vill ha en action film
        if val == 2:
            while True:
                # Slumpar fram en random film
                längd = len(bibliotek) - 1
                rng = r.randint(0, längd)
                
                # Kollar om det går att printa action upplevelsen
                try: 
                    print('Såhär säger andra om denna film!')
                    Action.tittarupplevelse(bibliotek[rng], bibliotek[rng].fightningsgrad)
                
                # Går det inte så börjar det om
                except: 
                    continue

                # Ja är false, och betyder att genren är speciferad
                ja = False
                # Går det skrivs information ut
                printer(rng, ja)
                break
            
        # Ifall användaren vill ha en romantisk film
        if val == 3:
            while True:
                # Slumpar fram en random film
                längd = len(bibliotek) - 1
                rng = r.randint(0, längd)
                
                # Kollar om det går att printa action upplevelsen
                try: 
                    print('Såhär säger andra om denna film!')
                    Romantik.tittarupplevelse(bibliotek[rng], bibliotek[rng].kärleksnivå)
                
                # Går det inte så börjar det om
                except: 
                    continue

                # Ja är false, och betyder att genren är speciferad
                ja = False
                # Går det skrivs information ut
                printer(rng, ja)
                break
        
        # Återgår till huvudmenyn
        break

# Huvudprogram

# Skapar lista på 7 objekt
bibliotek = []

film1 = Action('Bullet Train', 126, 5)
film2 = Action('The Gray Man', 122, 2)
film3 = Action('Memory', 114, 4)
film4 = Action('Black Crab', 114, 1)
film5 = Romantik('The Lost City', 112, 3)
film6 = Romantik('Purple Hearts', 122, 1)
film7 = Romantik('After We Fell', 99, 4)

bibliotek.extend([film1, film2, film3, film4, film5, film6, film7])

running = True

while running:

    # Huvudmenyn visas och körs till användaren väljer ett giltigt alternativ 
    # Presenterar alternativen
    print('Välkommen till ditt filmbibliotek, välj vad du vill göra:\n1. Lägg till ny film i biblioteket\n2. Vad ska jag se för film idag? (Slumpa fram en film från biblioteket)\n3. Avsluta')
    val = siffra(1, 3)
    
    # Avslutar programmet
    if val == 3:
        print('Ha det bra, syns nästa gång!\nAvslutar programmet...')
        exit()
    # Slumpar en film
    elif val == 2: 
        slumpa()

    # Låter användaren lägga till en ny film i biblioteket
    elif val == 1:
        ny()
        print('En ny film har lagts in!')

# Detta är slutet av koden
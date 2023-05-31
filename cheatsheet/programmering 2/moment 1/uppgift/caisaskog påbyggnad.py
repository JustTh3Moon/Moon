# Uppgift: Biblioteket påbyggande uppgift

class Bok:
    def __init__(self, titel = '', författare = '', utlånad = False) -> None:
        self.titel = titel
        self.författare = författare
        self.utlånad = utlånad

     # Lånar ut boken genom att ändra utlånads instansvariabeln
    def lånaUt(objekt):
        objekt.utlånad = True

    # Återlämnar boken genom att ändra utlånads instansvariabeln
    def återlämna(objekt):
        objekt.utlånad = False

# Definerar fem instanser av klassen Bok
bok1 = Bok('Mio min Mio', 'Astrid Lindgren', False)
bok2 = Bok('Var är bus-Alfons?', 'Gunilla Bergström', True)
bok3 = Bok('Stora boken om Mamma Mu och Kråkan', 'Jujja Wieslander', False)
bok4 = Bok('LasseMajas detektivbyrå: Födelsedagsmysteriet', 'Martin Widmark', True)
bok5 = Bok('Dagbok för alla mina fans: På hal is', 'Jeff Kinney', False)

# Lista på alla böcker som finns på biblioteket
böcker = [bok1, bok2, bok3, bok4, bok5]

# Funktion som skriver ut informationen om en bok 
def info(objekt):
    print(f'Titel: {objekt.titel}\nFörfattare: {objekt.författare}\nUtlånad: {objekt.utlånad}\n')

# Funktion som skriver ut alla böcker samt dess status
def allaBöcker(lista):
    print('\nBöcker:')

    # Loop som går igenom varje bok
    for o in lista:
        # Hittar numret för boken
        x = lista.index(o)

        # Skriver ut nummer i listan, titel och författare
        print(f'--- #{x} {o.titel} - {o.författare}')

        # Om den är true är den utlånad och skriver ut det
        if o.utlånad:
            print('Status: Utlånad')

        # Annars är den ej utlånad och det skrivs ut
        else: 
            print('Status: Ej utlånad')

def redanUtlånad(o):
    # Kollar om boken är utlånad redan
    if o.utlånad:
        print('Boken är tyvärr redan utlånad.')
        return
    # Om boken inte är utlånad
    else: 
        print(f'Du kan låna {o.titel} av {o.författare} i två veckor. Tack för att du lånar <3')
        # Sätter den som utlånad
        Bok.lånaUt(o)
        return
    

# Funktion för att låna
def låna():
    antal = len(böcker)
    while True:
        try: 
            # Ber användaren ange vilken bok den vill låna
            lånebok = int(input('\nVilken bok vill du låna? Ange nummer: '))
            if 0 <= lånebok and lånebok < antal:
                o = böcker[lånebok]
                redanUtlånad(o)
                break
            else: 
                print('Boken du söker finns inte, välj ett giltigt nummer')
        except ValueError: 
            print('Var god ange endast en siffra!')

def igen():
    global running
    while True:
        #Fråga om användaren vill göra en ny omvandling
        igen = input("Vill du läsa in böckerna igen? (Ja/Nej)\n")
        igen = igen.lower()
        if igen == "ja":
            break
        elif igen == "nej":
            running = False
            break
        else: 
            print("Inte ett giltigt svar, snälla svara igen")

running = True

while running: 
    # Välkomnar användaren till biblioteket
    print("Välkommen till biblioteket!")

    # Skriver ut alla böcker som finns på biblioteket
    allaBöcker(böcker)

    # Frågar användaren vad den vill låna för bok
    låna()

    # Frågar om användaren vill låna igen
    igen()

# Detta är slutet av koden
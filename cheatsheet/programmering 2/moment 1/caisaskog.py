class Rektangel:
    def __init__(self, bredd = 0, höjd = 0):
        self.bredd = bredd
        self.höjd = höjd

    # Bredd getter
    @property 
    def b(self):
        return self.bredd
    
    # Bredd setter
    @b.setter
    def b(self, b):
        self.bredd = b

    # Höjd getter
    @property
    def h(self):
        return self.höjd

    # Höjd setter
    @h.setter
    def h(self, h):
        self._höjd = h

    # Beräknar omkretsen
    @property
    def omkretsen(self):
        return self.höjd * 2 + self.bredd * 2

    # Beräknar arean
    @property
    def arean(self):
        return self.höjd * self.bredd
    
    # Skriver ut informationen om figuren
    def printer(self):
        print(f'Höjd: {self.höjd} l.e\nBredd: {self.bredd} l.e\nOmkrets: {self.omkretsen} l.e\nArea: {self.arean} a.e')

    # Definerar del metoden
    def __del__(self):
        print('Figuren är borttagen')

# Tvingar användaren att ange en siffra när en längd ska anges
def ist_Int(sida):
    while True:
        try: 
            antal = int(input(f'Ange {sida}en: '))
        except ValueError:
            print('Vänligen ange endast siffror. \n')
            continue
        return antal

# Kollar så att användarens inmatning är en giltig siffra
def eligable_Int():
    # Kollar ifall det inte finns några figurer sparade
    if len(figurer) == 0:
        print('Det finns inga sparade rektanglar\n')
    while True: 
        # Frågar om siffran
        r = input('Vänligen ange siffran på figuren du vill ta bort:\n')
        try: 
            r = int(r)
        # Fångar upp om användaren inte anger en siffra
        except ValueError:
            print('Vänligen ange endast siffror')
            continue
        # Returnerar siffran
        return r

# Lista för att spara figurerna        
figurer = []

# Huvudprogram
while True:

    # Presenterar användaren med huvudmeny
    val = input('Vad vill du göra:\n1. Lägga in en ny rektangel\n2. Radera en lagrad rektangel\n3. Avsluta programmet\n')
    try:
        # Testar att se om det är en siffra
        val = int(val)

    # Fångar om något annat än en siffra fångas
    except ValueError:
        print('Vänligen ange endast siffror')
        continue

    # Avslutar programmet
    if val == 3:
        exit('Avslutar programmet...')

    # Radera en figur
    elif val == 2: 
        # Besvarar ifall listan är tom
        if len(figurer) == 0:
            print('Finns inga sparade rektanglar')
            continue
        else: 
            # Skriver ut alla sparade rektanglar
            for obj in figurer:
                print(f'Rektangel #{figurer.index(obj)}')
                # Skriver ut rektangelns information
                Rektangel.printer(obj)
            # Får fram en giltig siffra
            r = eligable_Int()
            # Tar bort figuren
            del figurer[r]
            
            
    # Lägg in ny figur
    elif val == 1:
        b = ist_Int('bredd')
        h = ist_Int('höjd')

        # Lagrar figuren
        figur = Rektangel(b, h)
        figurer.append(figur)
        print('Följande rektangel sparas: ')
        Rektangel.printer(figur)
        
        
    else: 
        print('Var vänlig ange en giltig siffra')

# Detta är slutet av koden
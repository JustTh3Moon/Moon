# Dictionary med enheter
enheter = {
    1: "meter",
    2: "centimeter",
    3: "foot/feet",
    4: "inch"
}

# Nested dictionary med alla förhållanden  
förhållanden = {

    # Relation från meter till resten av enheterna
    "meter": { 
        1: 1,
        2: 100,
        3: 3.280839895, 
        4: 0.0833333333
    },

    # Relation från centimeter till resten av enheterna
    "centimeter": {
        1: 0.01,
        2: 1,
        3: 0.032808399, 
        4: 0.3937007874
    },

    # Relation från foot till resten av enheterna
    "foot": {
        1: 0.3048,
        2: 30.48,
        3: 1, 
        4: 12
    },

    # Relation från inch till resten av enheterna
    "inch": {
        1: 0.0254,
        2: 2.54,
        3: 0.0833333333,
        4: 1
    }

}

# Funktion som omvandlar 
def omvandling(från, till, siffra):
    # Ifall från enheten är meter
    if från == 1:
        resultat = siffra * förhållanden["meter"][till]

    # Ifall från enheten är centimeter
    elif från == 2: 
        resultat = siffra * förhållanden["centimeter"][till]

    # Ifall från enheten är foot
    elif från == 3: 
        resultat = siffra * förhållanden["foot"][till]

    # Ifall från enheten är inch
    elif från == 4: 
        resultat = siffra * förhållanden["inch"][till]

    # Skriver ut resultatet
    print(f"Resultatet: {siffra} {enheter[från]} = {resultat:.2f} {enheter[till]}")

#Variabler
playing = True
alternativen = """
Välj mellan alternativen:
1. Meter
2. Centimeter
3. Foot
4. Inch
5. Avsluta
"""

# Tvingar en giltig siffra mellan 1-5
def tvingaSiffra(siffra):
    if siffra == 5:
        # Avbryter koden
        exit()
    elif siffra > 0 and siffra < 5:
        return True
    # Ifall användaren anger en siffra mindre än noll eller större än fem
    else: 
        print("Inte ett giltigt nummer, välj mellan 1-5!")

# Funktion som frågar vilken enhet användaren vill omvandla från och till
def tillOchFrån():
    global från
    global till

    # Skapar en loop för att låsa användaren här tills den svarar ett giltigt svar
    while True: 
        try: 
            från = int(input(f"Vilken enhet vill du omvandla från? {alternativen}"))

        # Fångar om användaren skriver något som inte är en siffra
        except ValueError:
            print("Du måste skriva in en siffra mellan 1-5!")
            # Påbörjar ny iteration
            continue
    
        if tvingaSiffra(från) == True:
            break
    
    # Skapar en loop för att låsa användaren här tills den svarar ett giltigt svar
    while True: 
        try: 
            till = int(input(f"Vilken enhet vill du omvandla till? {alternativen}"))
        except ValueError:
            print("Du måste skriva in en siffra mellan 1-5!")
            # Påbörjar ny iteration
            continue

        # Tvingar en giltig siffra
        if tvingaSiffra(till) == True:
            break

    # Skickar tillbaka de framtagna siffrorna
    return från, till

# Tvingar en giltig siffra
def siffran():
    global siffra

    while True:
        try:
            # Siffran som användaren vill ska omvandlas
            siffra = float(input(f"Skriv in antal {enheter[från]} här: "))
            break
        except ValueError:
            print("Ange en giltig siffra!")

# Funktion som frågar om användaren vill spela igen
def igen():
    global playing

    while True:
        #Fråga om användaren vill göra en ny omvandling
        igen = input("Vill du göra en ny omvandling? (Ja/Nej)\n")
        igen = igen.lower()
        if igen == "ja":
            break
        elif igen == "nej":
            playing = False
            break
        else: 
            print("Inte ett giltigt svar, snälla svara igen")

# Programloopen
while playing:
    # Fråga vilken enhet användaren vill omvandla från och till
    från, till = tillOchFrån()

    # Fråga vilken siffra som ska omvandlas
    siffran()

    # För in alla samlade variabler i funktionen som gör själva omvandlingen
    omvandling(från, till, siffra)

    # Kallar funktionen som frågar om användaren vill köra igen
    igen()

# Slutet av koden
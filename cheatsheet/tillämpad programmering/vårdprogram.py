# --- Variabler
running = True

# Alternativen för huvudmenyn
alt = '''
1. Patientslista
2. Lägg in ny patient
3. Avsluta'''

# Start nummer för patient
nr = 1

# Returnerar värde på vad som användaren valde att göra
def val():
    print(f'\nVälkommen till vårdpersonalens patientlista! För att gå vidare, välj en av nedanstående alternativ {alt}')
    
    while True: 
        try:
            svar = int(input(''))
        
        # Fångar om användaren anger något annat än en siffra
        except ValueError:
            print('Var vänlig ange endast siffror')
            continue
        
        # Stänger av programmet
        if svar == 3:
            exit('Avslutar program...')

        # Skickar den till att lägga in en ny patient
        elif svar == 2:
            return False

        # Skickar den till patientlistan
        elif svar == 1:
            return True
        
        # Om användaren anger en ogiltig siffra
        else: 
            print('Vänligen ange en siffra mellan 1-3')

# Definerar en dictionary som kommer innehålla listan på patienterna
patientlista = {}

# Funktion som skriver ut namnet på varje patient i systemet
def visaPatientlista():
    antal = len(patientlista)
    for i in range(antal):
        i += 1
        # Gör om siffran till en sträng som nyckeln representeras som 
        i = str(i)
        # Skriver ut numret och namnet på patienten
        print(f'#{i} {patientlista[i][0]}')

    while True:
        # Frågar användaren vad den vill göra och testar så att det är en siffra
        try: 
            svar = int(input('\nVad vill du göra nu?\n1. Visa mer information om en patient\n2. Gå tillbaka\n'))
        
        # Fångar om användaren anger något som inte är en siffra
        except ValueError:
            print('Var vänlig ange endast siffror')
            continue

        # Om det är en tvåa så går den tillbaka till huvudmenyn
        if svar == 2:
            break
        
        # Skickar den vidare till att kunna se en patiens information
        elif svar == 1:
            visaPatient()

        # Om användaren anger ett ogiltigt nummer
        else: 
            print('Ange en siffra mellan 1-2')
        

# Funktion osm skriver ut mer i detalj om en patient
def visaPatient():
    while True:

        # Frågar om numret för patienten som användaren vill skriva ut
        try: 
            nr = input('Ange numret på patienten du vill se mer information om:\n')

        # Om användaren anger något annat än siffror
        except ValueError:
            print('Vänligen ange endast siffror')
        
        # Skriver ut patientens information
        try: 
            print(f'\nPatient #{nr}\nNamn: {patientlista[nr][0]}\nÅlder: {patientlista[nr][1]}\nBlodtyp: {patientlista[nr][2]}\nAvdelning: {patientlista[nr][3]}\n')
            break

        # Om användaren anger en siffra på en patient som inte finns
        except KeyError: 
            print('Vänligen ange en giltig siffra')
            continue
        

# Tillåter användaren att lägga till en ny patient i systemet
def nyPatient(nr): 
    while True: 
        print('Var vänlig ange informationen som frågas nedan:')
        name = input('Namn: ')
        age = input('Ålder: ')
        blodtyp = input('Blodtyp: ')
        avdelning = input('Avdelning: ')

        # Skriver ut en preview av all information 
        print(f'\nNamn: {name}\nÅlder: {age}\nBlodtyp: {blodtyp}\nAvdelning: {avdelning}\n')

        giltig = True

        while giltig: 
            # Frågar om användaren är nöjd med den ifyllda informationen
            svar = input('Ser detta rätt ut? (Ja/Nej)\n')

            # Kollar så användaren anger ja eller nej
            if svar.lower() == "ja" or svar.lower() == "nej":
                giltig = False
            else: 
                print('Var vänlig ange Ja eller Nej')
                continue

        # Gör om till en sträng så man kan hitta med hjälp av key i dictionary
        nr = str(nr)

        # Om användaren svarade ja så sparas patienten 
        if svar.lower() == 'ja':
            patientlista[nr] = [name, age, blodtyp, avdelning]
            break

        # Om användaren svarade nej kommer hela processen börja om
        elif svar.lower() == 'nej':
            continue

while running: 
    # Huvudmeny
    vald = val()

    if vald == True:
        visaPatientlista()
    else:
        nyPatient(nr)
        nr += 1
# Detta är slutet av koden
# Frågar användaren ifall dem är trött
tired = input("Är du trött? (Ja/Nej)\n") 

energi = 0

# Om användaren svarar ja
if tired.lower() == "ja":
    print("Gå och lägg dig...")
    energi -= 1
# Om användaren svarar nej
elif tired.lower() == "nej":
    print("Okej, va vaken :)")
    energi += 1

# Det blev fel någonstans
else: 
    print("Jag kan inte hjälpa dig, sorry")

# Jämför ifall användaren har energi eller ej
if energi < 0:
    print("eller drick kaffe för energi")
elif energi > 0:
    print("Slay, queen 💅✨")

# Avslutning
print("Ha det bra!")

# Detta är slutet av koden
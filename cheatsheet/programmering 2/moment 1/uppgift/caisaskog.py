# Uppgift: Biblioteket grundläggande uppgift

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

# Definerar två instanser av klassen Bok
bok1 = Bok('Mio min Mio', 'Astrid Lindgren', False)
bok2 = Bok('Var är bus-Alfons?', 'Gunilla Bergström', True)

# Funktion som skriver ut informationen om en bok 
def info(objekt):
    print(f'Titel: {objekt.titel}\nFörfattare: {objekt.författare}\nUtlånad: {objekt.utlånad}\n')

# Skriver ut informationen om bok 1 och bok 2
info(bok1)
info(bok2)

# Lånar bok 1
Bok.lånaUt(bok1)

# Skriver ut informationen efter att lånat
info(bok1)

# Återlämnar bok 2
Bok.återlämna(bok2)

# Skriver ut information efter återlämning
info(bok2)

# Detta är slutet av koden
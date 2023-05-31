class Bil:
    def __init__(self, ägare = None, regnummer = '', fabrikat = '', årsmodell = '', tjänstevikt = 0, motoreffekt = 0) -> None:
        self.ägare = ägare          # Ägare
        self.nr = regnummer         # Registreringsnummer
        self.modell = fabrikat      # Fabrikat
        self.år = årsmodell         # Årsmodell
        self.tvikt = tjänstevikt    # Tjänstevikt
        self.meff = motoreffekt     # Motoreffekt

class Person:
    def __init__(self) -> None:
        self.förnamn = ''

b1 = Bil(Person(), 'ABC12A', 'Toyota', 'GR86', 1270, 170)
b2 = Bil(Person(), 'NFA126', 'Volvo', 'V50', 1560, 184)

b1.ägare.förnamn = 'Olivia'
b2.ägare.förnamn = 'Caisa'

def skrivbil(bil):
    print(f'--- Bil ägd av: {bil.ägare.förnamn} ---\nReg nr: {bil.nr}\nFabrikat: {bil.modell}\nÅrsmodell: {bil.år}\nTjänstevikt: {bil.tvikt} kg\nMotoreffekt: {bil.meff} kW\n')

skrivbil(b1)
skrivbil(b2)
class Auto():
    def __init__(self, name, motor, kilometer):
        self.name = name
        self.motor = motor
        self.kilometerzahl = kilometer

    def fahren(self, km):
        if self.restreichweite >= km:
            self.kilometerzahl += km
            self.restreichweite -= km
            print(f"Auto fährt {km}km.")
        else: 
            print("Reichweite nicht mehr ausreichend!")

# ------ Erbende Klasse: Verbrenner
# Über super().__init__(<args>) kann der Konstruktor der Superklasse aufgerufen werden
class Verbrenner(Auto):
    def __init__(self, name, kilometer):
        super().__init__(name, "Verbrenner", kilometer)
        self.tankstand = 100

    def tanken(self, km):
        self.tankstand += km
        print("Vollgetankt mit Brennstoff")

# ----- Erbende Klasse: E_Auto
class E_Auto(Auto):
    def __init__(self, name, kilometer):
        super().__init__(name, "Elektro", kilometer)
        self.akkuladung = 100
    
    def tanken(self, km):
        self.tankstand += km
        print("Vollgetankt mit Ökostrom")

my_e_car = E_Auto("Tesla Model X", 22210)
my_combustion_car = Verbrenner("BMW m3", 13000)

print(my_e_car.motor)
print(my_combustion_car.motor)
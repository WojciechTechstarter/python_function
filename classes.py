

class auto():
    def __init__(name, motor, reichweite, kilometer):
        self.name = name
        self.motor = motor
        self.restreichweite = reichweite
        self.kilometerzahl = kilometer




    def fahren(self, km):
        if self.restreichweite >= km:
            self.kilometerzahl += km
            self.restreichweite -= km
        else:
            print(f'Reichweite nicht mehr ausreichend!')


    def tanken(self, km):
        self.restreichweite += km
        
  
my_car = auto('Cintroen Xsara Picasso', 'Verbrenner', 200, 0)
my_car.fahren(30)
my_car.fahren(100)
my_car.fahren(100)

print(my_car.restreichweite)

my_car.tanken(200)

print(my_car.restreichweite)
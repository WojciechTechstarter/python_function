# Definiere eine Funktion namens "square_root", die eine Zahl annimmt und sie hoch zwei zurückgibt
# Funktionsdefinition
def square_root(zahl):
    return pow(zahl, 0.5)

# Funktion ohne Argumente:
def square_root_no_argument():
    zahl = user_input
    return pow(zahl, 0.5)

# Funktion mit 2 Argumenten:
def add(zahl1, zahl2):
    return zahl1 + zahl2

# Funktionsaufruf:
user_input = float(input("Gib mir eine Zahl: "))
result = square_root(user_input)
print(result)
print(square_root_no_argument())


add(5, 7)
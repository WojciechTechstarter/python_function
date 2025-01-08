# 1. Klammern nochmal erklären
## Listen werden immer mit [] initialisiert
name_list = ["Christof", "Mete", "Joshua", "Nassima", "Sebastian"]
# Element in einer Liste können über Indizes abgerufen werden
# In der Liste oben gibt es index 0 --> "Christof" name_list[0]
# index 1 --> "Mete"
# index 2 --> "Joshua"
print(f"Das erste Element ist: {name_list[0]}")
print(f"Das zweite Element ist: {name_list[1]}")
print(f"Das dritte Element ist: {name_list[2]}")
print(f"Das 4. Element ist: {name_list[3]}")
print(f"Das 5. Element ist: {name_list[-1]}")
print(f"Die geamte Liste sieht so aus: {name_list}")
for i in range(len(name_list)):
    print(f"Das {i}. Element ist aus dem Loop: {name_list[i]}")
for n in name_list:
    print(f"Element ist aus neuen dem For-Loop ist: {n}")

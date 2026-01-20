# I asked ChatGpt to give me some exercises but they were still too hard at the time so I needed lots of help.
# Originally made around New Year 2025 after 2 weeks with Python.

# Übung 1: Grid-Check
# Stell dir ein 5×5-Feld vor (Koordinaten x=0–4, y=0–4)
# Deine Figur startet bei (0,0)
# Schreibe eine Funktion move_to(x, y), die nur druckt, in welche Richtung du gehen würdest, bis du bei (x, y) bist
# Benutze Schleifen & if/elif/else

x = y = 0 
def move(direction): # A little confusing but manageable 
    global x, y
    if direction == "North":
        y += 1
    elif direction == "East":
        x += 1
    elif direction == "South":
        y -= 1
    elif direction == "West":
        x -= 1
    print(f"Move {direction} ({x}, {y})")


# Übung 2: Ernte-Check
# Du hast Felder mit Wasserstand: [0.1, 0.3, 0.5, 0.2, 0.8]
# Schreibe eine Schleife, die alle Felder durchgeht
# Wenn Wasser < 0.25 → „Gieße Feld“ drucken
# Sonst → „Feld ist ok“ drucken

field_water = [0.1, 0.3, 0.5, 0.2, 0.8] # First version
def use_water():
    for i in range(len(field_water)):
        if field_water[i] < 0.25:
            print(f"Feld {i} muss gegossen werden.")
        else:
            print(f"Feld {i} ist okay.")

field_water_2 = [ # Second version just to have tried it once but way too hard
    [0.1, 0.0, 0.8],
    [0.2, 0.6, 0.3]
]
def use_water_2():
    for y in range(len(field_water_2)):
        for x in range(len(field_water_2[y])):
            if field_water_2[y][x] < 0.25:
                print(f"Feld ({x}, {y}) muss gegossen werden.")
            else:
                print(f"Feld ({x}, {y}) ist okay.")


# Übung 3: Pflanzen nach Position
# Felder haben x,y Koordinaten: (0,0),(0,1),(1,0),(1,1)
# Schreibe eine Funktion plant(x,y), die entscheidet:
# x+y gerade → „Pflanze Baum“
# x+y ungerade → „Pflanze Karotte“
# Benutze if/else

def plant(x, y): # The easiest by far
    if (x + y) % 2:
        print(f"Baum auf ({x}, {y}) gepflanzt")
    else:
        print(f"Karotte auf ({x}, {y}) gepflanzt")


# Übung 4 (Bonus, optional): Einfache Sortier-Idee
# Liste von Zahlen: [5, 2, 8, 1]
# Schreibe eine Schleife, die die kleinste Zahl nach vorne bringt (du musst nicht alles sortieren)
# Ziel: Übung fürs Vergleichen & Tauschen

liste = [5, 2, 8, 1]
def find_smallest():
    global liste
    smallest = liste[0]
    for number in liste:
        if number < smallest:
            smallest = number
        print(f"Kleinste Zahl: {smallest}")

def sort_list(): # Way too hard
    global liste
    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    print(f"Sortierte Liste: {liste}")

# Exercises by my professor from the respository iubh/DLBDSIPWP01_D


# Berechne den Body Mass Index (BMI) aus den vorgegebenen Variablen und gebe diesen als Ganzzahl mit einer Erklärung aus,
# die den Vornamen der Person enthält. Der BMI kann berechnet werden, indem das Gewicht durch die quadrierte Größe 
# geteilt wird.
age = 41
height = 1.85
weight = 78
name = "Müller, Peter"
vorname = name.split(",") [1].strip()

def bmi():
    """Rechnet den BMI aus"""
    bmi = weight / (height * height)
    bmi = int(bmi)
    print(f"{vorname}'s BMI ist {bmi}!")
bmi()


# Es geht um die Verwaltung der Studierenden im Python-Kurs: Speichere die (aktuell zwei unten gegebenen) 
# Studierenden mit ihren Matrikelnummern, ihren Studiengängen und den aktuellen Semestern in einer Variablen. 
# Wähle dazu geeignete Datentypen. Zeige beispielhaft auch den Zugriff auf den Studiengang der ersten Person.
92901145, Applied AI, 1. Semester
69343291, Cyber Security, 2. Semester
students = [
    {"Matrikelnummer": "92901145", "Studiengang": "Applied AI", "Semester": "1. Semester"},
    {"Matrikelnummer": "69343291", "Studiengang": "Cyber Security", "Semester": "2. Semester"}
]
students[0]["Studiengang"]


def concat(vorname = "Vorname", nachname = "Nachname"):
    return vorname + " " + nachname, len(vorname), len(nachname)
result = concat("Peter", "Müller")
print(result)
print(concat("Peter"))
print(concat(nachname = "Müller"))

def calc_bmi(weight, height):
    return weight / height**2


# Debugging
def calc_bmi(weight, height):
    return weight / height**2

filename = input("Bitte geben Sie einen Dateinamen ein: ")
file = open(filename,"r")

for line in file
    line = line.strip()
    items = line.split(" ")
    bmi = calc_bmi(float(items[2]), float(items[3]))
    print(items[1], "hat einen BMI von ungefähr:", int(bmi))
file.close()


# Lies die Datei Lektion_6_Daten.csv in einen DataFrame ein. Die Datei enthält x- und y-Werte mit f(x)=y (d.h. y enthält die Funktionswerte für x)
# Gib die ersten fünf Zeilen des DataFrame aus. Gib dann die ersten zehn Zeilen aus.
# Extrahiere die x- und y-Werte aus dem DataFrame. Dazu kann die Funktion loc verwendet werden.
# Interpoliere die Daten mit einer geeigneten Schrittweite.
# Plotte die eingelesenen und interpolierten Daten.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_cvs("daten.csv")

print(df.head()) # first 5
print(df.head(10)) # first 10

x = df.loc[:, "x"]
y = df.loc[:, "y"]

x_interp = np.linespace(x.min(), x.max(), 200)
y_interp = np.linespace(x_interp, x, y)

plt.plot(x, y, "o", label="Originaldaten")
plt.plot(x_interp, y_interp, "-", label="Interpoliert")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()



# Exercises by my professor from the respository iubh/DLBDSIPWP01_D

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



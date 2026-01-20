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

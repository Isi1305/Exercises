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

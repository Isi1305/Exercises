# Using a name to do useless code
def reverse_name(name):
    return name [::-1]
def shout_name(name):
    return name.upper() + "!!!"
def count_letters(name):
    return "-".join(name) + " hat " + str(len(name)) + " Buchstaben!"

# Couldn't decide what to eat so I let it decide random
import random
def what_to_eat():
    options = ["Gazpacho", "Bowl", "Schafskäse", "Minestrone"]
    return random.choice(options)

# Celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    print("Es ist " + str(celsius) + ".")
    return (celsius + 9 / 5) + 32

# Simple check how strong a password is by lenght
def check_password_strenght(password):
    if len(password) >= 8:
        return "Strong!"
    else:
        return "Weak!"

# Number guessing game
import random
def guess_the_number():
    secret = random.randint(1, 10)
    while True:
        guess = int(input("Rate eine Zahl (1-10): "))
        if guess < secret:
            print("Zu niedrig!")
        elif guess > secret:
            print("Zu hoch!")
        else:
            return "RICHTIG!"

# Opening a file, writing in it and closing it
def safe_write_to_file(filename, content):
    try: 
        with open(filename, "w") as file:
            file.write(content)
            file.close()
            return "Erfolgreich gespeichert!"
    except FileNotFoundError:
        return "Stop that"

# Opening a file, reading in it and closing it
def safe_read_from_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "No."
    except:
        "Not working."

# This tells you how old you'll be in 5 years
name = input("Dein Name: ")
age = input("Dein Alter: ")
print(name + " ist " + str(int(age) + 5) + " Jahre alt in 5 Jahren")

# It's missing a lot but gave it a try
def simple_bot():
    name = input("Wie heißt du?")
    print(f"Bot: Hallo {name}! Schön dich kennenzulernen!")
    while True:
        user_input = input("Du: ")
        if user_input == "Hallo":
            print("Bot: Hi! Wie geht's?")
        elif user_input == "Wie geht's?":
            print("Bot: Mir geht es super! Und dir?")
        elif user_input == "Byebye":
            print("Bot: Bye, bis bald!")
            break
        else:
            print("Bot: Das verstehe ich nicht...")


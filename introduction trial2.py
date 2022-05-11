# Introduction trial V1
# This component will get the users name and age
# It will also ask if they have played the quiz before


def get_name():
    name = str(input("What is your name: "))
    return name


def get_age():
    age = int(input("How old are you: "))
    return age


# Main routine
name = get_name()
age = get_age()
print(f"Kia ora {name}. Welcome to Mamae Roro.\n"
      f"Since you are {age} years old you will probably find this easy")

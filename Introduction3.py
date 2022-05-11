# Introduction V2
# This component will be an improvement of Introduction V1


def get_name():  # This function will get the players name
    name = str(input("What is your name: "))
    return name


def get_age():  # This function will get the players age
    age = int(input("How old are you (1-100): "))
    if 1 <= age <= 100:
        return age
    else:
        print("Please enter a valid age")
        return get_age()


def formatter(symbol, text):  # This will border the introduction
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"




# Main routine
name = get_name()
age = get_age()
print(formatter("-", f"Kia ora {name}. Welcome to Mamae Roro.\n"
      f"Since you are {age} years old you will probably find this easy"))



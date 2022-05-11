#This is the final version of the Assement

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


def yes_no(question_text):
    while True:

        # Ask the user if they have played the game before
         answer = input(question_text).lower()
        # If they say yes, output 'Program continues'
         if answer == "yes" or answer == "y":
            answer = "Yes"
            break

        # If no, output 'display instructions'
         elif answer == "no" or answer == "n":
            answer = "No"
            print()
            print(formatter("-","This is the Mamae Roro quiz.\n"
                  "You will have to answer 10 questions about Te Reo Maori.\n"
                  "Please try to avoid decimals and/or answers that are not words."))
            print()
            break

        # else show 'error'
         else:
            print("Invalid answer. Please enter yes/no")




# Main routine
name = get_name()
age = get_age()
print(formatter("-", f"Kia ora {name}. Welcome to Mamae Roro.\n"
      f"Since you are {age} years old you will probably find this easy"))

yes_no("Have you played this quiz before: ")
input("Are you ready to begin: ")






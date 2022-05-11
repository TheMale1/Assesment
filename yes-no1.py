# Simplifies the input by converting it to lower case. Also accepts y or n as  abbreviations.
# Prints result of user choice as well as input - for testing


show_instructions = ""
while show_instructions != "x":
     # Ask the user if they have played the game before
     show_instructions = input("Have you played this quiz before (yes/no): ").lower()
     # If they say yes, output 'Program continues'
     if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

     # If no, output 'display instructions'
     elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

     # else show 'error'
     else:
         print("Invalid answer. Please enter yes/no")

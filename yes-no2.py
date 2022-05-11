# Functions go here
def yes_no(question_text):
    while True:

        # Ask the user if they have played the game before
         answer = input(question_text).lower()
        # If they say yes, output 'Program continues'
         if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If no, output 'display instructions'
         elif answer == "no" or answer == "n":
            answer = "No"
            print()
            print("----------------------------------------")
            print("This is the Mamae Roro quiz.\n"
                  "You will have to answer 10 questions about Te Reo Maori.\n"
                  "Please try to avoid decimals and/or answers that are not words.")
            print("----------------------------------------")
            print()

        # else show 'error'
         else:
            print("Invalid answer. Please enter yes/no")


# Main routine goes here
show_instructions = yes_no("Have you played this game before: ")
print(f"You entered '{show_instructions}' ")









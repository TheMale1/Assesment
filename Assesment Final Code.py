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


def questions():

    score = 0
    answer = input("Are you ready to play: ")
    if answer.lower() == "yes":
        answer = input("Question 1: How do you say hello to one person \n"
                           "a. Kia ora \n"
                           "b. tena koe \n"
                           "c. Tena kotou \n")


        while answer.lower() != "c":
            print("Wrong answer")
            answer = input("Question 1: How do you say hello to one person? \n"
                           "a. Kia ora \n"
                           "b. tena koe \n"
                           "c. Tena kotou \n")

        else:
            score += 1
            print("Correct")

        answer = input("Question 2: How do you say water in Te Reo? \n"
                       "a. wai \n"
                       "b. tokena \n"
                       "c. rima \n")
        while answer.lower() != "a":
            print("Wrong answer")
            answer = input("Question 2: How do you say water in Te Reo? \n"
                       "a. wai \n"
                       "b. tokena \n"
                       "c. rima \n")




        else:
            score += 1
            print("Correct")


        answer = input("Question 3: How do say 7 in Te Reo? \n"
                       "a. tena kotou \n"
                       "b. ono \n"
                       "c. whitu \n")
        while answer.lower() != "c":
            print("Wrong answer")
            answer = input("Question 3: How do say 7 in Te Reo? \n"
                       "a. tena kotou \n"
                       "b. ono \n"
                       "c. whitu \n")

        else:
            score += 1
            print("Correct")


        answer = input("Question 4: How do say hello to everyone in Te Reo? \n"
                       "a. tena kotou \n"
                       "b. kia ora kotou \n"
                       "c. tena koe \n")
        while answer.lower() != "b":
            print("Wrong answer")
            answer = input("Question 4: How do say hello to everyone in Te Reo? \n"
                       "a. tena kotou \n"
                       "b. kia ora kotou \n"
                       "c. tena koe \n")


        else:
            score += 1
            print("Correct")


        answer = input("Question 5: What does 'Ki te pehea a koe' mean?' \n"
                       "a. How are you \n"
                       "b. Where are you \n"
                       "c. What are you \n")
        while answer.lower() != "a":
            print("Wrong answer")
            answer = input("Question 5: What does 'Ki te pehea a koe' mean?' \n"
                       "a. How are you \n"
                       "b. Where are you \n"
                       "c. What are you \n")


        else:
            score += 1
            print("Correct")


        answer = input("Question 6: How do you say 4 in Te Reo? \n"
                       "a. waru \n"
                       "b. Wha \n"
                       "c. tahi \n")
        while answer.lower() != "b":
            print("Wrong answer")
            answer = input("Question 6: How do you say 4 in Te Reo? \n"
                       "a. waru \n"
                       "b. Wha \n"
                       "c. tahi \n")


        else:
            score += 1
            print("Correct")


        answer = input("Question 7: What are maori boats called? \n"
                       "a. Waka \n"
                       "b. Wiri \n"
                       "c. Rima \n")
        while answer.lower() != "a":
            print("Wrong answer")
            answer = input("Question 7: What are maori boats called? \n"
                       "a. Waka \n"
                       "b. Wiri \n"
                       "c. Rima \n")


        else:
            score += 1
            print("Correct")


        answer = input("Question 8: Did the Maori have tribes, or where they united? \n"
                       "a. Tribes \n"
                       "b. United people \n ")
        while answer.lower() != "a":
            print("Wrong answer")
            answer = input("Question 8: Did the Maori have tribes, or where they united? \n"
                       "a. Tribes \n"
                       "b. United people \n ")


        else:
            score += 1
            print("Correct")


        answer = input("Question 9: What is Wednesday in Te Reo? \n"
                       "a. Ratu \n"
                       "b. Rahina \n"
                       "c. Raapa \n")
        while answer.lower() != "c":
            print("Wrong answer")
            answer = input("Question 9: What is Wednesday in Te Reo? \n"
                       "a. Ratu \n"
                       "b. Rahina \n"
                       "c. Raapa \n")


        else:
            score += 1
            print("Correct")


            answer = input("Question 10: How do you say 'Luke is cool' in Te Reo? \n"
                           "a. He pai a Luke \n")
            while answer.lower() != "a":
                print("Wrong answer")
                answer = input("Question 10: How do you say 'Luke is cool' in Te Reo? \n"
                           "a. He pai a Luke \n")


            else:
                score += 1
                print("Correct")

# Main routine
name = get_name()
age = get_age()
print(formatter("-", f"Kia ora {name}. Welcome to Mamae Roro.\n"
      f"Since you are {age} years old you will probably find this easy"))

yes_no("Have you played this quiz before: ")
questions() == input("Are you ready to begin: ")







# This is the second version of the Questions component

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
questions() == input("Are you ready to play: ")

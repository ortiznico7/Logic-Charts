# generated responses depending on the answer
def quizquestions(question, answer):
    test = False
    while test is False:
        result = input(question + ":")
        if result == answer:
            print("Correct! You may proceed.")
            test = True

        else:
            
            test == False
            
            print("Incorrect. Try again.")


correct=0

# questions to help user in the case of struggle

questionBank = ["Do you struggle with Algebra 1 skills?", "Do you struggle with Geometry skills?", "Do you struggle with Algebra 2 skills?", "Do you struggle with PreCalculus skills?", "Do you struggle with Calculus skills?",  "Do you struggle with Trigonometry skills?"]
for question in questionBank:

    test = False

    while test is False:

        userInput = input(question + ":")
       

        if userInput.lower() == "yes":

            test = True

            print("Looks like you need help. We will have this factor present in your study plan.")

        elif userInput.lower() == "no":

            test = True
            print("You may proceed.")    
        
        else:

            test = False
            print("Enter a valid input")

questionBank = ["What is the square root of 576?", "If 55 = 6x + 7, what is the value of x?", "What is the zero of the following function: (x+7)?"]
answerBank = ["36", "8", "-7"]

for index in range(len(questionBank)):
    quizquestions(questionBank[index], answerBank[index])

# for question in questionBank:

#     test = False

#     while test is False:

#         userInput = input(question + ":")

#         if userInput.lower() == "36":

#             test = True

#             print("Correct! You may proceed.")
#             correct+=1

#         else:

#             test = False

#             print("Incorrect. Try again.")
# questionBank = ["If 55 = 6x + 7, what is the value of x?"]
# for question in questionBank:

#     test = False

#     while test is False:

#         userInput = input(question + ":")

#         if userInput.lower() == "8":

#             test = True

#             print("Correct! You may proceed.")
#             correct+=1

#         else:

#             test = False
            
#             print("Incorrect. Try again.")
# questionBank = ["What is the zero of the following function: (x + 7)?"]
# for question in questionBank:

#     test = False

#     while test is False:

#         userInput = input(question + ":")

#         if userInput.lower() == "-7":

#             test = True

#             print("Correct! You may proceed.")
#             correct+=1

#         else:

#             test = False
            
#             print("Incorrect. Try again.")


proceedNOW = False

# asks whether the user is interested in continuing the quiz or not

while  proceedNOW is False:
        userInput = input( "Would you like to proceed with this mini-quiz?" )

        if userInput.lower() == "no":
        
            proceedNOW = True

            # answer if user doesn't want to continue

            print ("Thank you for your responses! We will have your study plan ready in a day or two.")

        elif userInput.lower() == "yes":

            proceedNOW = True

            # answer if user does want to continue

            print("You will be redirected to continue soon. Please wait patiently for the link.")
        else:

            proceedNow = False
            print("Enter a valid input")

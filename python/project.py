# ALG1 = input( "Do you struggle with Algebra 1 skills? " )
# if ALG1 == "Yes":
#     print("Looks like you need help with ALGEBRA 1 skills.")
#     print("We will add this to your study plan. You may proceed.")
# elif ALG1 == "No"
#     print("You may continue to the next question.")
# else:
#     print("Please type again, you may have typed something incorrectly.")
# GEO = input( "Do you struggle with Geometry skills? " )
# if GEO == "Yes":
#     print("Looks like you need help with GEOMETRY skills.")
#     print("We will add this to your study plan. You may proceed.")
# else:
#     print("You may continue to the next question.")
# ALG2 = input( "Do you struggle with Algebra 2 skills? " )
# if ALG2 == "Yes":
#     print("Looks like you need help with ALGEBRA 2 skills.")
#     print("We will add this to your study plan. You may proceed.")
# elif ALG2 == "No":
#     print("You may continue to the next question.")
# else:
#     print("Please type again, you may have typed something incorrectly.")
# PCALC = input( "Do you struggle with Pre-Calculus skills? ")
# if PCALC == "Yes":
#     print("Looks like you need help with PRECALCULUS skills.")
#     print("We will add this to your study plan. You may proceed.")
# else:
#     print("You may continue to the next question.")
# CALC = input ( "Do you struggle with Calculus skills? " )
# if CALC == "Yes":
#     print("Looks like you need help with CALCULUS skills.")
#     print("We will add this to your study plan. You may proceed.")
# else:
#     print("You may continue to the next question.")
# TRIG = input ( "Do you struggle with Trigonometry skills? ")
# if TRIG == "Yes":
#     print("Looks like you need help with TRIGONOMETRY skills.")
#     print("We will add this to your study plan. You may proceed.")
# else:
#     print("You may continue to the next question.")
# COLLG = input ( "Have you ever taken any college level Math courses? " )
# if COLLG == "Yes":
#     print("Great! You may continue to the next question.")
# else:
#     print("You may continue to the next question. This topic might come up later.")
# STUDY = input ( "Is math one of the school topics you study most? " )
# if STUDY == "Yes":
#     print("Great! You may continue to the next question.")
# else:
#     print("You may continue to the next question. This topic might come up later.")
# REGBASIS = input ( "Do you study math on a regular basis? " )
# if REGBASIS == "Yes":
#     print("Great! You may continue to the next question.")
# else:
#     print("You may continue to the next question. This topic might come up later.")


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
questionBank = ["What is the square root of 576?"]
for question in questionBank:

    test = False

    while test is False:

        userInput = input(question + ":")

        if userInput.lower() == "36":

            test = True

            print("Correct! You may proceed.")

        else:

            test = False

            print("Incorrect. Try again.")
questionBank = ["If 55 = 6x + 7, what is the value of x?"]
for question in questionBank:

    test = False

    while test is False:

        userInput = input(question + ":")

        if userInput.lower() == "8":

            test = True

            print("Correct! You may proceed.")

        else:

            test = False
            
            print("Incorrect. Try again.")
questionBank = ["What is the zero of the following function: (x + 7)?"]
for question in questionBank:

    test = False

    while test is False:

        userInput = input(question + ":")

        if userInput.lower() == "-7":

            test = True

            print("Correct! You may proceed.")

        else:

            test = False
            
            print("Incorrect. Try again.")


proceedNOW = False

while  proceedNOW is False:
        userInput = input( "Would you like to proceed with this mini-quiz?" )

        if userInput.lower() == "no":
        
            proceedNOW = True

            print ("Thank you for your responses! We will have your study plan ready in a day or two.")

        elif userInput.lower() == "yes":

            proceedNOW = True

            print("You will be redirected to continue soon. Please wait patiently for the link.")
        else:

            proceedNow = False
            print("Enter a valid input")






        


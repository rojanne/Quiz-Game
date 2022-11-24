import time

#rules of the game
print("\nWelcome to Quiz Game:\n\nB A C K to B A S I C S !!!")
time.sleep(2)
print("\nThis is a game about Code Foundations: Data Types and Expressions")
time.sleep(2)
print("\nThere are 10 questions.\nYou have two attempts to guess the correct answer each question.\nBut if you get the correct answer on your 2nd attempt, you will only get half a point.")
time.sleep(3)
print("\nAfter 10 questions, your score will be tallied. The passing rate is a score of 6.5 and above.\nBest of luck!")
time.sleep(3)
print("\nRemember: Wrong spelling is wrong answer!!!")
time.sleep(4)
score = 0
question_no = 0 

play = input("\nAre you ready to play? yes or no: ") 
play = play.lower()
time.sleep(2)

if play == "yes":
    print("Lets start!")
    time.sleep(2)

    #question #1
    question_no += 1   
    question = input(f"\n{question_no}.What do you call the operation to join two or more strings end-to-end?\nyour answer: ").lower()
    if question == "concatenation":
        score += 1
        print(f"\nCorrect! You got {score} point.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower()
        if question == "concatenation":
            score += 0.5
            print(f"\nCorrect! You got {score} point.")
        else:
            print("Sorry, wrong answer. The answer is concatenation.")

    #question #2
    question_no += 1
    time.sleep(2)
    question = input(f"\n{question_no}.What function is used to check if a string has a certain substring? This method returns the index of the first occurrence of the given value.\nyour answer: ").lower()
    if question == "find":
        score += 1
        print(f"\nCorrect! You got {score} points.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower
        if question == "find":
            score += 0.5
            print(f"\nCorrect! You got {score} points.")
        else:
            print("Sorry, wrong answer. The answer is find.")
    
    #question #3
    question_no += 1
    time.sleep(2)
    question = input(f"\n{question_no}.What function in Python is used to load a library module into a program's memory?\nyour answer: ").lower()
    if question == "import":
        score += 1
        print(f"\nCorrect! You got {score} points.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower()
        if question == "import":
            score += 0.5
            print(f"\nCorrect! You got {score} points.")
        else:
            print("Sorry, wrong answer. The answer is import.")
    
    #question #4
    question_no += 1
    time.sleep(2)
    question = input(f"\n{question_no}.What does this operator % means? It starts with letter 'm'.\nyour answer: ").lower()
    if question == "modulus":
        score += 1
        print(f"\nCorrect! You got {score} points.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower()
        if question == "modulus":
            score += 0.5
            print(f"\nCorrect! You got {score} points.")
        else:
            print("Sorry, wrong answer. The answer is modulus.")

    #question #5
    question_no += 1
    time.sleep(2)
    question = input(f"\n{question_no}.What type conversion in Python automatically converts one data type to another data type and does not need user involvement?\nyour answer: ").lower()
    if question == "implicit":
        score += 1
        print(f"\nCorrect! You got {score} points.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower()
        if question == "implicit":
            score += 0.5
            print(f"\nCorrect! You got {score} points.")
        else:
            print("Sorry, wrong answer. The answer is implicit.")

    #question #6
    question_no += 1
    time.sleep(2)
    question = input(f"\n{question_no}.A floating point number is accurate up to how many decimal places?\nyour answer: ").lower()
    if question == "15":
        score += 1
        print(f"\nCorrect! You got {score} points.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower()
        if question == "15":
            score += 0.5
            print(f"\nCorrect! You got {score} points.")
        else:
            print("Sorry, wrong answer. The answer is 15.")    

    #question #7
    question_no += 1
    time.sleep(2)
    question = input(f"\n{question_no}.What is a collection of script modules accessible to a program to simplify the programming process and removing the need to rewrite commonly used commands?\nyour answer: ").lower()
    if question == "library":
        score += 1
        print(f"\nCorrect! You got {score} points.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower()
        if question == "library":
            score += 0.5
            print(f"\nCorrect! You got {score} points.")
        else:
            print("Sorry, wrong answer. The answer is library.")

    #question #8
    question_no += 1
    time.sleep(2)
    question = input(f"\n{question_no}.What function in Python returns the number of times a specified value occurs in a string?\nyour answer: ").lower()
    if question == "count":
        score += 1
        print(f"\nCorrect! You got {score} points.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower()
        if question == "count":
            score += 0.5
            print(f"\nCorrect! You got {score} points.")
        else:
            print("Sorry, wrong answer. The answer is count.")        

    #question #9
    question_no += 1
    time.sleep(2)
    question = input(f"\n{question_no}.What does this operator ** means?\nyour answer: ").lower()
    if question == "exponent":
        score += 1
        print(f"\nCorrect! You got {score} points.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower()
        if question == "exponent":
            score += 0.5
            print(f"\nCorrect! You got {score} points.")
        else:
            print("Sorry, wrong answer. The answer is exponent.")  

    #question #10
    question_no += 1
    time.sleep(2)
    question = input(f"\n{question_no}.This is an ordered sequence of items same as list but the only difference is it is immutable. What is it?\nyour answer: ").lower()
    if question == "tuple":
        score += 1
        print(f"\nCorrect! You got {score} points.")
    else:
        question = input("Sorry, wrong answer.Try again:\nyour answer: ").lower()
        if question == "tuple":
            score += 0.5
            print(f"\nCorrect! You got {score} points.")
        else:
            print("Sorry, wrong answer. The answer is tuple.")  

    time.sleep(4)
    #score evaluation
    if score > 6:
        print(f"\nCongratulations on finishing the quiz!\n\nYou pass the quiz with a total score of {score}. You are an excellent and brilliant player!")
        time.sleep(2)
        print(f"\n\nThank you for taking the quiz!\nWe will be back with more!")

    else:
        print(f"\nCongratulations on finishing the quiz.\n\nYou got a total score of {score} points.\nSadly, you did not pass the quiz.\nStudy more and take the quiz again.")
        time.sleep(2)
        print(f"\n\nThank you for taking the quiz!\nWe will be back with more!")

else: #if does not want to play
    print(f"\nCome again if you want to play!")



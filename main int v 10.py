# Caleb Blackburn
# This program will be a quiz game
# works cited
# https://stackoverflow.com/questions/37826322/get-a-specific-input-in-python
# History.com for the history and general facts
print("Heyo and welcome to Caleb Blackburn's Quiz game extraordinaire!")
print("Choose your category! math, history, games, sciences")
#this allows the user to exit the code
print("If you want to quit enter bye")
# the def functions lets me create my own functions to assign
def categories():
    while_function_true=True
    for while_function_true in range(True):
        category=input("Type your catagory here as written above: ")
        print("Follow all instructions as given for your answer to count!")
        print("Type answers as written for multiple choice questions")
        print("do not use capital letters")
        history_category="history"
        math_category="math"
        sciences_category = "sciences"
        games_category = "games"
     #for category in range(len(category_list)):
        # The "if" allows me to specify a certain result to occur for a
        # specific input
        if category=="history":
            # this piece of code lets me call out this function
            history_questions()
        elif category=="math":
            math_questions()
        elif category=="games":
            games_questions()
        elif category=="sciences":
            sciences_questions()
        elif category=="bye":
            category=False
        else:
            print("You seem to have misspelled a category please try again")
def history_questions():
    function_history_true=True
    while function_history_true:
        print("Welcome to the history cateogry!")
        user_answer=input("where is Rome located? ")
        correct_answer="italy"
        if not(user_answer==correct_answer):
            print("wrong answer please try again")
        if user_answer==correct_answer:
            score=0
            score+=1
            print("your score is now", score)
            history_question_0(score, user_answer, correct_answer)
def history_question_0(score, user_answer, correct_answer):
    while user_answer==correct_answer:
        print("good","job", sep=' :) ')
        user_answer=input("now when did the American civil war end? ")
        correct_answer="1868"
        if user_answer!=correct_answer:
            print("wrong answer please try again")
        if user_answer==correct_answer:
            score+=1
            print("your score is now", score)
            history_question_1(score, user_answer, correct_answer)
def history_question_1(score, user_answer, correct_answer):
    while user_answer==correct_answer:
        # the end= ' ' links my two print statements to the same line
        print("alright you know your stuff", end=' ')
        print("now who crossed the Alps? ")
        print("this is a multiple choice question")
        user_answer=input("hannibal, the_huns, napoleon, or jeff" )
        correct_answer=("hannibal napoleon")
        if user_answer != correct_answer:
            print("wrong answer please try again")
        if (user_answer==correct_answer)and(not(0)):
            score+=1
            print("your score is now", score)
            history_question_2(score, user_answer, correct_answer)
def history_question_2(score, user_answer, correct_answer):
    while user_answer==correct_answer:
        print("to be written")
# I use the majority of the numerical operators in the math section of my quiz
def math_questions():
    function_math_true = True
    while function_math_true:
        print("Welcome to everyone's favorite category math!")
        user_answer=input("what is 99/55? ")
        correct_answer="1.8"
        if user_answer!=correct_answer:
            print("wrong answer please try again")
        if user_answer == correct_answer:
            score=0
            score+= 1
            print("your score is now", score)
            math_question_0(score, user_answer,correct_answer)
def math_question_0(score, user_answer,correct_answer):
    while user_answer==correct_answer:
        print("nice job with that calculator")
        print("** means exponet in python")
        user_answer=input("now what is 5**3 - 40 ")
        correct_answer="85"
        if user_answer!=correct_answer:
            print("wrong answer please try again")
        if user_answer==correct_answer:
            score+=1
            print("your score is now", score)
            math_question_1(score, user_answer,correct_answer)
def math_question_1(score, user_answer, correct_answer):
    while correct_answer == user_answer:
        print("you really know how to use that calculator now do", end=' ')
        user_answer = input(" 1**2/2 + 55 - 80 * ln(1) ")
        correct_answer = "0"
        if user_answer != correct_answer:
            print("wrong answer please try again")
        if user_answer == correct_answer:
            score += 1
            print("your score is now", score)
            math_question_2(score, user_answer, correct_answer)
def math_question_2(score, user_answer, correct_answer):
    while user_answer == correct_answer:
        print("% means to find the remainder", end=' ')
        print(" // means to divide and only use the remainder")
        user_answer = input("whats 5%8-20//9 ")
        correct_answer = "3"
        if user_answer != correct_answer:
            print("wrong answer please try again")
        if user_answer == correct_answer:
            score += 1
            print("your score is now", score)
            math_question_3(score, user_answer, correct_answer)
def math_question_3(score, user_answer,correct_answer):
    while user_answer==correct_answer:
        print("nice job you have almost finished the math section!")
        print("answer should be one of the following true, false")
        print("find if the equation is true for both x=-2 and x=4")
        user_answer=input("18-30x+1/2(90)-x>=(20+30)/(1.95(20.6))-5x+10x")
        correct_answer="false"
        if (user_answer!=correct_answer)or(not(user_answer==correct_answer)):
            print("wrong answer please try again")
        if user_answer==correct_answer:
            score+=1
            print("your score is now", score)
            math_question_4(score, user_answer,correct_answer)
def math_question_4(score, user_answer, correct_answer):
    while user_answer==correct_answer:
        print("to be written")
def games_questions():
    function_games_true = True
    while function_games_true:
        print("Welcome to the games cateogry!")
        print("When was the first video game made?")
        user_answer=input("1900, 1958, 1990, 2000: ")
        correct_answer="1958"
        if user_answer!=correct_answer:
            print("wrong answer please try again")
        if user_answer == correct_answer:
            score=0
            score+=1
            print("your score is now", score)
            games_question_0(score, user_answer, correct_answer)
def games_question_0(score, user_answer, correct_answer):
    while user_answer==correct_answer :
        print("nice job ", end=' ')
        user_answer=input("now who held the first olympics and where: ")
        correct_answer=("greece athens")
        if user_answer!=correct_answer:
            print("wrong answer please try again")
        if user_answer==correct_answer:
            score+=1
            print("your score is now", score)
            games_question_1(score, user_answer, correct_answer)
def games_question_1(score, user_answer, correct_answer):
    while user_answer==correct_answer :
        # The * allows clap to be printed 5 times
        print("clap "*5,"well done")
        user_answer=input("to be written ")
def sciences_questions():
    function_sciences_true = True
    while function_sciences_true:
        print("Welcome to the sciences cateogry!")
        print("What layer of Earth is its center?")
        user_answer=input("core, inner core, mantle, or the centorium: ")
        correct_answer="inner core"
        if user_answer!=correct_answer:
            print("wrong answer please try again")
        if user_answer == correct_answer:
            score=0
            score += 1
            print("your score is now", score)
            sciences_question_0(score, user_answer, correct_answer)
def sciences_question_0(score, user_answer, correct_answer):
    while user_answer==correct_answer:
        print("alright nice one!"+" tell me", end=' ')
        print("what does malleable mean?")
        user_answer=input("its immovable, its easy to shape, that it melts: ")
        correct_answer="its easy to shape"
        if user_answer!=correct_answer:
            print("wrong answer please try again")
        if user_answer==correct_answer:
            score+=1
            print("your score is now", score)
            sciences_question_1(score, user_answer, correct_answer)
def sciences_question_1(score, user_answer, correct_answer):
    while user_answer==correct_answer :
        print("your doing great!", end=' ')
        print(" What animal actively hunts humans?")
        user_answer=input(" lion, polar bear, hyena, great white: ")
        correct_answer=("polar bear"or"Polar Bear")
        if user_answer!=correct_answer:
            print("wrong answer please try again")
        if user_answer==correct_answer:
            score+=1
            print("your score is now", score)
            sciences_question_2(score, user_answer, correct_answer)
def sciences_question_2(score, user_answer, correct_answer):
    while user_answer==correct_answer :
        print("to be written ")
categories()
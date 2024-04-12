from random import randint

rules = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 2
MAX_NUMBER = 100


# Description of the logic of the game:
def gcd(a, b):
    while a != 0 and b != 0:
        a, b = min(a, b), max(a, b)
        b = b % a
    return a + b


# The function returns the question and the correct answer
def get_question_and_answer():
    random_number1 = randint(MIN_NUMBER, MAX_NUMBER)
    random_number2 = randint(MIN_NUMBER, MAX_NUMBER)

    #Calculating the correct answer:
    corect_answer = gcd(random_number1, random_number2)
    if random_number1 == random_number2:
        corect_answer = random_number1
    elif corect_answer == 0:
        corect_answer = 1

    question = str(random_number1) + " " + str(random_number2)
    return question, str(corect_answer)

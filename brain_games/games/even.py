from random import randint

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


# Description of the logic of the game
# The function returns the question and the correct answer
def get_question_and_answer():
    min_number = 1
    max_number = 100
    random_number = randint(min_number, max_number)

    # Calculating the correct answer:
    if is_even(random_number):
        corect_answer = 'yes'
    else:
        corect_answer = 'no'

    question = random_number
    return question, corect_answer


# Checking for parity:
def is_even(random_number):
    return random_number % 2 == 0

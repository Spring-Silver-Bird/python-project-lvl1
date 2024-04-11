from random import randint
from math import sqrt

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Description of the logic of the game
# The function returns the question and the correct answer
def get_question_and_answer():
    min_number = 2  # Минимальное рандомное число
    max_number = 100  # Максимальное рандомное число
    random_number = randint(min_number, max_number)

    if is_prime(random_number):
        corect_answer = 'yes'
    else:
        corect_answer = 'no'

    question = random_number
    return question, corect_answer


# Checking for parity
def is_prime(random_number):
    flag = True
    max_num_for_check = int(sqrt(random_number))
    for i in range(2, max_num_for_check):
        if random_number % i == 0:
            flag = False
    return flag

from random import randint, choice

rules = 'What is the result of the expression?'


# Description of the logic of the game
# The function returns the question and the correct answer
def get_question_and_answer():
    min_number = 1
    max_number = 10
    random_number1 = randint(min_number, max_number)
    random_number2 = randint(min_number, max_number)
    operator = ["+", "-", "*"]
    random_operator = choice(operator)

    # Calculating the correct answer:
    if random_operator == "+":
        corect_answer = random_number1 + random_number2
    elif random_operator == "-":
        corect_answer = random_number1 - random_number2
    else:
        corect_answer = random_number1 * random_number2

    question = [str(random_number1), str(random_operator), str(random_number2)]
    return ' '.join(question), str(corect_answer)

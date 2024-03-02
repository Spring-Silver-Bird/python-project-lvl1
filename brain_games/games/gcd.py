from random import randint

rules = 'Find the greatest common divisor of given numbers.'
LIFES = 3


# Описание логики игры
# Функция вычисляющая НОД:
def gcd(a, b):
    corect_answer = 0
    for i in range(2, max(random_number1, random_number2)):
        if random_number1 % i == 0 and random_number2 % i == 0:
            corect_answer = i
    return correct_answer
    
# Функция возвращает вопрос и правильный ответ
def game():
    min_number = 2  # Минимальное рандомное число
    max_number = 100  # Максимальное рандомное число
    random_number1 = randint(min_number, max_number)
    random_number2 = randint(min_number, max_number)

    # Вычисляем правильный ответ:
    correct_answer = gsd(random_number1, random_number2)
    if random_number1 == random_number2:
        corect_answer = random_number1
    elif corect_answer == 0:
        corect_answer = 1

    question = str(random_number1) + " " + str(random_number2)
    return question, str(corect_answer)

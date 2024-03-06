from random import randint

rules = 'Find the greatest common divisor of given numbers.'
LIFES = 3
MIN_NUMBER = 2  # Минимальное рандомное число
MAX_NUMBER = 100  # Максимальное рандомное число


# Описание логики игры
# Функция вычисляющая НОД:
def gcd(a, b):
    corect_answer = 0
    for i in range(2, max(a, b)):
        if a % i == 0 and b % i == 0:
            corect_answer = i
    return corect_answer


# Функция возвращает вопрос и правильный ответ
def game():
    random_number1 = randint(MIN_NUMBER, MAX_NUMBER)
    random_number2 = randint(MIN_NUMBER, MAX_NUMBER)

    # Вычисляем правильный ответ:
    corect_answer = gcd(random_number1, random_number2)
    if random_number1 == random_number2:
        corect_answer = random_number1
    elif corect_answer == 0:
        corect_answer = 1

    question = str(random_number1) + " " + str(random_number2)
    return question, str(corect_answer)

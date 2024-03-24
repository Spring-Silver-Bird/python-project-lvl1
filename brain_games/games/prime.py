from random import randint

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'

# Описание логики игры
# Функция возвращает вопрос и правильный ответ


def game():
    min_number = 2  # Минимальное рандомное число
    max_number = 100  # Максимальное рандомное число
    random_number = randint(min_number, max_number)

    if is_prime(random_number):
        corect_answer = 'yes'
    else:
        corect_answer = 'no'

    question = random_number
    return question, corect_answer


# Проверка на четность
def is_prime(random_number):
    flag = True
    for i in range(2, random_number):
        if random_number % i == 0:
            flag = False
    return flag

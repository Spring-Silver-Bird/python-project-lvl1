from random import randint, choice

rules = 'What is the result of the expression?'
LIFES = 3


# Описание логики игры
# Функция возвращает вопрос и правильный ответ
def game():
    min_number = 1  # Минимальное рандомное число
    max_number = 10  # Максимальное рандомное число
    random_number1 = randint(min_number, max_number)
    random_number2 = randint(min_number, max_number)
    operator = ["+", "-", "*"]  # Перечень операторов
    random_operator = choice(operator)  # Выбираем рандомный оператор

    # Вычисляем правильный ответ:
    if random_operator == "+":
        corect_answer = random_number1 + random_number2
    elif random_operator == "-":
        corect_answer = random_number1 - random_number2
    else:
        corect_answer = random_number1 * random_number2

    question = [str(random_number1), str(random_operator), str(random_number2)]
    return ' '.join(question), str(corect_answer)

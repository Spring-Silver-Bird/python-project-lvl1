from random import randint

rules = 'What number is missing in the progression?'
LIFES = 3


# Описание логики игры
# Функция возвращает вопрос и правильный ответ
def game():
    min_number = 0  # Минимальное рандомное число
    max_number = 100  # Максимальное рандомное число
    first_number = randint(min_number, max_number)  # Первое число последовательности
    step = randint(min_number, max_number)  # Шаг последовательности
    progression_lenth = 10  # Длина выводимой прогрессии
    progression = [str(first_number + i * step) for i in range(progression_lenth)]  # Прогрессия
    random_member = randint(0, progression_lenth)  # Выбираем рандомный член прогресии

    # Вычисляем правильный ответ:
    corect_answer = progression[random_member]
    # Вычисляем правильный ответ:
    progression[random_member] = '..'

    question = ' '.join(progression)
    return question, str(corect_answer)

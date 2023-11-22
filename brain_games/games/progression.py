from random import randint

rules = 'What number is missing in the progression?'
LIFES = 3


# Описание логики игры
# Функция возвращает вопрос и правильный ответ
def game():
    min_number = 0  # Минимальное рандомное число
    max_number = 100  # Максимальное рандомное число
    # Первое число последовательности
    first_num = randint(min_number, max_number)
    # Шаг последовательности:
    step = randint(min_number, max_number)
    progression_lenth = 10  # Длина выводимой прогрессии
    # Прогрессия:
    progression = [str(first_num + i * step) for i in range(progression_lenth)]
    # Выбираем рандомный член прогресии:
    random_member = randint(0, progression_lenth - 1)
    # Вычисляем правильный ответ:
    corect_answer = progression[random_member]
    # Вычисляем правильный ответ:
    progression[random_member] = '..'

    question = ' '.join(progression)
    return question, str(corect_answer)

from random import randint

rules = 'What number is missing in the progression?'
MIN_COUNT = 5  # Минимальная длина выводимой прогрессии
MAX_COUNT = 10  # Максимальная длина выводимой прогрессии
MIN_NUMBER = 1  # Минимальное рандомное число
MAX_NUMBER = 100  # Максимальное рандомное число
MIN_STEP = 2  # Минимальный шаг последовательности
MAX_STEP = 25  # Максимальный шаг последовательности


# Описание логики игры
# Вычисляем прогрессию:
def make_progression(size, first_num, step):
    """
    Make arithmetic progression.
    """
    return [str(first_num + i * step) for i in range(size)]


def progression_question(prog, member):
    prog[member] = '..'
    return ' '.join(prog)


# Функция возвращает вопрос и правильный ответ
def game():
    # Размер последовательности:
    size = randint(MIN_COUNT, MAX_COUNT)
    # Первый член последовательности:
    first_element = randint(MIN_NUMBER, MAX_NUMBER)
    # Шаг последовательности:
    step = randint(MIN_STEP, MAX_STEP)
    # Прогрессия:
    progression = make_progression(size, first_element, step)
    # Выбираем рандомный член прогресии:
    random_member = randint(0, size - 1)
    # Вычисляем правильный ответ:
    corect_answer = progression[random_member]
    # Формируем вопрос:
    question = progression_question(progression, random_member)
    return question, corect_answer

from random import randint

rules = 'What number is missing in the progression?'
LIFES = 3
MIN_COUNT = 5 # Минимальная длина выводимой прогрессии
MAX_COUNT = 10 # Максимальная длина выводимой прогрессии
MIN_NUMBER = 1 # Минимальное рандомное число
MAX_NUMBER = 100 # Максимальное рандомное число
MIN_STEP = 2 # Минимальный шаг последовательности
MAX_STEP = 25 # Максимальный шаг последовательности
 

# Описание логики игры
# Вычисляем прогрессию:
def make_progression(size, first_num, step):
    progression = [first_num + i * step for i in range(size)]
    return progression

# Функция возвращает вопрос и правильный ответ
def game():
    # Размер последовательности:
    size = randint(MIN_COUNT, MAX_COUNT)
    # Первый член последовательности:
    first_num = randint(MIN_NUMBER, MAX_NUMBER)
    # Шаг последовательности:
    step = randint(MIN_STEP, MAX_STEP)
    # Прогрессия:
    progression = progression(size, first_num, step)
    # Выбираем рандомный член прогресии:
    random_member = randint(size)
    # Вычисляем правильный ответ:
    corect_answer = progression[random_member]
    # Вычисляем правильный ответ:
    progression[random_member] = '..'

    question = ' '.join(progression)
    return question, str(corect_answer)

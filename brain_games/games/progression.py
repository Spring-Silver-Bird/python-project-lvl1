from random import randint

rules = 'What number is missing in the progression?'
MIN_COUNT = 5
MAX_COUNT = 5
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_STEP = 2
MAX_STEP = 25


# Description of the logic of the game
def make_progression(size, initial, difference):
    """
    Make arithmetic progression.
    """
    return [initial + i * difference for i in range(size)]


def make_progression_question(prog, index_hidden_element):
    prog[index_hidden_element] = '..'
    return ' '.join([str(member) for member in prog])


def make_game_data():
    size = randint(MIN_COUNT, MAX_COUNT)
    initial = randint(MIN_NUMBER, MAX_NUMBER)
    difference = randint(MIN_STEP, MAX_STEP)
    progression = make_progression(size, initial, difference)
    index_find_member = randint(0, size - 1)
    corect_answer = str(progression[index_find_member])
    question = make_progression_question(progression, index_find_member)
    return question, corect_answer

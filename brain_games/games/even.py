from random import randint
import prompt

rules = 'Answer "yes" if the number is even, otherwise answer "no".'
LIFES = 3




#Описание логики игры
#Функция возвращает вопрос и правильный ответ
def game():
    min_number = 1 #Минимальное рандомное число
    max_number = 100 #Максимальное рандомное число
    random_number = randint(min_number, max_number)
    #print('Question:', random_number)
    #user_answer = prompt.string('Your answer: ')

    if is_even(random_number):
        corect_answer = 'yes'
    else:
        corect_answer = 'no'

    question = random_number
    return question, corect_answer

#Проверка на четность
def is_even(random_number):
    return random_number % 2 == 0

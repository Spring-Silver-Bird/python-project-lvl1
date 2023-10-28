from random import randint, choice
import prompt

rules = 'Find the greatest common divisor of given numbers.'
LIFES = 3


#Описание логики игры
#Функция возвращает вопрос и правильный ответ
def game():
    min_number = 2 #Минимальное рандомное число
    max_number = 100 #Максимальное рандомное число
    random_number1 = randint(min_number, max_number)
    random_number2 = randint(min_number, max_number)
    operator = ["+", "-", "*"] #Перечень операторов
    random_operator = choice(operator) #Выбираем рандомный оператор

    
    #Вычисляем правильный ответ:
    corect_answer = 0
    for i in range(2, max(random_number1, random_number2)):
        if random_number1 % i == 0 and random_number2 % i == 0:
            corect_answer = i
    if corect_answer == 0:
        corect_answer = 1
        


    question = str(random_number1) + " " + str(random_number2)
    return question, str(corect_answer)





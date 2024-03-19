import prompt


# Приветствуем пользователя в игре и запрашиваем его имя
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

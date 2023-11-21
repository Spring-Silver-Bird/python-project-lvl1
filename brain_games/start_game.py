import prompt

# Начало игры, принимаем правила и название игры


def start_game(rules, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    LIFES = 3
    win = True
    print(rules)

    while LIFES > 0:
        question, correct_answer = game()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'. \nLet's try again, {name}!")
            win = False
            break

        LIFES -= 1

    if win:
        print(f'Congratulations, {name}!')

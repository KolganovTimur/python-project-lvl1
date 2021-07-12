import prompt
from brain_games.cli import welcome_user


def base(game):
    name = welcome_user()
    print(name)
    print(game.description)
    total_steps = 3
    count = 0
    while count < total_steps:
        question, correct_answer = game.generating_question_and_answer()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            count += 1
            print('Correct!')
        else:
            print('\'{}\' is wrong answer ;(. '.format(answer), end='')
            print('Correct answer is \'{}\'.'.format(correct_answer))
            print('Let\'s try again, {}!'.format(name))
            return
    print('Congratulations, {}!'.format(name))

import prompt
from brain_games.cli import greeting


def base(description, generate):
    name = greeting()
    print(description)
    count = 0
    while count < 3:
        question, correct_answer = generate()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print('\'{}\' is wrong answer ;(. '.format(answer), end='')
            print('Correct answer is \'{}\'.'.format(correct_answer))
            print('Let\'s try again, {}!'.format(name))
            return
        count = count + 1
    print('Congratulations, {}!'.format(name))

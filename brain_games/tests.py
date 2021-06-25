import prompt
from random import randint as rand


def test_1():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = rand(0, 50)
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        if answer == correct_answer:
            print('Correct!')
        else:
            print('\'{}\' is wrong answer ;(. '.format(answer), end='')
            print('Correct answer is \'{}\'.'.format(correct_answer))
            print('Let\'s try again, {}!'.format(name))
            return
        count += 1
    print('Congratulations, {}!'.format(name))

import random
import prompt


def nod(a, b):
    while b > 0:
        a, b = b, a % b
    return str(a)


def start():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    for count in range(3):
        a = random.randint(0, 50)
        b = random.randint(0, 50)
        print('Question: {} {}'.format(a, b))
        answer = prompt.string('Your answer: ')
        correct_answer = nod(a, b)
        print(correct_answer)
        if answer == correct_answer:
            print('Correct!')
        else:
            print('\'{}\' is wrong answer ;(. '.format(answer), end='')
            print('Correct answer is \'{}\'.'.format(correct_answer))
            print('Let\'s try again, {}!'.format(name))
            return
    print('Congratulations, {}!'.format(name))

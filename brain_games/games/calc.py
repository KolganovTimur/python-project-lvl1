import random

import prompt
from random import randint as rand


def start():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    for count in range(3):
        num1 = random.randint(0, 50)
        num2 = random.randint(0, 50)
        operator = random.choice('+-*')
        print('Question: {} {} {}'.format(num1, operator, num2))
        answer = prompt.string('Your answer: ')
        correct_answer = ''
        if operator == '+':
            correct_answer = str(num1 + num2)
        elif operator == '-':
            correct_answer = str(num1 - num2)
        elif operator == '*':
            correct_answer = str(num1 * num2)
        if answer == correct_answer:
            print('Correct!')
        else:
            print('\'{}\' is wrong answer ;(. '.format(answer), end='')
            print('Correct answer is \'{}\'.'.format(correct_answer))
            print('Let\'s try again, {}!'.format(name))
            return
    print('Congratulations, {}!'.format(name))

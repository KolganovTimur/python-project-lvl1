import random
import prompt


def is_prime(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
        i += 1
    return True


def start():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for count in range(3):
        num = random.randint(1, 1000)
        print('Question: {}'.format(num))
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_prime(num) else 'no'
        if answer == correct_answer:
            print('Correct!')
        else:
            print('\'{}\' is wrong answer ;(. '.format(answer), end='')
            print('Correct answer is \'{}\'.'.format(correct_answer))
            print('Let\'s try again, {}!'.format(name))
            return
    print('Congratulations, {}!'.format(name))

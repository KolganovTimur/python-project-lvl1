import random
import prompt


def start():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')
    for count in range(3):
        num = random.randint(0, 15)
        k = random.randint(2, 6)
        length = 10
        index = random.randint(1, length - 1)
        correct_answer = ''
        print('Question: {} '.format(num), end='')
        for x in range(length):
            num += k
            if x == index:
                correct_answer = str(num)
                print('.. ', end='')
            else:
                print('{} '.format(num), end='')
        answer = prompt.string('\nYour answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print('\'{}\' is wrong answer ;(. '.format(answer), end='')
            print('Correct answer is \'{}\'.'.format(correct_answer))
            print('Let\'s try again, {}!'.format(name))
            return
    print('Congratulations, {}!'.format(name))

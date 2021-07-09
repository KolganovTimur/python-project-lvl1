from random import randint as rand
from brain_games.engine.engine import base


def generating_question_and_answer():
    num = rand(0, 20)
    step = rand(2, 9)
    len = 10
    index = rand(0, len - 1)
    question = ''
    correct_answer = ''
    for x in range(len):
        if x == index:
            correct_answer = '{}'.format(num)
            question += '.. '
        else:
            question += '{} '.format(num)
        num += step
    return question, correct_answer


def start():
    description = 'What number is missing in the progression?'
    base(description, generating_question_and_answer)

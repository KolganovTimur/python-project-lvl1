from random import randint as rand
from brain_games.engine.engine import base


def nod(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def generating_question_and_answer():
    num1 = rand(0, 50)
    num2 = rand(0, 50)
    question = 'Question: {} {}'.format(num1, num2)
    correct_answer = str(nod(num1, num2))
    return question, correct_answer


def start():
    description = 'Find the greatest common divisor of given numbers.'
    base(description, generating_question_and_answer)

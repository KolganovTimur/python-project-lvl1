from random import randint as rand
from brain_games.engine.engine import base


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def generating_question_and_answer():
    number = rand(0, 50)
    question = 'Question: {}'.format(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


def start():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    base(description, generating_question_and_answer)

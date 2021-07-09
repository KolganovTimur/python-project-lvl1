from random import randint as rand
from random import choice
from brain_games.engine.engine import base


def operation(num1, num2, operator):
    if operator == '+':
        return str(num1 + num2)
    if operator == '-':
        return str(num1 - num2)
    if operator == '*':
        return str(num1 * num2)


def generating_question_and_answer():
    num1 = rand(0, 50)
    num2 = rand(0, 50)
    operator = choice('+-*')
    question = 'Question: {} {} {}'.format(num1, operator, num2)
    correct_answer = operation(num1, num2, operator)
    return question, correct_answer


def start():
    description = 'What is the result of the expression?'
    base(description, generating_question_and_answer)

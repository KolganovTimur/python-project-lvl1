from random import randint as rand


def is_prime(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


def generating_question_and_answer():
    num = rand(0, 100)
    question = 'Question: {}'.format(num)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer


description = 'Answer "yes" if given number is prime. Otherwise answer "no"'

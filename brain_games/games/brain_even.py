#!/usr/bin/env python3.10
from random import randint
from prompt import string


def main():
    print("Welcome to the Brain Games!")
    name = string('May I have your name? ')
    print(f'Hello, {name}\nAnswer "yes" if the number is even, otherwise answer "no".')

    counter = 0

    while counter != 3:
        randoms_value = randint(0, 1000)

        print(f'Question: {randoms_value}')
        user_answer = string('Your answer: ')

        if (randoms_value % 2 == 0 and user_answer == 'yes' or
                randoms_value % 2 != 0 and user_answer == 'no'):
            counter += 1
            print('Correct!')

        else:
            mirror_answer = 'yes' if randoms_value % 2 == 0 else 'no'

            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{mirror_answer}'. "
                  f"\nLet's try again, {name}")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

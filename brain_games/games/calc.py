from random import randint, choice
import operator
import enginy


def calc_game():
    enginy.welcome_us()
    print('What is the result of the expression?')

    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    action_key = list(action.keys())
    counter = 0

    while counter != 3:
        random_operation = choice(action_key)
        first_value = randint(10, 20)
        second_value = randint(1, 10)

        enginy.question(f'{first_value} {random_operation} {second_value}')
        answer = enginy.user_answer()

        correct_answer = f'{action[random_operation](first_value, second_value)}'
        if answer == correct_answer:
            counter += 1
            print('Correct!')
        else:
            enginy.goodbye_user(answer, correct_answer)
            break

    enginy.congratulations(counter)

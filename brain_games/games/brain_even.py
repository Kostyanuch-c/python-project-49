from random import randint
import enginy


def even_game():
    enginy.welcome_us()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0

    while counter != 3:
        randoms_value = randint(0, 1000)

        enginy.question(randoms_value)
        answer = enginy.user_answer()

        if (randoms_value % 2 == 0 and answer == 'yes' or
                randoms_value % 2 != 0 and answer == 'no'):
            counter += 1
            print('Correct!')

        else:
            correct_answer = 'yes' if randoms_value % 2 == 0 else 'no'

            enginy.goodbye_user(answer, correct_answer)
            break

    enginy.congratulations(counter)




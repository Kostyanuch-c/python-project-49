from prompt import string

user_name = ''


def welcome_us():
    global user_name
    user_name = string('May I have your name? ')
    print(f"Hello, {user_name}")


def user_answer():
    return string('Your answer: ')


def question(problem):
    print(f'Question: {problem}')


def congratulations(counter):
    if counter == 3:
        print(f'Congratulations, {user_name}!')


def goodbye_user(answer, correct_answer):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. "
          f"\nLet's try again, {user_name}")

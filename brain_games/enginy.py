from prompt import string

NUMBER_OF_ROUNDS = 3


def welcome_user(question):
    user_name = string('May I have your name? ')
    print(f"Hello, {user_name}"
          f"\n{question}")
    return user_name


def game_engine(game_module):
    user_name = welcome_user(game_module.QUESTION)
    counter = 0
    while counter < NUMBER_OF_ROUNDS:

        problem, correct_answer = game_module.problem_and_correct_answer()

        print(f'Question: {problem}')
        answer = string('Your answer: ')
        if answer == correct_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')

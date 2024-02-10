from prompt import string

user_name = ''


def welcome_us(question):
    global user_name
    user_name = string('May I have your name? ')
    print(f"Hello, {user_name}"
          f"\n{question}")


def user_answer():
    return string('Your answer: ')


def comparison(logic_game):
    tpl_with_question = logic_game()
    question = tpl_with_question[0]
    welcome_us(question)
    counter = 0
    while counter < 3:

        tpl_with_problem_and_answer = logic_game()
        correct_answer = tpl_with_problem_and_answer[2]
        problem = tpl_with_problem_and_answer[1]

        print(f'Question: {problem}')
        answer = user_answer()
        if answer == correct_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {user_name}!")
            break

    if counter == 3:
        print(f'Congratulations, {user_name}!')

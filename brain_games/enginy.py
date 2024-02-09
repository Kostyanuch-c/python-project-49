from prompt import string

user_name = ''


def welcome_us(question):
    global user_name
    user_name = string('May I have your name? ')
    print(f"Hello, {user_name}"
          f"\n{question}")


def user_answer():
    return string('Your answer: ')


# def comparison(problem_and_answer, counter):
#     correct_answer = problem_and_answer[1]
#     problem = problem_and_answer[0]
#
#     print(f'Question: {problem}')
#     answer = user_answer()
#     if answer == correct_answer:
#         counter += 1
#         print('Correct!')
#     else:
#         counter += 4
#         print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. "
#               f"\nLet's try again, {user_name}!")
#
#     if counter == 3:
#         print(f'Congratulations, {user_name}!')
#     return counter


def comparison(question, problem_and_answer):
    welcome_us(question)
    counter = 0
    while counter < 3:

        tpl_with_result = problem_and_answer()
        correct_answer = tpl_with_result[1]
        problem = tpl_with_result[0]

        print(f'Question: {problem}')
        answer = user_answer()
        if answer == correct_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. "
                  f"\nLet's try again, {user_name}!")
            break

    if counter == 3:
        print(f'Congratulations, {user_name}!')

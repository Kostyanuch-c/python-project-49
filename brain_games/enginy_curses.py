import curses

# from brain_games.statistics.statistic import
NUMBER_OF_ROUNDS = 3


def game_engine(game_module, name_user):
    curses.noqiflush()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(1)
    RED_AND_BLACK = curses.color_pair(2)

    question_win = curses.newwin(
        curses.LINES // 5,
        curses.COLS - 1,
        int(curses.LINES * 0.8),
        1)
    question_win.box()
    question_win.addstr(1, 1, game_module.QUESTION)

    answer_win = curses.newwin(3,
                               curses.COLS - 1,
                               int(curses.LINES * 0.6),
                               1)
    answer_win.box()
    answer_win.addstr(1, 1, "You answer:", )

    answer_win.refresh()
    question_win.refresh()
    for i in range(NUMBER_OF_ROUNDS):

        problem, correct_answer = game_module.problem_and_correct_answer()

        question_win.addstr(2, 1, str(problem))
        question_win.refresh()

        user_answer = answer_win.getstr(1, 13).decode()
        if user_answer == correct_answer:
            if i < NUMBER_OF_ROUNDS - 2:
                question_win.addstr(3, 1, 'Correct! Keep up the good work!',
                                    GREEN_AND_BLACK)
            else:
                question_win.addstr(3, 1, 'Correct! One more!             ',
                                    GREEN_AND_BLACK)
            question_win.move(2, 1)
            question_win.clrtoeol()

        else:
            question_win.bkgd(' ')
            question_win.erase()
            question_win.refresh()

            question_win.addstr(3, 1, f"'{user_answer}' is ")
            question_win.addstr(*question_win.getyx(), "wrong answer ",
                                RED_AND_BLACK)
            question_win.addstr(*question_win.getyx(),
                                f";(. Correct answer was '{correct_answer}'")
            question_win.addstr(4, 1, f"Let's try again, {name_user}"
                                      f"! Or choose another game!")
            question_win.refresh()
            break

        answer_win.addstr(1, 13, f"{' ' * len(user_answer)}")
        answer_win.refresh()
        question_win.refresh()
    else:
        question_win.bkgd(' ')
        question_win.erase()
        question_win.refresh()

        question_win.addstr(4, 1, f'Congratulation '
                                  f'{name_user}! Shall we play again?')
        question_win.refresh()

        return True
    return False

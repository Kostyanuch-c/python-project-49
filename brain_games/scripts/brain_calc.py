#!/usr/bin/env python3.10
from brain_games.games.calc import (welcome_question_calc,
                                    problem_and_correct_answer_calc)
from brain_games.enginy import comparison


def main():
    comparison(welcome_question_calc(), problem_and_correct_answer_calc)


if __name__ == '__main__':
    main()

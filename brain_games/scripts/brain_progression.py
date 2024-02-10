#!/usr/bin/env python3.10
from brain_games.games.progression import (
    welcome_question_progression,
    problem_and_correct_answer_progression
)
from brain_games.enginy import comparison


def main():
    comparison(welcome_question_progression(),
               problem_and_correct_answer_progression)


if __name__ == '__main__':
    main()

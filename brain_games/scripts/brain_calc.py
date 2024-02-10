#!/usr/bin/env python3.10
from brain_games.games.calc import welcome_question, problem_and_correct_answer
import brain_games.enginy


def main():
    brain_games.enginy.comparison(welcome_question(), problem_and_correct_answer)


if __name__ == '__main__':
    main()

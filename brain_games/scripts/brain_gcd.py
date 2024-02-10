#!/usr/bin/env python3.10
from brain_games.games.gcd import (welcome_question_gcd,
                                   problem_and_correct_answer_gcd)
import brain_games.enginy


def main():
    brain_games.enginy.comparison(welcome_question_gcd(),
                                  problem_and_correct_answer_gcd())


if __name__ == '__main__':
    main()

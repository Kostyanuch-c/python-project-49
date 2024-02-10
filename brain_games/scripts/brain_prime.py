#!/usr/bin/env python3.10
from brain_games.games.prime import (welcome_question_prime,
                                     problem_and_correct_answer_prime)
import brain_games.enginy


def main():
    brain_games.enginy.comparison(
        welcome_question_prime(),
        problem_and_correct_answer_prime
    )


if __name__ == '__main__':
    main()

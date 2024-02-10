#!/usr/bin/env python3.10
import brain_games.games.prime
from brain_games.enginy import comparison


def main():
    comparison(brain_games.games.prime.welcome_question(),
               brain_games.games.prime.problem_and_correct_answer)


if __name__ == '__main__':
    main()

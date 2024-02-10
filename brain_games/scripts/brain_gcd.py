#!/usr/bin/env python3.10
import brain_games.games.gcd
from brain_games.enginy import comparison


def main():
    comparison(brain_games.games.gcd.welcome_question(),
               brain_games.games.gcd.problem_and_correct_answer)


if __name__ == '__main__':
    main()

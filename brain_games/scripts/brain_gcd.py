#!/usr/bin/env python3.10
import brain_games.games.gcd
import brain_games.enginy


def main():
    brain_games.enginy.comparison(brain_games.games.gcd.welcome_question(),
                                  brain_games.games.gcd.problem_and_correct_answer)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3.10
import brain_games.games.prime
import brain_games.enginy


def brain_prime():
    brain_games.enginy.comparison(brain_games.games.prime.welcome_question(),
                                  brain_games.games.prime.problem_and_correct_answer)


if __name__ == '__main__':
    brain_prime()

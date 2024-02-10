#!/usr/bin/env python3.10
import brain_games.games.prime
import brain_games.enginy


def main():
    brain_games.enginy.comparison(
        brain_games.games.prime.welcome_question_prime(),
        brain_games.games.prime.problem_and_correct_answer_prime)


if __name__ == '__main__':
    main()

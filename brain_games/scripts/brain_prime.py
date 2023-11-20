#!/usr/bin/env python3

from brain_games.start_game import start_game
from brain_games.games.prime import game, rules


def main():
    brain_games_prime()


def brain_games_prime():
    start_game(rules, game)


if __name__ == '__main__':
    main()

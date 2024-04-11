#!/usr/bin/env python3
from brain_games.engine import play_game
from brain_games.games.gcd import game, rules


def main():
    brain_games_even()


def brain_games_even():
    play_game(rules, game)


if __name__ == '__main__':
    main()

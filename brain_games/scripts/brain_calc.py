#!/usr/bin/env python3
from brain_games.start_game import start_game
from brain_games.games.calc import game, rules

def main():
    brain_games_even()


def brain_games_even():
    start_game(rules, game)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
from brain_games.engine import play_game
from brain_games.games.progression import make_game_data, rules


def main():
    brain_games_even()


def brain_games_even():
    play_game(rules, make_game_data)


if __name__ == '__main__':
    main()

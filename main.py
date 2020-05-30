from random import choice
import time

import dice
from board import Board
from playerturn import PlayerTurn
from messages import Messages
import commons

dices = [dice.Dice(6) for x in range(0, 4)]
msg = Messages()


def main():
    players, game_board = setup()

    while True:

        for player in players:

            player_turn = PlayerTurn(dices, player, game_board)
            commons.clear_terminal()

            while player_turn.has_next_round():
                player_turn.new_round()

            if player_turn.is_player_ending():
                game_board.move_player(player, player_turn.get_turn_choices())

            if game_board.check_winner(player):
                exit()


def setup():
    commons.clear_terminal()
    print_title()
    print(msg.get_message('setup'))
    player_num = get_player_number()
    players = get_player_names(player_num)
    players = sort_player_order(players)
    game_board = Board(players)

    return players, game_board


def print_title():
    print(msg.get_message('title'))


def sort_player_order(players):
    print('\n')
    for i in range(0, 3):
        print(f'{msg.get_message("sort")}{i*".."}')
        time.sleep(1)
    qty_players = len(players)

    random_players = []
    print(msg.get_message('order'))
    for p in range(0, qty_players):
        chosen_player = choice(players)
        random_players.append(chosen_player)
        players.remove(chosen_player)
        print(f'{p+1} - {chosen_player}')

    time.sleep(3)

    return random_players


def get_player_number():
    player_num = ''
    while isinstance(player_num, str):
        try:
            player_num = input(msg.get_message('p_qty'))
            player_num = int(player_num)
            if player_num < 2 or player_num > 4:
                raise 'InvalidNumber'
        except Exception:
            player_num = ''
            print(
                msg.get_message('invalid_num').replace('P_NUM1', '2').replace('P_NUM2', '4')
            )

    return player_num


def get_player_names(player_num):
    players = []
    for player in range(0, player_num):
        next_player = False
        while not next_player:
            player_name = input(msg.get_message('p_name').replace('P_ID', str(player + 1)))
            if player_name in players or len(player_name) < 1:
                print(msg.get_message('invalid_name'))
            else:
                players.append(player_name)
                next_player = True

    return players


if __name__ == '__main__':
    main()

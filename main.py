from random import choice

import dice
from board import Board
from playerturn import PlayerTurn

dices = [dice.Dice(6) for x in range(0,4)]


def main():
    player_num = get_player_number()
    players = get_player_names(player_num)
    players = sort_player_order(players)
    game_board = Board(players)

    while True:

        for player in players:
            print(f'This is {player}\'s turn!')
            player_turn = PlayerTurn(dices, player, game_board)

            while player_turn.has_next_round():
                player_turn.new_round()
            
            if player_turn.is_player_ending():
                game_board.move_player(player, player_turn.get_turn_choices())
            
            if game_board.check_winner(player):
                exit()


def sort_player_order(players):
    print('Sorting player order')
    qty_players = len(players)

    random_players = []
    print('Player order is: ')
    for p in range(0, qty_players):
        chosen_player = choice(players)
        random_players.append(chosen_player)
        players.remove(chosen_player)
        print(f'{p+1} - {chosen_player}')
    
    return random_players


def get_player_number():
    player_num = ''
    while isinstance(player_num, str):
        try:
            player_num = input('How many players? ')
            player_num = int(player_num)
            if player_num < 2 or player_num > 4:
                raise 'InvalidNumber'
        except:
            player_num = ''
            print('Invalid player number. Please enter a valid number between 2 to 4.')

    return player_num


def get_player_names(player_num):
    players = []
    for player in range(0, player_num):
        next_player = False
        while not next_player:
            player_name = input(f'What\'s the name of player {player+1}? ')
            if player_name in players or len(player_name) < 1:
                print('Invalid name. Please enter an unique name.')
            else:
                players.append(player_name)
                next_player = True

    return players


if __name__ == '__main__':
    main()

from itertools import permutations
from random import choice

import dice
import playerturn

dices = [dice.Dice(6) for x in range(0,4)]


def main():
    player_num = get_player_quantity()
    players = get_player_names(player_num)
    players = sort_player_order(players)

    while True:
        for player in players:
            print(f'This is {player}\'s turn!')
            turn = playerturn.PlayerTurn()
            dice_roll = roll_dices()



            show_player_options(get_player_options(dice_roll))

            exit()

    print(players)


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


def get_player_quantity():
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


def roll_dices():
    roll = sorted([dice.roll() for dice in dices])
    print(f'You\'ve rolled {roll}')
    return roll


def get_player_options(rolled_dices):
    unique_dices = len(set(rolled_dices))

    if unique_dices == 4:
        options = [
            [(rolled_dices[0], rolled_dices[1]), (rolled_dices[2], rolled_dices[3])],
            [(rolled_dices[0], rolled_dices[2]), (rolled_dices[1], rolled_dices[3])],
            [(rolled_dices[0], rolled_dices[3]), (rolled_dices[1], rolled_dices[2])],
        ]
    elif unique_dices == 3:
        if rolled_dices[1] == rolled_dices[2]:
            options = [
                [(rolled_dices[0], rolled_dices[1]), (rolled_dices[2], rolled_dices[3])],
                [(rolled_dices[0], rolled_dices[3]), (rolled_dices[1], rolled_dices[2])]
            ]
        else:
            options = [
                [(rolled_dices[0], rolled_dices[1]), (rolled_dices[2], rolled_dices[3])],
                [(rolled_dices[0], rolled_dices[2]), (rolled_dices[1], rolled_dices[3])]
            ]
    elif unique_dices == 1 or unique_dices == 2:
        options = [
            [(rolled_dices[0], rolled_dices[1]), (rolled_dices[2], rolled_dices[3])]
        ]

    return options


def show_player_options(player_options):
    opt_id = 0

    for option in player_options:
        opt_id += 1

        first_move_track = option[0][0] + option[0][1]
        second_move_track = option[1][0] + option[1][1]

        print(f'Option {opt_id}: First Pair: {option[0]}.')
        print(f'          Second Pair: {option[1]}.')
        print()
        
        if first_move_track == second_move_track:
            print(f'          Move 2 spaces on track {first_move_track}')
        else:
            print(f'          Result: Move 1 space on track {first_move_track} and 1 space on track {second_move_track}')
        print('-----')

        


if __name__ == '__main__':
    main()

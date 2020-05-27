import time

class PlayerTurn:
    
    def __init__(self, dices, allowed_moves):
        self._max_qty_tracks = 3
        self._turn_choices = []
        self._allowed_moves = allowed_moves
        self._dices = dices
        self._next_round = True
        self._player_end = False
    

    def new_round(self):
        rolled_dices = self.roll_dices()
        dices_options = self.get_dice_options(rolled_dices)
        dices_options = self.validate_dice_options(dices_options)
        if len(dices_options) == 0:
            self.lose_turn()
            return
        self.show_player_options(dices_options)
        player_choice = int(input('Which option will you choose? '))
        self.choose_dices_pairs(dices_options[player_choice-1])
        player_choice = input('Would you like to continue rolling dices? [y/n] ')
        if player_choice == 'n':
            self._next_round = False
            self._player_end = True
        else:
            self._next_round = True



    def roll_dices(self):
        print(f'Rolling the dices......')
        time.sleep(3)

        roll = sorted([dice.roll() for dice in self._dices])
        print(f'You\'ve rolled {roll}')
        return roll


    def get_dice_options(self, rolled_dices):
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


    def validate_dice_options(self, dice_options):
        valid_dice_options = []

        for dice_option in dice_options:
            if self.is_dice_option_valid(dice_option):
                valid_dice_options.append(dice_option)
        
        return valid_dice_options


    def is_dice_option_valid(self, option):
        temp_allowed_moves = self._allowed_moves
        temp_turn_choices = self._turn_choices

        first_move = option[0][0] + option[0][1]
        second_move = option[1][0] + option[1][1]

        is_first_valid = False
        is_second_valid = False

        is_first_chosen = False
        is_second_chosen = False
        
        for turn_choice in temp_turn_choices:
            if first_move == turn_choice['track'] and not is_first_valid:
                is_first_chosen = True
                if temp_allowed_moves[str(first_move)] > 0:
                    temp_allowed_moves[str(first_move)] -= 1
                    is_first_valid = True  
            if second_move == turn_choice['track'] and not is_second_valid:
                is_second_chosen = True
                if temp_allowed_moves[str(second_move)] > 0:
                    temp_allowed_moves[str(second_move)] -= 1
                    is_second_valid = True
        
        if not is_first_valid and not is_first_chosen:
            if len(self._turn_choices) < self._max_qty_tracks:
                if temp_allowed_moves[str(first_move)] > 0:
                    temp_allowed_moves[str(first_move)] -= 1
                    is_first_valid = True
        
        if is_first_valid and not is_second_valid and not is_second_chosen and first_move == second_move:
            if temp_allowed_moves[str(first_move)] > 0:
                temp_allowed_moves[str(first_move)] -= 1
                is_second_valid = True
        
        if not is_second_valid and not is_second_chosen:
            if len(self._turn_choices) < self._max_qty_tracks:
                if temp_allowed_moves[str(second_move)] > 0:
                    temp_allowed_moves[str(second_move)] -= 1
                    is_second_valid = True
                
        if is_first_valid and is_second_valid:
            return True
        else:
            return False


    def show_player_options(self, player_options):
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


    def choose_dices_pairs(self, dice_option):
        for dice_pair in dice_option:
            track_number = dice_pair[0] + dice_pair[1]
            self.move_chosen_track(track_number)


    def move_chosen_track(self, track_number):
        self._allowed_moves[str(track_number)] -= 1

        for turn_choice in self._turn_choices:
            if track_number == turn_choice['track']:
                turn_choice['movements'] += 1
                return

        self._turn_choices.append({
                'track': track_number,
                'movements': 1
            })


    def lose_turn(self):
        print('You cannot choose any two pairs with this roll! =(')
        print('You\'ve lost your turn!!')
        
        self._turn_choices = []
        self._next_round = False


    def show_turn_choices(self):
        print(self._turn_choices)

    def get_turn_choices(self):
        return self._turn_choices
    
    def has_next_round(self):
        return self._next_round
    
    def is_player_ending(self):
        return self._player_end

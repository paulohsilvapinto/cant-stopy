import time
import copy

from messages import Messages
import commons


class PlayerTurn:
    def __init__(self, dices, player_name, current_board):
        self._max_qty_tracks = 3
        self._turn_choices = []
        self._allowed_moves = current_board.get_player_left_moves(player_name)
        self._player_name = player_name
        self._dices = dices
        self._next_round = True
        self._player_end = False
        self._temp_board = copy.deepcopy(current_board)
        self._msg = Messages()

    def new_round(self):
        commons.clear_terminal()
        print(self._msg.get_message('p_turn').replace('P_NAME', self._player_name))
        time.sleep(1)
        self._temp_board.show_board(self._player_name, self._turn_choices)
        rolled_dices = self.roll_dices()
        dices_options = self.get_dice_options(rolled_dices)
        dices_options = self.validate_dice_options(dices_options)
        if len(dices_options) == 0:
            self.lose_turn()
            return
        self._show_player_options(dices_options)
        self._get_player_dice_choice(dices_options)
        commons.clear_terminal()
        self._temp_board.show_board(self._player_name, self._turn_choices)
        self.show_runners()
        self._get_player_round_decision()

    def show_runners(self):
        print(self._msg.get_message('runners'))
        for runner in self._turn_choices:
            print(
                self._msg.get_message('runners_move').replace('P_TRACK', str(runner['track'])).replace('P_MOVE', str(runner['movements']))
            )

    def _get_player_dice_choice(self, dices_options):
        player_choice = None
        qty_options = len(dices_options)
        while not player_choice:
            try:
                player_choice = int(
                    input(
                        self._msg.get_message('p_option').replace('P_NAME', self._player_name)
                    ))
                if player_choice < 1 or player_choice > qty_options:
                    raise Exception
            except Exception:
                player_choice = None
                if qty_options > 1:
                    print(
                        self._msg.get_message('invalid_num').replace('P_NUM1', '1').replace('P_NUM2', str(qty_options))
                    )
                else:
                    print(self._msg.get_message('invalid_choice'))

        player_choice = player_choice - 1

        if dices_options[player_choice]['valid_choice'] == 'single' and len(
                dices_options[player_choice]['dice_pairs']) == 2:
            player_sub_choice = self._get_player_dice_sub_choice()
            self.choose_dices_pairs([
                dices_options[player_choice]['dice_pairs'][player_sub_choice]
            ])
        else:
            self.choose_dices_pairs(dices_options[player_choice]['dice_pairs'])

    def _get_player_dice_sub_choice(self):
        player_sub_choice = None

        while not player_sub_choice:
            try:
                player_sub_choice = int(
                    input(self._msg.get_message('sub_opt')))
                if player_sub_choice < 1 or player_sub_choice > 2:
                    raise Exception
            except Exception:
                player_sub_choice = None
                print(self._msg.get_message('invalid_num').replace('P_NUM1', '1').replace('P_NUM2', '2'))

        return player_sub_choice - 1

    def _get_player_round_decision(self):
        player_choice = None
        while not player_choice:
            try:
                player_choice = input(
                    self._msg.get_message('continue_round').replace('P_NAME', self._player_name)
                )
                if not player_choice.upper(
                ) == 'N' and not player_choice.upper() == 'Y':
                    raise Exception
            except Exception:
                player_choice = None
                print(self._msg.get_message('invalid_input'))

        if player_choice.upper() == 'N':
            self._next_round = False
            self._player_end = True
        else:
            self._next_round = True

    def roll_dices(self):
        print('\n')
        for i in range(0, 3):
            print(f"{self._msg.get_message('rolling')}{i*'..'}")
            time.sleep(1)

        roll = sorted([dice.roll() for dice in self._dices])
        print(self._msg.get_message('rolled').replace('P_ROLL', str(roll)))
        time.sleep(2)
        return roll

    def get_dice_options(self, rolled_dices):

        options = [
            [(rolled_dices[0], rolled_dices[1]),
             (rolled_dices[2], rolled_dices[3])],
            [(rolled_dices[0], rolled_dices[2]),
             (rolled_dices[1], rolled_dices[3])],
            [(rolled_dices[0], rolled_dices[3]),
             (rolled_dices[1], rolled_dices[2])],
        ]

        max_range = len(options)
        unique_options = []

        for i in range(0, max_range):
            option = options.pop()
            if option not in options:
                unique_options.append(option)

        return unique_options

    def validate_dice_options(self, dice_options):
        valid_dice_options = []

        for dice_pairs in dice_options:
            valid_dice_pair = []
            for dice_pair in dice_pairs:
                if self.is_dice_pair_valid(dice_pair):
                    valid_dice_pair.append(dice_pair)

            if len(valid_dice_pair
                   ) == 2 and self.is_both_dice_pair_simultaneously_valid(
                       valid_dice_pair):
                valid_dice_options.append({
                    'dice_pairs': valid_dice_pair,
                    'valid_choice': 'both'
                })
            elif len(valid_dice_pair) > 0:
                valid_dice_options.append({
                    'dice_pairs': valid_dice_pair,
                    'valid_choice': 'single'
                })

        return valid_dice_options

    def is_dice_pair_valid(self, dice_pair):
        temp_allowed_moves = copy.deepcopy(self._allowed_moves)
        temp_turn_choices = copy.deepcopy(self._turn_choices)

        track_number = dice_pair[0] + dice_pair[1]
        is_track_number_valid = False

        for turn_choice in temp_turn_choices:
            if track_number == turn_choice['track']:
                if temp_allowed_moves[str(track_number)] > 0:
                    is_track_number_valid = True

        if not is_track_number_valid:
            if len(self._turn_choices) < self._max_qty_tracks:
                if temp_allowed_moves[str(track_number)] > 0:
                    is_track_number_valid = True

        return is_track_number_valid

    def is_both_dice_pair_simultaneously_valid(self, dice_option):
        temp_allowed_moves = copy.deepcopy(self._allowed_moves)
        temp_turn_choices = copy.deepcopy(self._turn_choices)

        first_pair = dice_option[0][0] + dice_option[0][1]
        second_pair = dice_option[1][0] + dice_option[1][1]

        first_pair_new = True
        second_pair_new = True

        for turn_choice in temp_turn_choices:
            if turn_choice['track'] == first_pair:
                first_pair_new = False

        if first_pair_new and first_pair == second_pair:
            second_pair_new = False
        else:
            for turn_choice in temp_turn_choices:
                if turn_choice['track'] == second_pair:
                    second_pair_new = False

        if len(temp_turn_choices) + int(first_pair_new) + int(
                second_pair_new) > 3:
            return False

        temp_allowed_moves[str(first_pair)] -= 1
        temp_allowed_moves[str(second_pair)] -= 1

        if temp_allowed_moves[str(first_pair)] < 0 or temp_allowed_moves[str(
                second_pair)] < 0:
            return False

        return True

    def _show_player_options(self, player_options):
        opt_id = 0

        for option in player_options:
            opt_id += 1

            first_dice_pair = option['dice_pairs'][0]
            first_move_track = str(first_dice_pair[0] + first_dice_pair[1])

            print(self._msg.get_message('option_one').replace('P_OPT_ID', str(opt_id)).replace('P_DICES', str(first_dice_pair)))

            if len(option['dice_pairs']) == 2:
                second_dice_pair = option['dice_pairs'][1]
                second_move_track = str(second_dice_pair[0] + second_dice_pair[1])
                print(self._msg.get_message('option_two').replace('P_DICES', str(second_dice_pair)))

            if option['valid_choice'] == 'both':
                if first_move_track == second_move_track:
                    print(
                        self._msg.get_message('same_pair').replace('P_TRACK', first_move_track)
                    )
                else:
                    print(
                        self._msg.get_message('two_pairs').replace('P_TRACK1', first_move_track).replace('P_TRACK2', second_move_track)
                    )
            else:
                if len(option['dice_pairs']) == 2:
                    print(self._msg.get_message('only_one'))
                    print(
                        self._msg.get_message('pair_one').replace('P_TRACK', first_move_track)
                    )
                    print(self._msg.get_message('or'))
                    print(
                        self._msg.get_message('pair_two').replace('P_TRACK', second_move_track)
                    )
                else:
                    print(
                        self._msg.get_message('single_pair').replace('P_TRACK', first_move_track)
                    )

            print(self._msg.get_message('separator'))

    def choose_dices_pairs(self, dice_option):
        for dice_pair in dice_option:
            track_number = dice_pair[0] + dice_pair[1]
            self.move_chosen_track(track_number)

    def move_chosen_track(self, track_number):
        if self._allowed_moves[str(track_number)] == 0:
            return

        self._allowed_moves[str(track_number)] -= 1

        for turn_choice in self._turn_choices:
            if track_number == turn_choice['track']:
                turn_choice['movements'] += 1
                return

        if len(self._turn_choices) < self._max_qty_tracks:
            self._turn_choices.append({'track': track_number, 'movements': 1})

    def lose_turn(self):
        print(self._msg.get_message('stuck'))
        time.sleep(1)
        print(self._msg.get_message('lose_turn'))
        time.sleep(2)

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

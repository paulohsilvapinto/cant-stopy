from messages import Messages
import commons


class Board:
    _msg = Messages()
    _board_limits = [3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3]

    def __init__(self, player_names):
        self._board = {}
        self._board = self._generate_board(player_names)

    def _generate_board(self, player_names):
        board = dict()
        board['tracks'] = dict()
        board['score'] = dict()
        for track in range(2, 12 + 1):
            board['tracks'][str(track)] = dict()
            board['tracks'][str(track)]['players_position'] = dict()
            board['tracks'][str(track)]['max_spaces'] = self._board_limits[
                track - 2]
            board['tracks'][str(track)]['finished'] = False

            for player in player_names:
                board['tracks'][str(track)]['players_position'][player] = 0

        for player in player_names:
            board['score'][player] = 0

        return board

    def move_player(self, player_name, movements):
        for movement in movements:
            track = str(movement['track'])
            moved_spaces = movement['movements']

            self._board['tracks'][track]['players_position'][
                player_name] += moved_spaces
            if self._board['tracks'][track]['players_position'][
                    player_name] == self._board['tracks'][track]['max_spaces']:
                self._board['tracks'][track]['finished'] = True
                if player_name in self._board['score']:
                    self._board['score'][player_name] += 1
                else:
                    self._board['score'][player_name] = 1

    def check_winner(self, player_name):
        if self._board['score'][player_name] == 3:
            commons.clear_terminal()
            self.show_board()
            print(
                self._msg.get_message('winner').replace('P_NAME', player_name)
            )
            return True

        return False

    def get_player_position(self, player_name, track_number):
        track = str(track_number)

        current_position = self._board['tracks'][track]['players_position'][
            player_name]

        return current_position

    def get_player_left_moves(self, player_name):
        left_moves = {}
        for track in self._board['tracks']:
            if self._board['tracks'][track]['finished']:
                left_moves[track] = 0
            else:
                current_position = self._board['tracks'][track][
                    'players_position'][player_name]
                track_limit = self._board['tracks'][track]['max_spaces']

                left_move = track_limit - current_position
                left_moves[track] = left_move
        return left_moves

    def show_board(self, player_name=None, runner_movements=list()):
        self._board

        player_color = [
            self._msg.get_color_cyan(),
            self._msg.get_color_green(),
            self._msg.get_color_lightred(),
            self._msg.get_color_magenta()
        ]

        default_track = self._msg.get_message('default_track')
        empty_track = self._msg.get_message('empty_track')

        for y in range(0, 14):
            board_layer = ''
            for x in range(2, 13):

                players = ''
                str_x = str(x)

                count_players = 0
                for runner_movement in runner_movements:
                    if runner_movement['track'] == x:
                        if runner_movement['movements'] + self._board[
                                'tracks'][str_x]['players_position'][
                                    player_name] == 13 - y:
                            count_players += 1
                            players += self._msg.get_message('runner_symbol')

                color_idx = 0
                for player, player_position in self._board['tracks'][str_x][
                        'players_position'].items():
                    color_idx += 1
                    if player_position == 13 - y:
                        count_players += 1
                        players += player_color[color_idx - 1] + player[0]

                if y < 13:
                    if count_players > 0:
                        track = default_track[0:default_track.rfind('|') - count_players + 1] + players
                    else:
                        track = default_track

                    if (y < -2 * x + 14 and x <= 7) or (x > 7
                                                        and y < 2 * x - 14):
                        board_layer += empty_track
                    else:
                        board_layer += track
                else:
                    if self._board['tracks'][str_x]['finished']:
                        board_layer += default_track.replace('|', '-')
                    else:
                        board_layer += default_track[0:-len(str_x)] + str_x

            print(board_layer)

        subtitle = self._msg.get_message('runner_subtitle')
        color_idx = 0
        for player_name in self._board['score']:
            color_idx += 1
            subtitle += empty_track + player_color[color_idx - 1] + f'{player_name[0]} - {player_name}'

        print(subtitle)

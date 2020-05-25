class Board:

    _board_layout = {
            # track_id: max_space
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 6,
            '9': 5,
            '10': 4,
            '11': 3,
            '12': 2
        }


    def __init__(self, player_names):
        self._board = {}
        for player in player_names:
            self._board[str(player)] = {'qty_tracks_finished': 0}
            for track in range(2, 12+1):
                self._board[str(player)][str(track)] = {
                    'spaces': 0,
                    'finished': False   
                }


    def move_player(self, player_name, movements):
        for movement in movements:
            track = str(movement['track'])
            moved_spaces = movement['movements']

            self._board[player_name][track]['spaces'] += moved_spaces
            if self._board[player_name][track]['spaces'] == self._board_layout[track]:
                self._board[player_name][track]['finished'] = True
                self._board[player_name]['qty_tracks_finished'] += 1


    def check_winner(self, player_name):
        if self._board[player_name]['qty_tracks_finished'] == 3:
            print (f'Congratulations!!! {player_name} has won this match!!')
            return True
        
        return False


    def get_player_position(self, player_name, track_number):
        track = str(track_number)

        current_position = self._board[player_name][track]['spaces']
        left_moves = self._board_layout[track] - current_position

        return current_position, left_moves


    def show_board(self):
        print(self._board)
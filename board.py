class Board:
    _board_limits = [3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3]

    def __init__(self, player_names):
        self._board = {}
        self._board = self._generate_board(player_names)


    def _generate_board(self, player_names):
        board = dict()
        board['tracks'] = dict()
        board['score'] = dict()
        for track in range(2, 12+1):
            board['tracks'][str(track)] = dict()
            board['tracks'][str(track)]['players_position'] = dict()
            board['tracks'][str(track)]['max_spaces'] = self._board_limits[track-2]
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

            self._board['tracks'][track]['players_position'][player_name] += moved_spaces
            if self._board['tracks'][track]['players_position'][player_name] == self._board['tracks'][track]['max_spaces']:
                self._board['tracks'][track]['finished'] = True
                if player_name in self._board['score']:
                    self._board['score'][player_name] += 1
                else:
                    self._board['score'][player_name] = 1


    def check_winner(self, player_name):
        if self._board['score'][player_name] == 3:
            print (f'Congratulations!!! {player_name} has won this match!!')
            return True
        
        return False


    def get_player_position(self, player_name, track_number):
        track = str(track_number)

        current_position = self._board['tracks'][track]['players_position'][player_name]

        return current_position
    

    def get_player_left_moves(self, player_name):
        left_moves = {}
        for track in self._board['tracks']:
            current_position = self._board['tracks'][track]['players_position'][player_name]
            track_limit = self._board['tracks'][track]['max_spaces']

            left_move = track_limit - current_position
            if left_move > 0:
                left_moves[track] = left_move
        return left_moves


    def show_board(self):
        print(self._board)
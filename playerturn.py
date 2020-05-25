class PlayerTurn:
    
    def __init__(self):
        self._max_qty_tracks = 3
        self._turn_choices = []
    
    
    def choose_track(self, track_number):
        for choice in self._turn_choices:
            if track_number == choice['track']:
                choice['movements'] += 1
                return

        if len(self._turn_choices) < self._max_qty_tracks:
            self._turn_choices.append({
                'track': track_number,
                'movements': 1
            })

    def show_tracks(self):
        print(self._turn_choices)


from colorama import init, Fore
from pyfiglet import Figlet


class Messages:
    custom_fig = Figlet(font='banner')
    _msg = {
        'title': Fore.GREEN + custom_fig.renderText("Can't Stopy"),
        'setup': Fore.WHITE + "Let's setup your game!",
        'p_qty': Fore.WHITE + '\nHow many players? ',
        'p_name': Fore.WHITE + "What's the name of player P_ID? ",
        'sort': Fore.BLUE + 'Sorting player order..',
        'order': Fore.YELLOW + '\nPlayer order is: ',
        'p_turn': Fore.YELLOW + "This is P_NAME's turn!\n",
        'invalid_num': Fore.RED + 'Invalid number. Please enter a valid number between P_NUM1 to P_NUM2.',
        'invalid_name': Fore.RED + 'Invalid name. Please enter an unique name.',
        'runners': Fore.YELLOW + '\n\nRight now your runners are:',
        'runners_move': Fore.YELLOW + "    - Track: P_TRACK - Movements: P_MOVE",
        'p_option': Fore.WHITE + '\nP_NAME, which option will you choose? ',
        'invalid_choice': Fore.RED + 'Invalid choice. You have to choose option 1',
        'sub_opt': Fore.WHITE + 'Which sub option will you choose? ',
        'continue_round': Fore.WHITE + '\nP_NAME, would you like to continue rolling the dices? [y/n] ',
        'invalid_input': Fore.RED + 'Invalid input. Please enter y or n',
        'rolling': Fore.BLUE + 'Rolling the dices..',
        'rolled': Fore.YELLOW + "You've rolled P_ROLL !",
        'stuck': Fore.RED + '\n\n\nYou cannot choose any pair with this roll! =(',
        'lose_turn': Fore.RED + "\nYou've lost your turn!!",
        'separator': Fore.WHITE + '-----',
        'or': Fore.BLUE + '          OR',
        'only_one': Fore.BLUE + '          You have to choose only one pair!',
        'option_one': Fore.YELLOW + '\nOption P_OPT_ID: ' + Fore.BLUE + 'First Pair: P_DICES.',
        'option_two': Fore.BLUE + '          Second Pair: P_DICES.\n',
        'same_pair': Fore.YELLOW + '          Move 2 spaces on track P_TRACK',
        'two_pairs': Fore.YELLOW + '          Move 1 space on track P_TRACK1 AND 1 space on track P_TRACK2',
        'pair_one': Fore.YELLOW + '          1 - Move 1 space on track P_TRACK',
        'pair_two': Fore.YELLOW + '          2 - Move 1 space on track P_TRACK',
        'single_pair': Fore.YELLOW + '          Move 1 space on track P_TRACK',
        'winner': Fore.YELLOW + '\n\nCongratulations!!! P_NAME has won this match!!',
        'default_track': Fore.WHITE + '    |',
        'empty_track': Fore.WHITE + '     ',
        'runner_symbol': Fore.LIGHTYELLOW_EX + '@',
        'runner_subtitle': Fore.LIGHTYELLOW_EX + '\n@ - Player Runner'
    }

    def __init__(self):
        init(autoreset=True)

    def get_message(self, message_id):
        return self._msg.get(message_id)

    def get_color_cyan(self):
        return Fore.CYAN

    def get_color_green(self):
        return Fore.GREEN

    def get_color_magenta(self):
        return Fore.MAGENTA

    def get_color_lightred(self):
        return Fore.LIGHTRED_EX

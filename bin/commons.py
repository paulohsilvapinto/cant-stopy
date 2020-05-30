import os
from bin.messages import Messages

msg = Messages()


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_quit(user_input):
    if user_input.upper() in ['QUIT', 'EXIT', 'QUIT()', 'EXIT()']:
        if input(msg.get_message('quit')).upper() == 'N':
            return None
        else:
            exit()
    return user_input

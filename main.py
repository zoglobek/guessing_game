from guess_game.logic import player_input, is_valid
from guess_game.messages import start_message
from guess_game.functions import get_num, is_high, is_low ,is_num


def turn():
    get_num()
    print(start_message)
    while is_valid(player_input()):
        is_high()
        is_low()
        is_num()





if __name__ == "__main__":
    turn()

from guess_game.logic import player_input, is_valid
from guess_game.messages import start_message, try_again
from guess_game.functions import get_num, is_high, is_low ,is_num

mynum = get_num()
player_num = player_input()

def turn(my_num,player_num):
    valid = is_valid(player_num)
    while valid != try_again:
        if is_high(mynum, valid):
            print(is_high(mynum, valid))
            return False
        elif is_low(mynum, valid):
            print(is_low(mynum, valid))
            return False
        elif is_num(mynum, valid):
            print(is_num(mynum, valid))
            return True
        else:
            return False






if __name__ == "__main__":
    print(start_message)

    while True:
        player_num
        if turn(mynum,player_num):
            continue



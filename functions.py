import random
import logic
from guess_game.messages import high_guess, low_guess, win


def get_num():
    my_number = random.randrange(1,100)
    return my_number

def is_high(my_number:int, valid_num:int):
    if my_number > valid_num:
        return high_guess


def is_low(my_number:int, valid_num:int):
    if my_number < valid_num:
        return low_guess


def is_num(my_number:int, valid_num:int):
    if my_number == valid_num:
        return win


if __name__ == "__main__":
    ...

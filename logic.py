from guess_game.messages import try_again


def player_input():
    num = int(input("Please enter a number between 1-100\n"))
    return num


def is_valid(num):
    if isinstance(num, int):
        while  num >= 0 and num <= 100:
            valid_num = num
            return valid_num
        else:
            return try_again
    else:
        return try_again




if __name__ == "__main__":
   print(is_valid(500))
   print(is_valid(50))
   print(is_valid(0))
   print(is_valid(-5))

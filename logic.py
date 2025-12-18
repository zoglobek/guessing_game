from guess_game.messages import try_again


def player_input():
    num = input("Please enter a number between 1-100")
    return num


def is_valid(num):
    if isinstance(num, int):
        if not num < 0 and not num > 100:
            valid_num = num
        return valid_num
    else:
        return try_again




if __name__ == "__main__":
    ...


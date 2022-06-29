from random import shuffle

my_list = ["0", " ", " "]


def shuffle_my_list(my_list):
    shuffle(my_list)
    return my_list


def user_input():
    guess = " "
    while guess not in ["O", "1", "2"]:
        guess = input("insert a 0, 1 or 2 ")
    result = int(guess)
    return result


def check_input(my_list, result):
    if my_list(result) == "O":
        print("Wrong Number")
    else:
        print("Correct!")


# initial list
my_list = ["O", " ", " "]
# shuffle list
mixed_list = shuffle_my_list(my_list)
# request user input
trial = user_input()
# Check guess
# check_input(my_list, )

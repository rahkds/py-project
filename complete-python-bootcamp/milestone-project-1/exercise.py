def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:
        choice = input("Pick a position(0,1,2): ")
        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice! ")

    return int(choice)


def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input("Keep Playing? (Y OR N) ")
        if choice not in ['Y', 'N']:
            print("Sorry, I didn't understand, please choose Y or N ")

    return choice == 'Y'



game_on = True
game_list = [1,2,3]

while game_on:
    display_game(game_list)
    choice = position_choice()
    game_list = replacement_choice(game_list,choice)
    display_game(game_list)
    game_on = gameon_choice()
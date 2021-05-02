"""
The game starts with a pile of 20 stones between the players. 2 players alternate taking stones until there are zero left. The last player to take a stone loses.
"""
def main():
    stones = 20 # initial pile
    i = 1 # variable to keep track of whose turn it is
    while stones != 0:
        print("There are", stones, "stones left")
        if i == 1: # player 1
            amount = int(input("Player " + str(i) + " would you like to remove 1 or 2 stones? "))
            while amount != 1 and amount != 2: # player can  take only 1 or 2 stones
                amount = int(input("Please enter 1 or 2: "))
            print()
            stones -= amount # the number of stones in the pile is reduced by amount taken by player 1
            i = 2 # next turn of player 2
        elif i == 2: # player 2
            amount = int(input("Player " + str(i) + " would you like to remove 1 or 2 stones? "))
            while amount != 1 and amount != 2: # player can  take only 1 or 2 stones
                amount = int(input("Please enter 1 or 2: "))
            print()
            stones -= amount # the number of stones in the pile is reduced by amount taken by player 2
            i = 1 # next turn of player 1
    print("Player", i, "wins!")


if __name__ == '__main__':
    main()
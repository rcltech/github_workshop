def printBoard(data):
    for i, element in enumerate(data['board']):
        print(element, end=" ")
        if i % 3 == 2:
            print()

def checkForNoWinner(data):
    newData = data.copy()
    if newData['moves'] == 9: # all moves exhausted
        newData['end'], newData['winner'] = True, 'None'
        return newData
    return data

# ============= DO NOT CHANGE ANYTHING ABOVE THIS ==============


# You can write additional functions here





# ============= TASK A ==============
def checkForWinner(data):
    # create a newData object by copying data
    newData = data.copy()

    # the conditions for winning the game using row, column or diagonal tiles on the board
    conditions = [
        [0,1,2], [3,4,5], [6,7,8], # row conditions
        [0,3,6], [1,4,7], [2,5,8], # col conditions
        [0,4,8], [2,4,6] # diagonal conditions
    ]

    # use newData instead of data, because you don't want to accidentally change the original data
    # write a for loop to check each condition against the board
    # when winner is found,
            # make newData['winner'] = the winner you have found
            # set newData['end'] to be true
            # return newData
    # if no winner is found, do not return anything
    



    # check for no winner (this has been written for you)
    newData = checkForNoWinner(data)
    return newData


# ============= TASK B ==============


def updateBoard(data, currentTurn, userInput):

    # currentTurn refers to a character which is either 'X' or 'O', update the board using this variable
    # userInput refers to the number that the user entered during this turn

    # figure out a way to update the board


    pass # remove this line when you have completed this function


# ============= DO NOT CHANGE ANYTHING BELOW THIS ==============

def main():
    # a python object to store all data
    # board is the current tic tac toe board
    # moves is the current number of moves elapsed
    # winner is the winner of the game
    data = {'board': [0,1,2,3,4,5,6,7,8],'moves':0, 'end': False, 'winner': None}

    printBoard(data)

    currentTurnList = ('X', 'O')
    while not data['end']:
        i = data['moves']
        print(f'{currentTurnList[i%2]}--> ', end="")
        userInput = int(input())
        data = updateBoard(data, currentTurnList[i%2], userInput)

        printBoard(data)
        data['moves'] += 1
        data = checkForWinner(data)

    print("Winner:", data['winner'])

main()

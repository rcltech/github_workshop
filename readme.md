# Pair Programming Session
#### Suggested time taken: 20-30 mins for amateur programmers

## Program outline
tictactoe.py is a python program that allows 2 users to play the nostalgic game Tic Tac Toe.

Users take turns to input board numbers to update the board.

#### Data structure
```
data = {
  'board': [0,1,2,3,4,5,6,7,8],
  'moves':0,
  'end': False,
  'winner': None
}
```
`data` - a python object to store all data

`board` -  the current tic tac toe board

`moves` - the current number of moves elapsed

`winner` - the winner of the game

## Tasks outline
For this workshop, you and your partner will write 2 different parts of the same program to complete tictactoe.py. One of you will complete one of the tasks. You are not allowed to complete both tasks by yourself, but both of you should work together to solve problems.

The first two pairs of programmers will be given prizes.

### Setting up
#### Task 1A (1 person)
Clone the github repository on our club's organisation.
```
git clone https://github.com/rcltech/github_workshop.git
```
Remove git and re-initalize git
```
cd github_workshop
rm -rf .git
git init
```

Create a new repository on your dashboard

Add new remote link (change `link` to your repo link)
```
git remote add origin link
```

Initial commit and push
```
git add -A
git commit -m 'initial commit'
git push -u origin master
```

#### Task 1B (another person)
Fork the newly created repository

Clone the forked repository
```
git clone link
```


#### Task 2 (together)
Discuss with your partner about the program structure, particularly the delegation of task. Work on solving any difficulties together as well.

#### Task A (1 person)
In the function `checkForWinner`, some winning `conditions` (in a 1D array) have been written for you. Within this function, the `data` object has been copied to `newData`; use `newData` instead of `data`, because you don't want to accidentally change the original `data` object.

To do:
- write a for loop to check each condition in `conditions` against the `board`.
- when a winner is found,
  - make `newData['winner']` = the winner you have found
  - set `newData['end']` to be true
  - return `newData` as soon as a winner is found
- if no winner is found, do not return anything, let the function continue its flow

#### Task B (another person)
The function `updateBoard` is to update the tic tac toe board according to who's turn is it, and which position the user has chosen.

Function input parameters:
- `currentTurn` refers to a character which is either 'X' or 'O', update the board using this variable
- `userInput` refers to the number that the user entered during this turn

To do:
- figure out a way to update the board

## Collaboration
Both of you push your code respectively.
`git push -u origin master`

Person who completed Task 1B, create a pull request. We will guide you here.

Person who completed Task 1A, wait for the pull request, and merge the request into your version of code. We will guide you in resolving conflicts.

## Completion
Congratulations, you have actually collaborated IN REAL TIME!

![Image of Yaktocat](./yes-baby.jpg)

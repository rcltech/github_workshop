# Pair Programming Session
#### Suggested time taken: 20-30 mins for amateur programmers

### Program outline
tictactoe.py is a python program that allows 2 users to play the nostalgic game Tic Tac Toe.

Users take turns to input board numbers to update the board.

##### Data structure
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

### Tasks outline
For this workshop, you and your partner will write 2 different parts of the same program to complete tictactoe.py. One of you will complete one of the tasks. You are not allowed to complete both tasks by yourself, but both of you should work together to solve problems.

The first two pairs of programmers will be given prizes.

#### Task 1A
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

#### Task 1B
Fork the newly created repository

Clone the forked repository
```
git clone link
```


#### Task 2
Discuss with your partner about the program structure, particularly the delegation of task. Work on solving any difficulties together as well.

#### Task A:


#### Task B:

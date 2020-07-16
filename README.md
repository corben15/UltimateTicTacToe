# UltimateTicTacToe
This is a variation of Tic Tac Toe. It consists of a larger Tic Tac Toe board
and inside each cell is another tic tac toe board. There is significantly more
to this game than regular tic tac toe and it is very strategic.

## Board Structure
```text
_|_|_  |  _|_|_  |  _|_|_
_|_|_  |  _|_|_  |  _|_|_
 | |   |   | |   |   | |  
_______|_________|________
_|_|_  |  _|_|_  |  _|_|_
_|_|_  |  _|_|_  |  _|_|_
 | |   |   | |   |   | |  
_______|_________|________
_|_|_  |  _|_|_  |  _|_|_
_|_|_  |  _|_|_  |  _|_|_
 | |   |   | |   |   | |  
 ```

 ## Rules
 The object of the game is to win the big board.
 You do this by winning individual smaller games.
 The person starting, X, goes where ever they want
 then the person placing the O must go in the
 large board in the cell that the X was placed.

 ex:
 So if an X was placed in cell (2,2) or NW/SE (north west south east)

 ```text
  0 1 2    3 4 5     6 7 8
0 _|_|_  |  _|_|_  |  _|_|_
1 _|_|_  |  _|_|_  |  _|_|_
2  | |X  |   | |   |   | |  
 _______|_________|________
3 _|_|_  |  _|_|_  |  _|_|_
4 _|_|_  |  _|_|_  |  _|_|_
5  | |   |   | |   |   | |  
 _______|_________|________
6 _|_|_  |  _|_|_  |  O must
7 _|_|_  |  _|_|_  |  go somewhere
8  | |   |   | |   |    HERE
  ```

 If a small board is won then if a player sends
 the other person to that square they get to go wherever they want on the large board.

"""
Tic-Tac-Toe
Implement a simple Tic-Tac-Toe game for a board of arbitrary size. It should be able to receive user 
input, i.e., where a user token (‘X’ or ‘O’) has been put, and return the state of the game as a result:  did any of the players win, is it a draw, or is the game still ongoing?
Solution hints:
A good design will most likely encapsulate the game state in a class and expose a method or two to 
allow placing tokens and retrieving game status.
An example can be a class with a single public method “placeToken(token, row, column)” that returns a 
string from the set (“FIRST PLAYER WON”, “SECOND PLAYER WON”, “DRAW”, “ONGOING”).
Think about handling exceptions - what if the user provides an invalid token, or places it outside the 
board or over a previous token? Do you raise an error (a.k.a throwing an exception), or return a 
different result?
What if the user provides the same token twice in a row - does your design treat this as an exception, 
or do you leave the question of turn integrity to the user? Note that it’s perfectly okay for the 
solution not to handle this scenario as an error, as long as the decision was made consciously.

clarify
    - board is 3x3 items are represented as strings
    - player vs AI 
    - return message when game is completed, message will vary depending on who won
    - account for invalid input 
    - account for a tie between players 

planning
    enum state: {
        "ongoing"
        "finished"
        "ai turn"
        "player turn" 
    }
    - placing an input
        @params -> inputChoice, row, col
        @returns -> state of class 
        desc: validateInput() -> place input -> checkIfWinner() -> update state -> return stateOfGame() 
    - determine winner 
        @returns -> boolean, T or F if curr player has won
    - create board
        create 3x3 board
    - return state of game 
        @returns -> enumType
    - AI move
        randomly generated
        @params -> inputChoice, row, col
        @returns -> state of class 
        desc: {generateInput() -> validateInput()} -> place input -> checkIfWinner() -> update state -> return stateOfGame() 

"""
from enum import Enum
import math
class GameState(Enum):
    firstPlayerWin = "FIRST PLAYER WON"
    secondPlayerWin = "SECOND PLAYER WON"
    ongoing = "GAME IS ONGOING"
    finished = "GAME IS FINISHED"
    draw = "GAME ENDED IN DRAW"
    firstPlayerTurn = "TURN: FIRST PLAYER"
    secondPlayerTurn = "TURN: SECOND PLAYER"

class Player:
    def __init__(self, ID, symbol):
        self.ID = ID
        self.symbol = symbol
        self.isWinner = False

class TicTacToe:
    def __init__(self, playerOne, playerTwo):
        self.board = [["." for r in range(3)] for c in range(3)]
        self.state = GameState.firstPlayerTurn
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.placed = set()

    def placeMove(self, playerObj, row, col):
        playerID, playerSymbol = playerObj.ID, playerObj.symbol
        if not self.isValid(row, col):
            return

        self.board[row][col] = playerSymbol
        self.placed.add((row, col))

        if self.checkIfWinner():
            playerObj.isWinner = True
            self.state = GameState.firstPlayerWin if playerID == self.playerOne.ID else GameState.secondPlayerWin
        elif self.checkIfDraw():
            self.state = GameState.draw
            return self.state
        else:
            self.state = GameState.secondPlayerTurn if playerID == self.playerOne.ID else GameState.firstPlayerTurn
        return self.state

    def isValid(self, row, col):
        if row < 0 or row >= 3 or col < 0 or col >= 3 and (row, col) in self.placed:
            return False
        return True
    
    def checkIfWinner(self):
        return True if self.checkRow() or self.checkCol() or self.checkDiag() else False

    def checkRow(self):
        for row in self.board:
            if row[0] == row[1] and row[1] == row[2]:
                return True

    def checkCol(self):
        for idx in range(len(self.board)):
            if self.board[0][idx] == self.board[1][idx] and self.board[1][idx] == self.board[2][idx]:
                return True

    def checkDiag(self):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or 
            self.board[2][0] == self.board[1][1] or self.board[0][2]):
            return True
        return False
    
    def checkIfDraw(self):
        if len(self.placed) == len(self.board) * len(self.board[0]):
            return True
        return False

playerOne = Player("justin", "X")
playerTwo = Player("alex", "O")
gameOne = TicTacToe(playerOne, playerTwo)
gameOne.placeMove(playerOne, 0, 0)
gameOne.placeMove(playerTwo, 1, 1)
gameOne.placeMove(playerOne, 0, 2)
gameOne.placeMove(playerOne, 0, 1)
print(gameOne.state)
print(gameOne.board)
"""
Implement a simple Connect Four game server for a board of arbitrary size. Much like the Tic-Tac-Toe game in the previous question, this system
should be able to handle user input (which token is placed in which column)
and notify the user of the game state after the move is made.
As a bonus algorithms/data structures question, try to implement this server for an infinite board (i.e., the pieces fall from infinite height, 
and any column index is valid) with constant-time complexity per operation.

use a matrix to store a row, col board of cells. will represent each cell thats empty as a ["."]
when a col token has been recieved, try moving that token until we reached the end of the matrix or a used cell marked as "X"

[
    [.][.][.]
    [.][.][.]
    [x][.][.]
]
"""
import enum
class GameState(enum.Enum):
    isPlacing = "Currently Placing."
    isDone = "Is done"
    error = "Invalid column, please try again"

class Player():
    def __init__(self, playerID, gameSession, rows, cols):
        self.playerID = playerID
        self.gameSession = gameSession
        self.isWinner = False
        self.rows = rows
        self.cols = cols
class ConnectFour():
    state = GameState.isPlacing
    def __init__(self, player):
        self.board = [["." for i in range(4)] for j in range(4)]
        self.player = player

    def placeToken(self, colIdx):
        if not self.isValid(colIdx):
            return GameState.error

        rowIdx = self.findRowIdx(colIdx)
        self.board[rowIdx][colIdx]
        
        if self.checkIfConnect(colIdx):
            self.state = GameState.isDone
            self.player.isWinner = True
            return self.state
        return self.state

    def isValid(self, colIdx):
        if colIdx < self.cols or colIdx > self.cols:
            return False
        return True

    def findRowIdx(self, colIdx):
        newIdx = 0
        while self.board[newIdx][colIdx] == "." or newIdx < self.rows:
            newIdx += 1
        return newIdx
    
    def checkIfConnect(self, colIdx):
        rowIdx = 0
        while self.board[rowIdx][colIdx] != "." or rowIdx < self.rows:
            idx += 1
        return True if rowIdx == len(self.board) else False
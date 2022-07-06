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

Clarify:
    - cell values are represented by string values/chars
    - return current of game
    - function to return if a cell has been occupied
    - if board is full, game ends in a draw
    - player vs player
    - print an error / return exception 

Board class 
    private encapsulate a game state, derive from enum class GameState()
    private create matrix of cells/strings "."
    assign players, depending on what was passed in 
    private create a set, that keeps track of placed items
    private winner = None
    getters/setters for private members
    placeItem() 
    isValid() 
    checkWinner() -> checkRow() -> checkDiag() -> checkNegDiag() -> checkCol()
    checkDraw() 
    checkState() 
    class Board:
        gameState
        constructor(){
            
        }

Player class
    Player class will be mapped to a board, the board will assign that boards winner to the winner player object
    private player class will hold data such as playerID
    private gameID
    getters/setters for playerID, gameID

enum class for game state
{
    ongoing : "this game is ongoing"
    done: "this game is done" 
}

CODE:

class GameState(enum):
    firstPlayerWon = "First player is the winner"
    secondPlayerWon = "Second player is the winner"
    firstPlayerTurn = "First player is currently going"
    secondPlayerTurn = "Second player is currently going"
    done = "Game is done"
    draw = "Game is a Draw" 

class Player():
    constructor(playerID, symbol, gameID):
        playerID = playerID
        symbol = symbol
        gameID = gameID
        isWinner = False
        
    setters/getters() 

class Board():
    state = GameState.firstPlayerTurn() 
    constructor(playerOne, playerTwo):
        board = [3 X 3 matrix of ["."]] 
        placed = set() 
        playerOne = playerOne
        playerTwo = playerTwo
        winnerPlayer = None

    private placeMove(player, row, col):
        playerID, symbol = player
        if not isValid(row, col):
            raise exception
            return 
        
        board[row][col] = symbol
        placed.add(row, col)

        if checkWinner(player):
            state = GameState.firstPlayerWon() if playerID == playerOne.ID else 
            winnerPlayer = player
            GameState.secondPlayerOne() if playerID == playerTwo.ID
        elif checkDraw():
            state = GameState.draw
            return state
        state = playerOneTurn if playerID == playerOne.id else playerTwoTurn
        return state
    
    private isValid(row, col):
        if row in range(3) or col in range(3) and row, col not in visited:
            return True
        return False
    
    private checkWinner():
        return True if checkRow or checkCol or checkDiag else False
    
    private checkRow():
        for each row in board
            board[row][0] == board[row][1] == board[row][2]
                return True
        return False

    private checkCol():
        for i in range(board):
            board[0][i] == board[1][i] == board[2][i]
                return True
        return False
    
    private checkDiag():
        board[0][0] == board[1][1] == board[2][2] or board[2][0] or board[1][1] or board[0][2]
            return True
        return False
    
    public getState():
        return state
"""


import enum

# enumerations - symbolic names bound to unique constant values; implemented using class
# enables more readable code and better documentation; used to represent constants
class GridPosition(enum.Enum):
  EMPTY = 0,
  YELLOW = 1,
  RED = 2


class Grid:
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols 
    self._grid = None
    self.initGrid()
  
  def initGrid(self):
    # using list comprehension to build 2d grid
    self._grid = [[GridPosition.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]

  def getGrid(self):
    return self._grid 
  
  def getColumn(self):
    return self.cols 
  
  def placePiece(self, col, piece):
    if col < 0 or col >= self.cols:
      raise ValueError("invalid column")
    if piece == GridPosition.EMPTY:
      raise ValueError('invalid piece')
    for row in range(self.rows - 1, -1, -1):
      if self._grid[row][col] == GridPosition.EMPTY:
        self._grid[row][col] = piece
        return row 

  # check if there is a win after each move
  def checkWin(self, connect_n, row, col, piece):
    cnt = 0
    # check horizontal
    for c in range(self.cols):
      if self._grid[row][c] == piece: cnt += 1
      else: cnt = 0
      if cnt == connect_n: return True 
    
    # check vertical
    for r in range(self.rows):
      if self._grid[r][col] == piece: cnt += 1
      else: cnt = 0
      if cnt == connect_n: return True
    
    # check anti-diagonally
    r, c = row, col 
    while 0 <= r < self.rows and 0 <= c < self.cols:
      if self_grid[r][c] == piece: cnt += 1
      else: cnt = 0
      if cnt == connect_n: return True
      r += 1
      c += 1
    
    r, c = row, col 
    while 0 <= r < self.rows and 0 <= c < self.cols:
      if self_grid[r][c] == piece: cnt += 1
      else: cnt = 0
      if cnt == connect_n: return True
      r -= 1
      c -= 1
    
    # check diagonally
    r, c = row, col 
    while 0 <= r < self.rows and 0 <= c < self.cols:
      if self_grid[r][c] == piece: cnt += 1
      else: cnt = 0
      if cnt == connect_n: return True
      r -= 1
      c += 1
    
    r, c = row, col 
    while 0 <= r < self.rows and 0 <= c < self.cols:
      if self_grid[r][c] == piece: cnt += 1
      else: cnt = 0
      if cnt == connect_n: return True
      r += 1
      c -= 1

    return False
      

class Player:
  def __init__(self, name, pieceColor):
    # underscore to denote private variable to readers
    self._name = name
    self._pieceColor = pieceColor

  def getName(self):
    return self._name 
  
  def getPieceColor(self):
    return self._pieceColor
  

class Game:
  def __init__(self, grid, connect_n, targetScore):
    self._grid = grid 
    self._connect_n = connect_n
    self._targetScore = targetScore

    self._players = [
      Player('Player1', GridPosition.YELLOW),
      Player('Player2', GridPosition.RED)
    ]

    self._score = {}
    for player in self._players:
      self._score[player.getName()] = 0

    def printBoard(self):
      grid = self._grid.getGrid()
      for i in range(len(grid)):
        row = ''
        for piece in grid[i]:
          if piece == GridPosition.EMPTY: row += '0 '
          elif piece == GridPosition.RED: row += 'R '
          elif piece == GridPosition.YELLOW: row += 'Y '
        print(row)
      print('')
    
# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8


def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  return TypeOfGame.lower()[0]

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("{0:<5}{1}".format("","-"*25))
    print("R{0:<1}".format(RankNo),end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("{0:<5}{1}".format("","-"*25))
  print()
  print("{0:<6}{1:<3}{2:<3}{3:<3}{4:<3}{5:<3}{6:<3}{7:<3}{8:<3}".format("","F1","F2","F3","F4","F5","F6","F7","F8"))
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if StartRank == BOARDDIMENSION - 1:
      if FinishRank == StartRank - 2 or FinishRank == StartRank - 1:
        CheckRedumMoveIsLegal = True
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False

  RankDifference = abs(FinishRank - StartRank)
  FileDifference = abs(FinishFile - StartFile)

  if FileDifference == RankDifference:
    CheckNabuMoveIsLegal = True
    
  if StartFile < FinishFile and StartRank < FinishRank:
    for count in range(1, BOARDDIMENSION):
      if StartRank + count <= BOARDDIMENSION and StartFile + count <= BOARDDIMENSION:
        if Board [StartRank + count][StartFile - count] != "":
          CheckNabuMoveIsLegal = True

      
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  elif (abs(FinishFile - StartFile)) == 1 and abs(FinishRank - StartRank) == 1:
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  try:
      if (FinishFile == StartFile) and (FinishRank == StartRank):
        MoveIsLegal = False
      else:
        PieceType = Board[StartRank][StartFile][1]
        PieceColour = Board[StartRank][StartFile][0]
        if WhoseTurn == "W":
          if PieceColour != "W":
            MoveIsLegal = False
          if Board[FinishRank][FinishFile][0] == "W":
            MoveIsLegal = False
        else:
          if PieceColour != "B":
            MoveIsLegal = False
          if Board[FinishRank][FinishFile][0] == "B":
            MoveIsLegal = False
        if MoveIsLegal == True:
          if PieceType == "R":
            MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
          elif PieceType == "S":
            MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
          elif PieceType == "M":
            MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
          elif PieceType == "G":
            MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
          elif PieceType == "N":
            MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
          elif PieceType == "E":
            MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  except IndexError:
      print("That is not a legal move - please try again")
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    InitialiseSampleBoard(Board)
  else:
    InitialiseNewBoard(Board)

def InitialiseSampleBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      Board[RankNo][FileNo] = "  "
  Board[1][2] = "BG"
  Board[1][4] = "BS"
  Board[1][8] = "WG"
  Board[2][1] = "WR"
  Board[3][1] = "WS"
  Board[3][2] = "BE"
  Board[3][8] = "BE"
  Board[6][8] = "BR"
  
def InitialiseNewBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      if RankNo == 2:
        Board[RankNo][FileNo] = "BR"
      elif RankNo == 7:
        Board[RankNo][FileNo] = "WR"
      elif RankNo == 1 or RankNo == 8:
        if RankNo == 1:
          Board[RankNo][FileNo] = "B"
        if RankNo == 8:
          Board[RankNo][FileNo] = "W"
        if FileNo == 1 or FileNo == 8:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
        elif FileNo == 2 or FileNo == 7:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
        elif FileNo == 3 or FileNo == 6:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
        elif FileNo == 4:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
        elif FileNo == 5:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
      else:
        Board[RankNo][FileNo] = "  "    
                    
def GetMove(StartSquare, FinishSquare):
  valid_move = False
  valid_option = False
  surrendered = False
  while valid_move  == False and valid_option == False:
    try:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
      if StartSquare != -1: 
        if len(str(StartSquare)) == 2:
            valid_move = True
        else:
            print("Please enter the file AND the rank")
      else:
        DisplayOptions()
        selection = GetOptionSelection()
        surrendered = MakeOptionSelection(selection)
        valid_option = True
    except ValueError:
      print("Please enter the file and the rank")
  valid_move = False
  while valid_move == False and valid_option == False:
    try:
      FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      if FinishSquare != -1:
          if len(str(FinishSquare)) == 2:
              valid_move = True
          else:
              print("Please enter the file AND the rank")
      else:
        DisplayOptions()
        selection = GetOptionSelection()
        surrendered = MakeOptionSelection(selection)
        valid_option = True
    except ValueError:
      print("Please enter the file and the rank")
  return StartSquare, FinishSquare, surrendered

def ConfirmMove(StartSquare, FinishSquare):
    print("Move from space {0} to {1}?".format(StartSquare, FinishSquare))
    confirmed = input("Confirm move(y/n): ")
    return confirmed
                     
def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print("White Redum promoted to White Marzaz Pani")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print("Black Redum promoted to Black Marzaz Pani")
  else:
    if Board[FinishRank][FinishFile] != "  ":
      print()
      TakeColour, TakePiece = GetPieceName(Board[StartRank][StartFile])
      TakenColour, TakenPiece = GetPieceName(Board[FinishRank][FinishFile])
      print("{0} {1} takes {2} {3}.".format(TakeColour, TakePiece, TakenColour, TakenPiece))
      print()
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "
    

def GetPieceName(PieceCode):
  Colour = PieceCode[0]
  Piece = PieceCode[1]
  if Colour == "W":
    Colour = "White"
  elif Colour == "B":
    Colour = "Black"
  if Piece == "S":
    Piece = "Sarrum"
  elif Piece == "M":
    Piece = "Marzaz Pani"
  elif Piece == "N":
    Piece = "Nabu"
  elif Piece == "E":
    Piece = "Etlu"
  elif Piece == "G":
    Piece = "Gisgigir"
  elif Piece == "R":
    Piece = "Redum"
  return Colour, Piece


def DisplayMenu():
  print("Main Menu")
  print("1. Start new game")
  print("2. Load existing game")
  print("3. Play sample game")
  print("4. View high scores")
  print("5. Settings")
  print("6. Quit program")
  

def GetMenuSelection():
  DisplayMenu()
  Choice = int(input("Please select an option: "))
  return Choice

def MakeSelection(Choice):
  if Choice == 1:
    PlayGame("n")
  elif Choice == 2:
    pass
  elif Choice == 3:
    PlayGame("y")
  elif Choice == 4:
    pass
  elif Choice == 5:
    DisplaySettings()
  elif Choice == 6:
    pass



def DisplayOptions():
  print("Options")
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")
  print("4. Surrender")
  

def GetOptionSelection():
  OptionChoice = int(input("Please enter an option: "))
  
  return OptionChoice

def MakeOptionSelection(OptionChoice):
  if OptionChoice == 1:
    pass
  elif OptionChoice == 2:
    Quit = False
    return Quit
  elif OptionChoice == 3:
    pass
  elif OptionChoice == 4:
    surrendered = True
    return surrendered

def DisplaySettings():
  print("1. Use Kashshaptu Piece")
def PlayGame(SampleGame):
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        StartSquare, FinishSquare, surrendered = GetMove(StartSquare, FinishSquare)
        if surrendered == True:
           print("Surrendering.....")
           if WhoseTurn == "W":
             print("White has surrendered, Black wins.")
             GameOver = True
             MoveIsLegal = True
             PlayAgain = "N"
           else:
             print("Black has surrendered, White wins.")
             GameOver = True
             MoveIsLegal = True
             PlayAgain = "N"
        elif surrendered == False:
            MoveConfirmed = ConfirmMove(StartSquare, FinishSquare)
            if MoveConfirmed == "y":
                StartRank = StartSquare % 10
                StartFile = StartSquare // 10
                FinishRank = FinishSquare % 10
                FinishFile = FinishSquare // 10
                MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
                if not(MoveIsLegal):
                  print("That is not a legal move - please try again")
        if surrendered == False:
          GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
          MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
          if GameOver:
            DisplayWinner(WhoseTurn)
          if WhoseTurn == "W":
            WhoseTurn = "B"
          else:
            WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)
    
    
if __name__ == "__main__":
  Quit = False
  while Quit == False:
    Choice = GetMenuSelection()
    MakeSelection(Choice)
  
  






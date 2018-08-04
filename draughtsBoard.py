import pygame
from random import *
import mysql.connector
#this is so i can connect to the database
cnx = mysql.connector.connect(user='root', password="johnmaf23", host="127.0.0.1",database="draughtsdatabase")
cursor = cnx.cursor()


#this is the query that will be used to insert the game board into the database
add_gameBoard= ("INSERT INTO draughtsgameboard "
               "(gameID, userID, columnNo, rowNo, pieceType) "
               "VALUES (%s, %s, %s, %s, %s)")
gameID=1
userID=1
#this is used to see what level computer the user will get
difficulty=3

#this will be used to determine how many pieces each player has to see if the game is one
def calculatePieceTotal():
    redPieceTotal=0
    blackPieceTotal=0
    for x in range(8):
        for y in range(8):
            if gameBoard[x][y]==normalBlack:
                blackPieceTotal=blackPieceTotal+1
            elif gameBoard[x][y]==kingBlack:
                blackPieceTotal=blackPieceTotal+1
            elif gameBoard[x][y]==normalRed:
                redPieceTotal=redPieceTotal+1
            elif gameBoard[x][y]==kingRed:
                redPieceTotal=redPieceTotal+1
    return redPieceTotal,blackPieceTotal

#this function save the game board into the database
def saveGame():
    global gameBoard
    for x in range(8):
        for y in range(8):
            if gameBoard[x][y]!=None:
                pieceType=gameBoard[x][y]#this gets the piece type to be saved into the database
                dataGameBoard=(gameID,userID,x,y,pieceType)#this add the piece os t=data for the sql statement
                cursor.execute(add_gameBoard,dataGameBoard)#this does the saving
                cnx.commit()#to make sure it is in the databas



turn="red"

normalRed,normalBlack,kingRed,kingBlack=1,2,3,4#all the different piece types
playerTwoColour="black"

clickCounter=0#this will be used to determine wether the user is choosing or moving a piece
newGame=True
loggedIn=False
miniGame=False
computerGame=False

# Define some colors
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
pink=(255,51,204)
green=(0,102,0)
lightGreen=(0,255,0)
purple=(153,51,255)
blue=(0,102,255)
lightBlue=(51,204,255)
yellow=(255,204,0)
brown=(153,51,0)
grey=(179,179,179)
greenBlue=(0,102,102)
greyBackground =(225, 225, 225)

# This sets the WIDTH and HEIGHT of each square
width=65
height=65
radius=30#the radius for each circle
margin=0# This sets the margin between each square
xDistanceFromEdge=220
moveCounter=0

playerOneColour="red"
#this is where the coordinates will be stored. they are -1 no so it's no affecting the board
startX=-1
startY=-1
endX=-1
endY=-1

pygame.init()# Initialize pygame
gameBoard=[]
windowSize= [960, 640]# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(windowSize)


pygame.display.set_caption("Draughts Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock();
#this function is used to create the gameboard for a logged in user
def createUsersBoard():
    global gameBoard
    gameBoard[:] = [[None]*8 for i in range(8)]
    boardQuery= "SELECT pieceType FROM draughtsgameboard WHERE userID=%s AND gameID=%s AND columnNo=%s AND rowNo=%s"#query for getting the piece to put into the gameboard
    boardEmpty="DELETE FROM draughtsgameboard WHERE userID= %s AND gameID= %s"
    for x in range(8):
        for y in range(8):
            cursor.execute(boardQuery,(userID,gameID,x,y))
            pieces=cursor.fetchone()
            pieceType=pieces
            gameBoard[x][y]=pieceType
    print(gameBoard)
    cnx.commit()




#these are all the different types of moves that piece can be able to make
def southWestMove(startX,startY):
    return startX-1,startY+1
def southEastMove(startX,startY):
    return startX+1,startY+1
def northWestMove(startX,startY):
    return startX-1,startY-1
def northEastMove(startX,startY):
    return startX+1,startY-1
def southWestJump(startX,startY):
    middleX,middleY=southWestMove(startX,startY)
    return middleX-1,middleY+1
def southEastJump(startX,startY):
    middleX,middleY=southEastMove(startX,startY)
    return middleX+1,middleY+1
def northWestJump(startX,startY):
    middleX,middleY=northWestMove(startX,startY)
    return middleX-1,middleY-1
def northEastJump(startX,startY):
    middleX,middleY=northEastMove(startX,startY)
    return middleX+1,middleY-1



#this will wbe used to either switch turns or find out if someone has won the game
def endTurn():
    global turn
    if turn=="red":
        if checkEndGame(turn)==True:
            font=pygame.font.SysFont("comicsansms", 20)
            if playerOneColour==turn:
                winnerLbl=font.render("RED wins the game", True, (0,0,0))
            else:
                winnerLbl=font.render("BLACK wins the game", True, (0,0,0))

            screen.blit(winnerLbl,(430,620))
        else:
            turn="black"

    else:
        if checkEndGame(turn)==True:
                    font=pygame.font.SysFont("comicsansms", 20)
                    if playerOneColour==turn:
                        winnerLbl=font.render("wins the game", True, (0,0,0))
                    else:
                        winnerLbl=font.render("wins the game", True, (0,0,0))

                    screen.blit(winnerLbl,(430,620))
        else:
            turn="red"




#this is a quick to to see if someone has won the game
#it does this by calculating each piece total
def checkEndGame(turn):
    redTotal,blackTotal=calculatePieceTotal()
    if turn=="red":
        if blackTotal==0:
            return True
        else:
            return False

    else:
        if redTotal==0:
            return True
        else:
            return False


#this is used to find the colour for the correct square
def square_colour(row, col):
    return black if (row + col) % 2 == 0 else white  # Makes upper-left corner white.


#this is used to make the actuall board fo rthe gui
def boardGui(black,white):
    for boardRow in range(8):
        for boardColumn in range(8):
            xCoordinate=((margin+width) * boardColumn + margin)+xDistanceFromEdge
            yCoordinate=(margin+height) * boardRow + margin
            currentColour = square_colour(boardRow, boardColumn)
            pygame.draw.rect(screen,currentColour,[xCoordinate,yCoordinate, width, height])
#this is determining which gameboard to make depending on wether someone is signed in or a new game or mini-game option
def piecesGameBoard():
    if moveCounter==0:
        if loggedIn==True:
            createUsersBoard()
        elif newGame==True:
            newGameBoard()
        elif miniGame==True:
            miniGameBoard()
    else:
        drawPieces(black,red)

#gameboard for a minigame
def miniGameBoard():
    global gameBoard
    global miniGame
    gameBoard[:] = [[None]*8 for i in range(8)]
    pieceType=[normalRed,normalBlack,kingRed,kingBlack]
    totalPieceTotal=randint(12,28)


    for i in range(totalPieceTotal):
            startX=randint(0,7)
            startY=randint(0,7)
            currentPiece=randint(0,3)
            if square_colour(startX,startY) == white:
                if gameBoard[startX][startY] == None:
                    gameBoard[startX][startY]=pieceType[currentPiece]


#game board for a new game
def newGameBoard():
    global gameBoard, newGame
    gameBoard[:] = [[None]*8 for i in range(8)]  # Empty the game board.

    for x in range(8):
        for y in range(8):
            if square_colour(x, y) == white:
                if y in range(3):
                    gameBoard[x][y]=normalRed
                if y in range(5,8):
                    gameBoard[x][y]=normalBlack

    newGame=False


#actually drawing the game board for the gui
def drawPieces():
    global redPieceTotal,blackPieceTotal
    font=pygame.font.SysFont("comicsansms", 30)
    kingLbl=font.render('K', True, (255,255,255))
    for x in range(8):
        for y in range(8):
            xCoordinate=((margin+width) * x + margin+32)+xDistanceFromEdge
            yCoordinate=(margin+height) * y + margin+33
            if gameBoard[x][y]==normalBlack:
                pygame.draw.circle(screen,black,(xCoordinate,yCoordinate),radius)
                # Draw a white outline around edge of piece if the game board square is black.
            if gameBoard[x][y]==kingBlack:
                pygame.draw.circle(screen,black,(xCoordinate,yCoordinate),radius)
                screen.blit(kingLbl,(xCoordinate-10,yCoordinate-20))
            if gameBoard[x][y]==normalRed:
                pygame.draw.circle(screen,red,(xCoordinate,yCoordinate),radius)
            if gameBoard[x][y]==kingRed:
                pygame.draw.circle(screen,red,(xCoordinate,yCoordinate),radius)
                screen.blit(kingLbl,(xCoordinate-10,yCoordinate-20))
            if gameBoard[x][y]==None and square_colour(x,y)==white:
                pygame.draw.circle(screen,white,(xCoordinate,yCoordinate),radius)
    #update display every time a move is played
    pygame.display.update()



#this will be drawing all the other extra info that will be going with the game
def drawGameStatusBox(black):
    pygame.draw.rect(screen, black, [0,520,960,10])
    font=pygame.font.SysFont("comicsansms", 20)
    playerOneLbl=font.render("Player one:", True, (0,0,0))
    playerTwoLbl=font.render("Player two:", True, (0,0,0))
    screen.blit(playerOneLbl,(120,570))#putting the labels onto the creen
    screen.blit(playerTwoLbl,(700,570))
    if playerOneColour=="red":
        pygame.draw.circle(screen,red,(260,590),radius)
        pygame.draw.circle(screen,black,(840,590),radius)
    else:
        pygame.draw.circle(screen,black,(840,590),radius)
        pygame.draw.circle(screen,red,(260,590),radius)


#this is to check that the user has clicked on the right piece
def checkCorrectPlayerPiece(startX,startY):
    global clickCounter
    font=pygame.font.SysFont("comic+sansms", 15)
    if turn=="red":#if its reds turn they can only use normal red or king red
        if gameBoard[startX][startY]!=normalRed:
            if gameBoard[startX][startY]!=kingRed:
                clickCounter=0
                moveStatusLbl=font.render("It's Red's turn. A red piece must be chosen", True, (255,0,0))

                print("not working")
            else:
                moveStatusLbl=font.render("Make your move", True, (255,0,0))

                print("correct piece")
        else:
            moveStatusLbl=font.render("Make your move", True, (255,0,0))

            print("correct piece")
    elif turn=="black":#if its blacks turn they can only use normal black or king black
        if gameBoard[startX][startY]!=normalBlack:
            if gameBoard[startX][startY]!=kingBlack:
                clickCounter=0
                moveStatusLbl=font.render("It's Black's turn. A red piece must be chosen", True, (0,0,0))

                print("not working")
            else:
                moveStatusLbl=font.render("Make your move", True, (0,0,0))

                print("correct piece")

        else:
            moveStatusLbl=font.render("Make your move", True, (0,0,0))

            print("correct piece")
    print(startX,startY)
#this will make the move for the red piece in the gameboard
def makeRedMove(startX,startY,endX,endY):
    gameBoard[startX][startY]=None
    if endY==7:
        gameBoard[endX][endY]=kingRed
    else:
        gameBoard[endX][endY]=normalRed

    endTurn()
#this will make a jump for the red piece in the gameBoard
def makeRedJump(startX,startY,endX,endY,takeX,takeY):
    gameBoard[startX][startY]=None
    gameBoard[takeX][takeY]=None
    if endY==7:
        gameBoard[endX][endY]=kingRed
    else:
        gameBoard[endX][endY]=normalRed

    endTurn()
#this will make a move for the king red in the game Board
def makeKingRedMove(startX,startY,endX,endY):
    gameBoard[startX][startY]=None
    gameBoard[endX][endY]=kingRed
    endTurn()
#this willl make a jump for the king red in the gameboard
def makeKingRedJump(startX,startY,endX,endY,takeX,takeY):
    gameBoard[startX][startY]=None
    gameBoard[takeX][takeY]=None
    gameBoard[endX][endY]=kingRed
    endTurn()
# this will make a move for kingblack in the gameboard
def makeKingBlackMove(startX,startY,endX,endY):
    gameBoard[startX][startY]=None
    gameBoard[endX][endY]=kingBlack
    endTurn()
#this will make a jump for the king black in the gameboard
def makeKingBlackJump(startX,startY,endX,endY,takeX,takeY):
    gameBoard[startX][startY]=None
    gameBoard[takeX][takeY]=None
    gameBoard[endX][endY]=kingBlack
    endTurn()

#this will make a move for the black piece in the game board
def makeBlackMove(startX,startY,endX,endY):
    gameBoard[startX][startY]=None
    if endY==0:
        gameBoard[endX][endY]=kingBlack
    else:
        gameBoard[endX][endY]=normalBlack

    endTurn()
#this will make a jump for the black piece in the gameBoard
def makeBlackJump(startX,startY,endX,endY,takeX,takeY):
    gameBoard[startX][startY]=None
    gameBoard[takeX][takeY]=None
    if endY==0:
        gameBoard[endX][endY]=kingBlack
    else:
        gameBoard[endX][endY]=normalBlack

    endTurn()


#this function does all of the alternative move until comes across a move that meets the requirements for a legitimate move
def checkLegalMove(endX,endY,startX,startY):
    global gameBoard
    checkX,checkY=southWestMove(startX,startY)
    checkX1,checkY1=southEastMove(startX,startY)
    jumpX,jumpY=southWestJump(startX,startY)
    jumpX1,jumpY1=southEastJump(startX,startY)
    checkX2,checkY2=northWestMove(startX,startY)
    checkX3,checkY3=northEastMove(startX,startY)
    jumpX2,jumpY2=northWestJump(startX,startY)
    jumpX3,jumpY3=northEastJump(startX,startY)
    if turn=="red":
        if gameBoard[startX][startY]==normalRed:
            if endX==checkX and endY==checkY:
                if gameBoard[endX][endY]==None:
                    makeRedMove(startX,startY,endX,endY)

            elif endX==checkX1 and endY==checkY1:
                if gameBoard[endX][endY]==None:
                    makeRedMove(startX,startY,endX,endY)

            elif (gameBoard[checkX][checkY]==normalBlack):
                if endX==jumpX and endY==jumpY:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX,checkY
                        makeRedJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX1][checkY1]==normalBlack):
                if endX==jumpX1 and endY==jumpY1:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX1,checkY1
                        makeRedJump(startX,startY,endX,endY,takeX,takeY)

        elif gameBoard[startX][startY]==kingRed:
            if endX==checkX2 and endY==checkY2:
                if gameBoard[endX][endY]==None:
                    makeKingRedMove(startX,startY,endX,endY)

            elif endX==checkX3 and endY==checkY3:
                if gameBoard[endX][endY]==None:
                    makeKingRedMove(startX,startY,endX,endY)

            elif (gameBoard[checkX2][checkY2]==normalBlack):
                if endX==jumpX and endY==jumpY:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX2,checkY2
                        makeKingRedJump(startX,startY,endX,endY,takeX,takeY)
            elif (gameBoard[checkX2][checkY2]==kingBlack):
                if endX==jumpX2 and endY==jumpY2:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX2,checkY2
                        makeKingRedJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX3][checkY3]==normalBlack):
                if endX==jumpX3 and endY==jumpY3:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX3,checkY3
                        makeKingRedJump(startX,startY,endX,endY,takeX,takeY)
            elif (gameBoard[checkX3][checkY3]==kingBlack):
                if endX==jumpX3 and endY==jumpY3:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX3,checkY3
                        makeKingRedJump(startX,startY,endX,endY,takeX,takeY)
            elif endX==checkX and endY==checkY:
                if gameBoard[endX][endY]==None:
                    makeKingRedMove(startX,startY,endX,endY)

            elif endX==checkX1 and endY==checkY1:
                if gameBoard[endX][endY]==None:
                    makeKingRedMove(startX,startY,endX,endY)

            elif (gameBoard[checkX][checkY]==normalBlack):
                if endX==jumpX and endY==jumpY:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX,checkY
                        makeKingRedJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX][checkY]==kingBlack):
                if endX==jumpX and endY==jumpY:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX,checkY
                        makeKingRedJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX1][checkY1]==normalBlack):
                if endX==jumpX1 and endY==jumpY1:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX1,checkY1
                        makeKingRedJump(startX,startY,endX,endY,takeX,takeY)
            elif (gameBoard[checkX1][checkY1]==normalBlack):
                if endX==jumpX1 and endY==jumpY1:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX1,checkY1
                        makeKingRedJump(startX,startY,endX,endY,takeX,takeY)





    else:
        if gameBoard[startX][startY]==normalBlack:
            if endX==checkX2 and endY==checkY2:
                if gameBoard[endX][endY]==None:
                    makeBlackMove(startX,startY,endX,endY)

            elif endX==checkX3 and endY==checkY3:
                if gameBoard[endX][endY]==None:
                    makeBlackMove(startX,startY,endX,endY)

            elif (gameBoard[checkX2][checkY2]==normalRed):
                if endX==jumpX2 and endY==jumpY2:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX2,checkY2
                        makeBlackJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX3][checkY3]==normalRed):
                if endX==jumpX3 and endY==jumpY3:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX3,checkY3
                        makeBlackJump(startX,startY,endX,endY,takeX,takeY)
        elif gameBoard[startX][startY]==kingBlack:
                        if endX==checkX and endY==checkY:
                            if gameBoard[endX][endY]==None:
                                makeKingBlackMove(startX,startY,endX,endY)

                        elif endX==checkX1 and endY==checkY1:
                            if gameBoard[endX][endY]==None:
                                makeKingBlackMove(startX,startY,endX,endY)

                        elif (gameBoard[checkX][checkY]==normalRed):
                            if endX==jumpX and endY==jumpY:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX,checkY
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif (gameBoard[checkX][checkY]==kingRed):
                            if endX==jumpX and endY==jumpY:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX,checkY
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif (gameBoard[checkX1][checkY1]==normalRed):
                            if endX==jumpX1 and endY==jumpY1:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX1,checkY1
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif (gameBoard[checkX1][checkY1]==kingRed):
                            if endX==jumpX1 and endY==jumpY1:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX1,checkY1
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif endX==checkX2 and endY==checkY2:
                            if gameBoard[endX][endY]==None:
                                makeKingBlackMove(startX,startY,endX,endY)

                        elif endX==checkX3 and endY==checkY3:
                            if gameBoard[endX][endY]==None:
                                makeKingBlackMove(startX,startY,endX,endY)

                        elif (gameBoard[checkX2][checkY2]==normalRed):
                            if endX==jumpX2 and endY==jumpY2:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX2,checkY2
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)
                        elif (gameBoard[checkX2][checkY2]==kingRed):
                            if endX==jumpX2 and endY==jumpY2:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX2,checkY2
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)


                        elif (gameBoard[checkX3][checkY3]==normalRed):
                            if endX==jumpX3 and endY==jumpY3:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX3,checkY3
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)
                        elif (gameBoard[checkX3][checkY3]==kingRed):
                            if endX==jumpX3 and endY==jumpY3:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX3,checkY3
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

    print(gameBoard)



#this will search for one of the computer's piece to make a move on
def findComputerPieces():
    global playerOneColour
    for x in range(8):
        for y in range(8):
            if square_colour(x,y)==white:
                if playerTwoColour=="black":
                    if (gameBoard[x][y]==normalBlack) or (gameBoard[x][y]==kingBlack):
                        startX=x
                        startY=y
                        print(startX,startY)
                        ai(startX,startY)
                else:
                    if (gameBoard[x][y]==normalRed) or (gameBoard[x][y]==kingRed):
                        startX=x
                        startY=y
                        ai(startX,startY)

def checkTwoPiecesIntoKing():
    for x in range(8):
        for y in range(8):
            startX,startY=findComputerPieces()
            return x,y
#this function does all of the alternative move until comes across a move that meets the requirements for a legitimate move
def ai(startX,startY):
    if turn=="red":
            if gameBoard[startX][startY]==normalRed:
                endX,endY=southWestMove(startX,startY)
                endX1,endY1=southEastMove(startX,startY)
                jumpX,jumpY=southWestJump(startX,startY)
                jumpX1,jumpY1=southEastJump(startX,startY)
                if gameBoard[endX][endY]==None:
                        makeRedMove(startX,startY,endX,endY)

                if gameBoard[endX1][endY1]==None:
                        makeRedMove(startX,startY,endX,endY)

                elif (gameBoard[checkX][checkY]==normalBlack):
                    if endX==jumpX and endY==jumpY:
                        if gameBoard[endX][endY]==None:
                            takeX,takeY=checkX,checkY
                            makeRedJump(startX,startY,endX,endY,takeX,takeY)

                elif (gameBoard[checkX1][checkY1]==normalBlack):
                    if endX==jumpX1 and endY==jumpY1:
                        if gameBoard[endX][endY]==None:
                            takeX,takeY=checkX1,checkY1
                            makeRedJump(startX,startY,endX,endY,takeX,takeY)

    else:
            if gameBoard[startX][startY]==normalBlack:
                endX,endY=northWestMove(startX,startY)
                endX1,endY1=northEastMove(startX,startY)
                jumpX,jumpY=northWestJump(startX,startY)
                jumpX1,jumpY1=northEastJump(startX,startY)
                if (gameBoard[endX][endY]==normalRed):
                        if gameBoard[jumpX][jumpY]==None:
                            takeX,takeY=endX,endY
                            makeBlackJump(startX,startY,jumpX,jumpY,takeX,takeY)

                elif (gameBoard[endX1][endY1]==normalRed):
                        if gameBoard[jumpX1][jumpY1]==None:
                            takeX,takeY=endX1,endY1
                            makeBlackJump(startX,startY,jumpX1,jumpY1,takeX,takeY)

                elif gameBoard[endX][endY]==None:
                        makeBlackMove(startX,startY,endX,endY)

                elif gameBoard[endX1][endY1]==None:
                        makeBlackMove(startX,startY,endX1,endY1)




#this determines what move can be made
def computerMove(difficulty):
    if difficulty==3:
        ai(startX,startY)



    if difficulty==2:
        ai()
        checkTwoPiecesAndTaken()
        checkMovetoEdge()
        checkOnePieceAndTaken()
        checkMoveAndUnthreatend()

    if difficulty==1:
        ai()
        checkOnePieceAndTaken()
        checkMoveAndUnthreatend()

def checkTurnKing():

    pass
#this accesses all of the functions so that once the game is opened the gui appear
screen.fill(greyBackground)
boardGui(black,white)
piecesGameBoard()
drawGameStatusBox(black)

print(startX,startY,endX,endY,clickCounter)#used as a test to make sure the correct place is clicked

#fps for the game
clock.tick(60)
pygame.display.flip()



# -------- Main Program Loop -----------
while not done:
    if computerGame==True and turn==playerTwoColour:
                findComputerPieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if loggedIn==True:
                saveGame()#this is when the game will be saved
                cursor.close()
                cnx.close()
                done = True
            else:
                cursor.close()
                cnx.close()
                done=True


        elif event.type == pygame.MOUSEBUTTONDOWN:

            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()

            # Change the x/y screen coordinates to grid coordinates
            column = (pos[0]-xDistanceFromEdge) // (width+margin)
            row = pos[1] // (height + margin)
            #getting how many times the screen has been clicked on
            clickCounter=clickCounter+1



            if clickCounter==1:
                startX=column
                startY=row
                checkCorrectPlayerPiece(startX,startY)
            if clickCounter==2:
                endX=column
                endY=row
                checkLegalMove(endX,endY,startX,startY)
                clickCounter=0





            print("Click ", pos, "Grid coordinates: ", row, column)

        drawPieces()






pygame.quit()
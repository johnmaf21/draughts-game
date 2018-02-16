#importing the pygame library for the checkers game it's self
import pygame, sys
from pygame.locals import*

#these will be all the colours that will be used for the game
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,255,0)
PINK=(255,51,204)
GREEN=(0,102,0)
LIGHT_GREEN=(0,255,0)
PURPLE=(153,51,255)
BLUE=(0,102,255)
LIGHT_BLUE=(51,204,255)
YELLOW=(255,204,0)
BROWN=(153,51,0)
GREY=(179,179,179)
GREEN_BLUE=(0,102,102)

size=(1000,1000)#this is setting how the size of the of the screen
screen=pygame.display.set_mode(size)
pygame.display.caption("Draughts")

class Board:
    def __init__(self):
        self.boardMatrix = self.newBoard()

    def newBoard():
        matrix=[[none]*8 for i in xrange(8)]#this sode is useful as it creates the board that will be played on

        for x in range(8):#these two for loops are for creating the colour for the board
            for y in range(8):
                if x%2==0:
                    matrix[x][y]=MenuPages.boardColour1
                else:
                    matrix[x][y]=MenuPages.boardColour2

class pieces:
    def __init__(self):
        self.colour = pieceColour

    def pieceColour():
        pass



carryOn=True#this will allow the window to carry on running once opened
clock=pygame.time.clock()# this will be used to update the screen per certain amount of time

#-----------------------------------------
#this  will be for making a sreenshot of the game so that the user can see how far they are with the previous game
pygame.image.save(Surface, filename)
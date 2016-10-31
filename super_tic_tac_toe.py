#super_tic_tac_toe.py
#CS 111, Winter 2016
#A strategic game involving nine tic-tac-toe boxes embedded within one larger "super" tic-tac-toe grid.

from graphics import *
import random
from time import sleep

class Box:
    
    def __init__(self):
        self.squaresList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.winner = 0
    
    def hasTwoInARow(self):
        #check every possible three in a row to see if it contains one empty square and two squares owned by the same player
        threeInRowList = [(0,1,2), (0,3,6), (0,4,8), (3,4,5), (1,4,7), (2,4,6), (6,7,8), (2,5,8)]
        for item in threeInRowList:
            x, y, z = item
            rowList = [self.squaresList[x], self.squaresList[y], self.squaresList[z]]
            if rowList.count(0) == 1:
                if rowList.count(1) == 2:
                    return 1
                elif rowList.count(2) == 2:
                    return 2
        return 0
    
    def isFull(self):
        #try to find an empty subsquare. if unsuccessful, box is full
        for i in range (9):
                if self.squaresList[i] == 0:
                    return False
        return True
                
        
    def checkWinner(self):
        #if no winner has been assigned, check whether any possible three in a row combination is owned by the same player
        if self.winner == 0:
            threeInRowList = [(0,1,2), (0,3,6), (0,4,8), (3,4,5), (1,4,7), (2,4,6), (6,7,8), (2,5,8)]
            for item in threeInRowList:
                x, y, z = item
                if self.squaresList[x] == self.squaresList[y] and self.squaresList[y] == self.squaresList[z] and self.squaresList[x] != 0:
                    self.winner = self.squaresList[x]
        return self.winner
    
    def checkPotentialWin(self, square, player):
        #see if adding a certain square to a certain player would give that player three in a row in the box
        potentialSquaresList = []
        potentialSquaresList.extend(self.squaresList)
        potentialSquaresList[square] = player
        threeInRowList = [(0,1,2), (0,3,6), (0,4,8), (3,4,5), (1,4,7), (2,4,6), (6,7,8), (2,5,8)]
        potentialWinner = 0
        for item in threeInRowList:
            x, y, z = item
            if potentialSquaresList[x] == potentialSquaresList[y] and potentialSquaresList[y] == potentialSquaresList[z] and potentialSquaresList[x] != 0:
                potentialWinner = potentialSquaresList[x]
        return potentialWinner
        
        
    def checkPotentialTwo(self, square, player):
        #see if adding a certain square to a certain player would give that player two in a row in the box
        potentialSquaresList = []
        potentialSquaresList.extend(self.squaresList)
        potentialSquaresList[square] = player
        threeInRowList = [(0,1,2), (0,3,6), (0,4,8), (3,4,5), (1,4,7), (2,4,6), (6,7,8), (2,5,8)]   
        for item in threeInRowList:
            x, y, z = item
            rowList = [potentialSquaresList[x], potentialSquaresList[y], potentialSquaresList[z]]
            if rowList.count(0) == 1:
                if rowList.count(1) == 2:
                    return 1
                elif rowList.count(2) == 2:
                    return 2
        return 0
            
        
    def move(self, square, player):
    #pass in the square to mark as an int from 0 to 8 and the player as 1 or 2
        self.squaresList[square] = player


        
    def checkBlockedThree(self, square, player):
        #see whether moving in a certain place would prevent another player from getting two in a row or block an existing two in a row
        potentialSquaresList = []
        potentialSquaresList.extend(self.squaresList)
        potentialSquaresList[square] = player
        threeInRowList = [(0,1,2), (0,3,6), (0,4,8), (3,4,5), (1,4,7), (2,4,6), (6,7,8), (2,5,8)]
        for item in threeInRowList:
            x, y, z = item
            rowList = [potentialSquaresList[x], potentialSquaresList[y], potentialSquaresList[z]]
            if rowList.count(1) == 2 and rowList.count(2) == 1:
                return 2
            elif rowList.count(1) == 1 and rowList.count(2) == 2:
                return 1
        return 0
            
    def impossibleTwoInRow(self, square, player):
        #check if moving in a certain square would make an opponent's two in a row impossible
        potentialSquaresList = []
        potentialSquaresList.extend(self.squaresList)
        potentialSquaresList[square] = player
        threeInRowList = [(0,1,2), (0,3,6), (0,4,8), (3,4,5), (1,4,7), (2,4,6), (6,7,8), (2,5,8)]
        for item in threeInRowList:
            x, y, z = item
            rowList = [potentialSquaresList[x], potentialSquaresList[y], potentialSquaresList[z]]
            if rowList.count(1) == 1 and rowList.count(2) == 1:
                return 1
        return 0
    
class Grid:
   
    def __init__(self):
        self.boxList = []
        self.makeBoxes()
        self.winner = 0
        self.player1Boxes = []
        self.player2Boxes = []
        #start in the center box
        self.nextMove = 4
    
    def getNextMove(self):
        #determine where it is legal to move within the grid
        return self.nextMove
    
    def makeBoxes(self):
        #create nine boxes within the grid
        for i in range (9):
            self.boxList.append(Box())
    
    def isCenterFull(self):
        #check whether the center box is full
        return self.boxList[4].isFull()
    
    def potentialWin(self, box, square, player):
        #pass in whether a box has the potential to be won by a player
        return self.boxList[box].checkPotentialWin(square, player)
    
    def twoInARow(self, box):
        #pass in whether a box has two in a row and who owns it
        return self.boxList[box].hasTwoInARow()
    
    def potentialTwo(self, box, square, player):
        #return the potential two-in-a-row possibilities
        return self.boxList[box].checkPotentialTwo(square, player)
    
    def blockedThree(self, box, square, player):
        #returns who may have blocked a three in a row
        return self.boxList[box].checkBlockedThree(square, player)
    def impossibleTwo(self, box, square, player):
        #return whether a two in a row is impossible after a particular move
        return self.boxList[box].impossibleTwoInRow(square, player)
    def isBoxWon(self, box):
        #given a box, returns who has won it
        return self.boxList[box].checkWinner()
        
    def move(self, box, square, player):
        #mark the appropriate box for the appropriate player and, if the box is won, add it to the appropriate list
        self.boxList[box].move(square, player)
        #set the next move to be in the box of the same index as the square just played
        self.nextMove = square
        if self.boxList[box].checkWinner() == 1 and box not in self.player1Boxes:
            self.player1Boxes.append(box)
        if self.boxList[box].checkWinner() == 2 and box not in self.player2Boxes:
            self.player2Boxes.append(box)
        return self.boxList[box].checkWinner()
        
    def isValid(self, box, square):
        #check that the box matches the nextMove parameter and that the square is not already filled
        return self.nextMove == box and self.boxList[box].squaresList[square] == 0
    
    def isOver(self):
        #determine whether the game is over based on whether or not either player owns five boxes
        return len(self.player2Boxes) == 5 or len(self.player1Boxes) == 5
    
    def setWinner(self, player):
        #set the winner as a player, in case force rule comes into effect
        self.winner = player
    
    def getWinner(self):
        #determine which player won the game
        if self.isOver() and len(self.player2Boxes) == 5:
            self.winner = 2
        if self.isOver() and len(self.player1Boxes) == 5:
            self.winner = 1
        return self.winner
        
        
        
        
class Game:
    
    def __init__(self):
        self.interface = GraphicsInterface()
        self.gameboard = Grid()
        self.computerOne = AI()
        self.computerTwo = AI()
        
    def play(self):
        
        #for each player's turn, activate the appropriate box, get the move, mark the appropriate square, and unhighlight the box
        
        computerOrHuman = input("Wecome to Super Tic Tac Toe! \nWould you like to play [0], [1], or [2] player? ")
        
        #highlight the first box
        box = self.gameboard.getNextMove()
        self.interface.highlightBox(box)
        
        if computerOrHuman == "0":
            number = int(input("How many games would you like to generate? "))
            self.generateGames(number)
                
        else:
        
            while True:
                self.takeTurn(1)
                
                self.interface.unHighlightBox(box)
                box = self.gameboard.getNextMove()
                if box == 4 and self.gameboard.isCenterFull():
                    self.gameboard.setWinner(2)
                    break
                if self.gameboard.isOver():
                    break
                self.interface.highlightBox(box)

                if  computerOrHuman == "2":   
                    self.takeTurn(2)

                else:
                    self.computerTwo.takeTurn(2, self.gameboard, self.interface)

                self.interface.unHighlightBox(box)
                box = self.gameboard.getNextMove()
                if box == 4 and self.gameboard.isCenterFull():
                    self.gameboard.setWinner(1)
                    break
                if self.gameboard.isOver():
                    break
                self.interface.highlightBox(box)
                
            winner = self.gameboard.getWinner()
            print("Congratulations! Player", winner, "wins!")
            input("Press any key to exit.")

    def generateGames(self, number):
        #generate a given number of games between two AIs, (keeping the weight list of the winner when applicable)
        for i in range (number):
            
            #randomly generate the skill levels of the AIs for each new game
            self.computerOne.generateWeights()
            self.computerTwo.generateWeights()
            
            ## this was for AI adjustment
#            winnerList = []
#            for j in range (10):
            
                 #highlight the first box
            box = self.gameboard.getNextMove()
            self.interface.highlightBox(box)

            while True:

#                    self.computerOne.takeTurnNoGraph(1, self.gameboard)
                self.computerOne.takeTurn(1, self.gameboard, self.interface)

                self.interface.unHighlightBox(box)
                box = self.gameboard.getNextMove()
                if box == 4 and self.gameboard.isCenterFull():
                    self.gameboard.setWinner(2)
                    break
                if self.gameboard.isOver():
                    break
                self.interface.highlightBox(box)
                    
                sleep(0.25)


#                    self.computerTwo.takeTurnNoGraph(2, self.gameboard)
                self.computerTwo.takeTurn(2, self.gameboard, self.interface)

                self.interface.unHighlightBox(box)
                box = self.gameboard.getNextMove()
                if box == 4 and self.gameboard.isCenterFull():
                    self.gameboard.setWinner(1)
                    break
                if self.gameboard.isOver():
                    break
                self.interface.highlightBox(box)
                
                sleep(0.25)

## this whole section was formerly used for AI generation
#                winnerList.append(self.gameboard.getWinner())
#                self.gameboard = Grid()
#
#            if winnerList.count(1) >= winnerList.count(2):
#                self.computerTwo = AI()
#                weightList = self.computerOne.getWeights()
#                self.computerTwo.adjustWeights(weightList, i % 9)
#
#
#            else:
#                self.computerOne = AI()
#                weightList = self.computerTwo.getWeights()
#                self.computerOne.adjustWeights(weightList, i % 9)
#                
#            if i % 100 == 0:
#                print(weightList, i)

            sleep(3)
    
            self.gameboard = Grid()
            self.interface.getWin().close()
            self.interface = GraphicsInterface()
  
 # this was used for AI generation and adjustment 

#        if winnerList.count(1) >= winnerList.count(2):
#            print("Best weight set:", self.computerOne.getWeights())
#        
#        else:
#            print("Best weight set:", self.computerTwo.getWeights())

        
    def takeTurn(self, player):
        #get coordinates of click from interface, mark appropriate box, check if box is won, denote accordingly
        result = self.interface.getBox()
        if result:
            box, square = result    
            if self.gameboard.isValid(box, square):
                self.gameboard.move(box, square, player)
                self.interface.mark(box, square, player)
                winner = self.gameboard.move(box, square, player)
                if winner != 0:
                    self.interface.markWonBox(box, winner)
                return
        #make sure there's a legal result    
        self.takeTurn(player)
            
class AI:
    def __init__(self):
        self.weightList = [100, 10, 7, 6, 2, 1, 5, 2, 1]
#        self.generateWeights()
        
    def generateWeights(self):
        #randomly generate a weightlist to see which randomly generated list was better
        self.weightList = []
        for i in range (9):
            self.weightList.append(random.randint(0, 1000))
            
    def adjustWeights(self, weightList, i):
        #take an existing weightlist and modify it slightly
        #used for AI adjustment
        for j in range(9):
            
            if j == i:
                
                adjustment = random.randint(0, 1)
                if adjustment == 0: 
                    self.weightList[j] = weightList[j] + 1
                    
                else:
                    self.weightList[j] = weightList[j] - 1
            else:
                self.weightList[j] = weightList[j]

    
        
    def getWeights(self):
        return self.weightList
    
    def takeTurn(self, player, gameboard, interface):
    #check every possible move and choose from legal moves after assigning them weights based on possible outcomes
        legalMoveList = []
        valueList = []


        for box in range (9):
            for square in range(9):
                if gameboard.isValid(box, square):
                    legalMoveList.append((box, square))
                    valueList.append(0)

        random.shuffle(legalMoveList)

        for i in range (len(legalMoveList)):

            box, square = legalMoveList[i]

            #worst move
            if square == 4 and gameboard.isCenterFull():
                valueList[i] = valueList[i] - self.weightList[0]

            #best move
            if gameboard.potentialWin(box, square, player) == player:
                valueList[i] = valueList[i] + self.weightList[1]

            #dec move
            if gameboard.potentialTwo(box, square, player) == player:
                valueList[i] = valueList[i] + self.weightList[2]

            #also a dec move
            if gameboard.blockedThree(box, square, player) == player:
                valueList[i] = valueList[i] + self.weightList[3]

            #eh                
            if gameboard.impossibleTwo(box, square, player) == ((player + 1) % 2):
                valueList[i] = valueList[i] + self.weightList[4]

            #a kind of pointless move
            if gameboard.blockedThree(box, square, player) == ((player + 1) % 2):
                valueList[i] = valueList[i] - self.weightList[5]

            #a pretty harmless alternative
            if gameboard.isBoxWon(square) != 0:
                valueList[i] = valueList[i] + self.weightList[6]

            #lame moves
            if gameboard.twoInARow(square) == 1 and gameboard.isBoxWon(square) == 0:
                valueList[i] = valueList[i] - self.weightList[7]

            if gameboard.twoInARow(square) == player and gameboard.isBoxWon(square) == 0:
                valueList[i] = valueList[i] - self.weightList[8]

        best = max(valueList)
        choice = legalMoveList[valueList.index(best)]

        box, square = choice

        gameboard.move(box, square, player)
        interface.mark(box, square, player)
        winner = gameboard.move(box, square, player)
        if winner != 0:
            interface.markWonBox(box, winner)
            
    def takeTurnNoGraph(self, player, gameboard):
#check every possible move and choose from legal moves after assigning them weights based on possible outcomes without displaying games
#this was mostly for easier adjustment simulations
        legalMoveList = []
        valueList = []


        for box in range (9):
            for square in range(9):
                if gameboard.isValid(box, square):
                    legalMoveList.append((box, square))
                    valueList.append(0)

        random.shuffle(legalMoveList)

        for i in range (len(legalMoveList)):

            box, square = legalMoveList[i]

            #worst move
            if square == 4 and gameboard.isCenterFull():
                valueList[i] = valueList[i] - self.weightList[0]

            #best move
            if gameboard.potentialWin(box, square, player) == player:
                valueList[i] = valueList[i] + self.weightList[1]

            #dec move
            if gameboard.potentialTwo(box, square, player) == player:
                valueList[i] = valueList[i] + self.weightList[2]

            #also a dec move
            if gameboard.blockedThree(box, square, player) == player:
                valueList[i] = valueList[i] + self.weightList[3]

            #eh                
            if gameboard.impossibleTwo(box, square, player) == ((player + 1) % 2):
                valueList[i] = valueList[i] + self.weightList[4]

            #a kind of pointless move
            if gameboard.blockedThree(box, square, player) == ((player + 1) % 2):
                valueList[i] = valueList[i] - self.weightList[5]

            #a pretty harmless alternative
            if gameboard.isBoxWon(square) != 0:
                valueList[i] = valueList[i] + self.weightList[6]

            #lame moves
            if gameboard.twoInARow(square) == player and gameboard.isBoxWon(square) == 0:
                valueList[i] = valueList[i] - self.weightList[7]

            if gameboard.twoInARow(square) == ((player + 1) % 2) and gameboard.isBoxWon(square) == 0:
                valueList[i] = valueList[i] - self.weightList[8]
        
        best = max(valueList)
        choice = legalMoveList[valueList.index(best)]

        box, square = choice

        gameboard.move(box, square, player)


        
class GraphicsInterface:
    
    def __init__(self):
        self.win = GraphWin("Super Tic Tac Toe", 600, 600)
        self.boxList = []
        self.boxCoordsList = []
        self.drawBoxes()
        
    def getWin(self):
        return self.win
        
    def drawBoxes(self):
        #draw nine boxes in a 3x3 arrangement
        for i in range (3):
            for j in range (3):
                box = GraphBox(j*200, i*200)
                box.draw(self.win)
                #store the coordinates of all nine boxes in a list whose indeces correspond to the boxes' positions
                self.boxCoordsList.append(box.getPlayableAreaCoordinates())
                #store the boxes in an indexed list
                self.boxList.append(box)
                
    def getBox(self):
        #find within which box and square a mouse was clicked
        point = self.win.getMouse()
        x, y = point.getX(), point.getY()
        for i in range (9):
            #check if the click was within the playable area of any box
            xMin, yMin, xMax, yMax = self.boxCoordsList[i]
            if xMin <= x <= xMax and yMin <= y <= yMax:
                currentBox = i
                return currentBox, self.getSquare(currentBox, x, y)

    def getSquare(self, currentBox, x, y):
        #given a box, determine which square within it was clicked
        xMin, yMin, xMax, yMax = self.boxCoordsList[currentBox]
        return (y - yMin) // 60 * 3 + (x - xMin) // 60
            
    def mark(self, box, square, player):
        #mark a square within a box with the appropriate player's color
        graphWin = self.win
        self.boxList[box].mark(square, player, graphWin)
        
    def highlightBox(self, box):
        #make the playable area white to indicate active box
        graphWin = self.win
        self.boxList[box].highlight(graphWin)
        
    def unHighlightBox(self, box):
        #return the playable area to gray upon play
        graphWin = self.win
        self.boxList[box].unHighlight(graphWin)
        
    def markWonBox(self, box, player):
        #change the border color of the box to the color of the player who won it
        graphWin = self.win
        self.boxList[box].markWon(player, graphWin)
        
class GraphBox:
    
    def __init__(self, xLoc, yLoc):
    #make a box consisting of a black border and a white/grey playable surface area
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.border = Rectangle(Point(xLoc, yLoc), Point(xLoc + 200, yLoc + 200))
        self.playableArea = Rectangle(Point(xLoc + 10, yLoc + 10), Point(xLoc + 190, yLoc + 190))
        self.border.setFill(color_rgb(0, 0, 0))
        self.border.setOutline(color_rgb(0, 0, 0))
        self.playableArea.setFill(color_rgb(200, 200, 200))
        self.playableArea.setOutline(color_rgb(0, 0, 0))
        self.gridLineList = []
        self.markerList = []
        
    def draw(self, graphWin):
    #draw the box
        self.border.draw(graphWin)
        self.playableArea.draw(graphWin)
        self.drawGridLines(graphWin)
        
        
    def drawGridLines(self, graphWin):
    #create the squares in the box by adding four lines
        line1 = Line(Point(self.xLoc + 70, self.yLoc + 10), Point(self.xLoc + 70, self.yLoc + 190))
        line2 = Line(Point(self.xLoc + 130, self.yLoc + 10), Point(self.xLoc + 130, self.yLoc + 190))
        line3 = Line(Point(self.xLoc + 10, self.yLoc + 70), Point(self.xLoc + 190, self.yLoc + 70))
        line4 = Line(Point(self.xLoc + 10, self.yLoc + 130), Point(self.xLoc + 190, self.yLoc + 130))
        self.gridLineList = [line1, line2, line3, line4]
        line1.draw(graphWin)
        line2.draw(graphWin)
        line3.draw(graphWin)
        line4.draw(graphWin)
        
    def getPlayableAreaCoordinates(self):
        #store the coordinates of every box to facilitate determining which box was clicked
        return self.xLoc + 10, self.yLoc + 10, self.xLoc + 190, self.yLoc + 190
    
    def mark(self, square, player, graphWin):
        #given a square within the box, place a circle of the appropriate color at the center of the square with radius 20
        mark = Circle(Point(self.xLoc + 40 +  60 * (square % 3), self.yLoc + 40 + 60 * (square // 3)), 20)
        if player == 1:
            mark.setOutline(color_rgb(255, 0, 0))
            mark.setFill(color_rgb(255, 0, 0))
        elif player == 2:
            mark.setOutline(color_rgb(0, 0, 255))
            mark.setFill(color_rgb(0, 0, 255))
        mark.draw(graphWin)
        self.markerList.append(mark)
        
    def highlight(self, graphWin):
        #set the playable area to white and draw everything back over it
        self.playableArea.setFill(color_rgb(255, 255, 255))
        self.playableArea.undraw()
        self.playableArea.draw(graphWin)
        for marker in self.markerList:
            marker.undraw()
            marker.draw(graphWin)
        for line in self.gridLineList:
            line.undraw()
            line.draw(graphWin)
    
    def unHighlight(self, graphWin):
        #set the playableArea back to gray
        self.playableArea.setFill(color_rgb(200, 200, 200))
        self.playableArea.undraw()
        self.playableArea.draw(graphWin)
        for marker in self.markerList:
            marker.undraw()
            marker.draw(graphWin)
        for line in self.gridLineList:
            line.undraw()
            line.draw(graphWin)
        
    def markWon(self, player, graphWin):
        #change a box that has been won to the appropriate border color and redraw everything over it
        if player == 1:
            self.border.setFill(color_rgb(255, 0, 0))
        elif player == 2:
            self.border.setFill(color_rgb(0, 0, 255))
        self.border.undraw()
        self.border.draw(graphWin)
        self.playableArea.undraw()
        self.playableArea.draw(graphWin)
        for marker in self.markerList:
            marker.undraw()
            marker.draw(graphWin)
        for line in self.gridLineList:
            line.undraw()
            line.draw(graphWin)

def main():
    game = Game()
    game.play()

    
if __name__ == "__main__":
    main()
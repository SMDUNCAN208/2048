import pygame, random, sys
from pygame.locals import *
pygame.init()

#Dimensions
windowWidth = 1000
windowHeight = 805
boxLength = 195
boxMargin = 5
extraSpace = 200
boxNum = 4


#Colours
black        = (0  ,   0,   0)
white        = (255, 255, 255)
yellow       = (255, 255, 103)
blue         = (183, 252, 249)
grey         = (245, 245, 245)
greyTwo      = (200, 200, 200)
background   = (189, 208, 220)
margins      = (169, 184, 193)

two          = (250, 197, 236)
four         = (135, 189, 240)
eight        = (217, 204, 255)
sixteen      = (222, 156, 153)
threeTwo     = (174,  95, 227)
sixFour      = (232, 220, 130)
oneTwoEight  = (129, 176,  88)
twoFiveSix   = ( 20, 182, 207)
fiveTwelve   = (207, 145, 255)
oneTwoFour   = (  2, 204, 164)
twoFourEight = (102,  69, 237)

twoFont          = (197, 250, 211)
fourFont         = (135, 240, 138)
eightFont        = (242, 255, 204)
sixteenFont      = (177, 219, 245)
threeTwoFont     = (237, 142, 175)
sixFourFont      = (130, 142, 232)
oneTwoEightFont  = (135,  88, 176)
twoFiveSixFont   = (162, 255, 184)
fiveTwelveFont   = (193, 255, 145)
oneTwoFourFont   = (204,   2,  42)
twoFourEightFont = (157, 191,  55)

SCREEN = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('2048')

#Words
fontObj = pygame.font.Font('freesansbold.ttf', 28)
fontObjOne = pygame.font.Font('freesansbold.ttf', 60)
fontObjTwo= pygame.font.Font('freesansbold.ttf', 30)
fontObjThree = pygame.font.Font('freesansbold.ttf', 20)

#Game
boxes = []
previousBoxes = []
global boardScore, savedScore

class Board (object) :
    global onScreen, number, boxScreen, wallXOne, wallXTwo, wallYOne, wallYTwo, currentColour, textColour, merged

    #Takes in the parameters(array position,
    def __init__ (self, _wallXOne, _wallXTwo, _wallYOne, _wallYTwo, _number) :
        self.onScreen = False
        self.number = _number
        self.boxScreen = pygame.Surface((windowWidth, windowHeight), pygame.SRCALPHA)
        self.wallXOne = _wallXOne
        self.wallXTwo = _wallXTwo
        self.wallYOne = _wallYOne
        self.wallYTwo = _wallYTwo
        self.changeColour()
        self.merged = False

    #Updates all of the box
    def updateBox(self, num):
        self.changeNumber(num)
        self.removeScreen()
        self.onScreen = True
        self.changeMerged()
        self.changeColour()

    def removeBox(self):
        self.changeNumber(0)
        self.onScreen = False
        self.removeScreen()
        self.setMerge()

    #If the box is on screen
    def hasBox(self):
        return self.onScreen

    def changeHasBox(self):
        if self.onScreen == False:
            self.onScreen = True
        elif self.onScreen == True:
            self.onScreen = False

    #Says if a box has already been merged or not
    def hasMerged(self):
        return self.merged

    def setMerge(self):
        self.merged = False

    def changeMerged(self):
        self.merged = True

    #The number on the box
    def returnNumber(self):
        return self.number

    def changeNumber(self, change):
        self.number = change

    #The screen for the box
    def getScreen(self):
        return self.boxScreen

    def changeScreen(self, newScreen):
        self.boxScreen = newScreen

    def removeScreen(self):
        self.boxScreen = pygame.Surface((windowWidth, windowHeight), pygame.SRCALPHA)

    #The colour of the box
    def getColour(self):
        return self.currentColour

    def getTextColour(self):
        return self.textColour

    def changeColour(self):
        if self.number == 0 :
            self.currentColour = two
            self.textColour = twoFont
        if self.number == 2 :
            self.currentColour = two
            self.textColour = twoFont
        elif self.number == 4:
            self.currentColour = four
            self.textColour = fourFont
        elif self.number == 8:
            self.currentColour = eight
            self.textColour = eightFont
        elif self.number == 16:
            self.currentColour = sixteen
            self.textColour = sixteenFont
        elif self.number == 32:
            self.currentColour = threeTwo
            self.textColour = threeTwoFont
        elif self.number == 64:
            self.currentColour = sixFour
            self.textColour = sixFourFont
        elif self.number == 128:
            self.currentColour = oneTwoEight
            self.textColour = oneTwoEightFont
        elif self.number == 256:
            self.currentColour = twoFiveSix
            self.textColour = twoFiveSixFont
        elif self.number == 512:
            self.currentColour = fiveTwelve
            self.textColour = fiveTwelveFont
        elif self.number == 1024:
            self.currentColour = oneTwoFour
            self.textColour = oneTwoFourFont
        elif self.number == 2048:
            self.currentColour = twoFourEight
            self.textColour = twoFourEightFont
        else :
            self.currentColour = two
            self.textColour = twoFont


    #The coordinates
    def getXOne(self):
        return self.wallXOne

    def getXTwo(self):
        return self.wallXTwo

    def getYOne(self):
        return self.wallYOne

    def getYTwo(self):
        return self.wallYTwo



def main() :
    global savedScore, boardScore, ended
    ended = False
    savedScore = 0
    boardScore = 0

    drawBoard()
    setBoard()
    randomBox()
    while True:
        for event in pygame.event.get():
            if ended == False :
                if event.type == QUIT or (event.type == KEYUP and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP and event.key == pygame.K_UP:
                    moveAllBoxes(3)
                elif event.type == KEYUP and event.key == pygame.K_DOWN:
                    moveAllBoxes(4)
                elif event.type == KEYUP and event.key == pygame.K_RIGHT:
                    moveAllBoxes(1)
                elif event.type == KEYUP and event.key == pygame.K_LEFT:
                    moveAllBoxes(2)
                elif event.type == KEYUP and event.key == pygame.K_BACKSPACE:
                    undo()
            elif ended == True and event.type == MOUSEMOTION :
                xCentre = (windowWidth + 200) / 2
                mouseX, mouseY = event.pos
                if mouseX >= xCentre - 90 and mouseX <= xCentre - 10 and mouseY >= 375 and mouseY <= 415:
                    yesDrawing(greyTwo)
                elif mouseX >= xCentre + 14 and mouseX <= xCentre + 94 and mouseY >= 375 and mouseY <= 415:
                    noDrawing(greyTwo)
                else :
                    yesDrawing(white)
                    noDrawing((white))
            if ended == True :
                if event.type == QUIT or (event.type == KEYUP and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP :
                    mouseX, mouseY = event.pos
                    xCentre = (windowWidth + 200) / 2
                    #Checks if the user clicks to play again and then restarts the game
                    if mouseX >= xCentre - 90 and mouseX <= xCentre - 10 and mouseY >= 375 and mouseY <= 415 :
                        ended = False
                        savedScore = 0
                        boardScore = 0
                        for i in range(0, 4, 1):
                            del boxes[0]


                        drawBoard()
                        setBoard()
                        randomBox()
                    #Quits the game if the user decides not to play again
                    elif mouseX >= xCentre + 14 and mouseX <= xCentre + 94 and mouseY >= 375 and mouseY <= 415 :
                        pygame.quit()
                        sys.exit()

def drawBoard() :
    SCREEN.fill(margins)
    addingFactor = 200 #(windowHeight / 4)
    for i in range(extraSpace, windowWidth, addingFactor):
        for j in range(5, windowHeight, addingFactor):
            pygame.draw.rect(SCREEN, blue, (i, j, boxLength, boxLength))

    gameText = fontObjOne.render('2048', True, grey, None)
    SCREEN.blit(gameText, (25, 20))

    undoText = fontObjThree.render('Backspace = Undo', True, grey, None)
    SCREEN.blit(undoText, (15, 200))


    pygame.display.update()

def setBoard():
    #Creates the 2d array
    for i in range(0, 4, 1):
        boxes.append([])
        previousBoxes.append([])

    #These are the initial box positions
    boxX = extraSpace
    boxY = boxMargin

    for i in range(0,4, 1):
        for j in range(0,4,1):
            boxes[i].append(Board(boxX, boxX + boxLength, boxY, boxY + boxLength, 0))
            previousBoxes[i].append(Board(boxX, boxX + boxLength, boxY, boxY + boxLength, 0))
            boxY += boxLength + boxMargin
        boxY = boxMargin
        boxX += boxLength + boxMargin

    drawScore()

def drawScore():
    pygame.draw.rect(SCREEN, margins, (0, 100, 200, 100))
    scoreText = fontObjTwo.render("Score: " + str(boardScore), True, grey)
    numberWidth = scoreText.get_width()
    SCREEN.blit(scoreText, ((extraSpace - numberWidth) / 2, 100))
    pygame.display.update()

def randomBox():
    emptySlot = checkFull()
    if emptySlot == True:
        # Change to false to randomize
        addedBox = False

        while addedBox == False:
            randX = random.randrange(0, boxNum)
            randY = random.randrange(0, boxNum)

            if boxes[randX][randY].hasBox() == False:
                boxes[randX][randY].changeHasBox()
                boxes[randX][randY].changeNumber(2)
                boxes[randX][randY].changeColour()
                drawBox(randX, randY, boxes[randX][randY].getXOne(), boxes[randX][randY].getYOne(), boxes[randX][randY].getColour())
                addedBox = True

    else:
        endGame(white, False)

def checkFull() :
    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            if boxes[i][j].hasBox() == False:
                return True
    return False

def drawBox(x, y, positionX, positionY, colour):
    numBox = boxes[x][y].returnNumber()

    pygame.draw.rect(boxes[x][y].getScreen(), colour, (positionX, positionY, boxLength, boxLength))

    numberText = fontObjOne.render(str(boxes[x][y].returnNumber()), True, boxes[x][y].getTextColour())
    numberWidth = numberText.get_width()
    boxes[x][y].getScreen().blit(numberText, (positionX + (195 - numberWidth) / 2, positionY + 67))

    SCREEN.blit(boxes[x][y].getScreen(), (0, 0))
    pygame.display.update()

def moveAllBoxes(direction):
    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            boxes[i][j].setMerge()

    setSavedArray()

    if direction == 1:
        for i in range(3, -1, -1) :
            for j in range(0, 4, 1):
                moveBoxRight(i, j)

        randomBox()
    elif direction == 2:
        for i in range(0, 4, 1) :
            for j in range(0, 4, 1):
                moveBoxLeft(i, j)

        randomBox()
    elif direction == 3:
        for i in range(0, 4, 1) :
            for j in range(0, 4, 1):
                moveBoxUp(i, j)

        randomBox()
    elif direction == 4:
        for i in range(3, -1, -1) :
            for j in range(0, 4, 1):
                moveBoxDown(i, j)

    drawScore()

    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            if boxes[i][j].returnNumber() == 2048 :
                endGame(white, True)

def setSavedArray():
    global boardScore, savedScore
    savedScore = boardScore
    #These are the initial box positions
    boxX = extraSpace
    boxY = boxMargin

    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            previousBoxes[i][j] = Board(boxX, boxX + boxLength, boxY, boxY + boxLength, boxes[i][j].returnNumber())
            if boxes[i][j].hasBox() == True :
                previousBoxes[i][j].changeHasBox()
            boxY += boxLength + boxMargin
        boxY = boxMargin
        boxX += boxLength + boxMargin

def moveBoxRight(x, y) :
    if boxes[x][y].hasBox() == True and boxes[x][y].hasMerged() == False :
        finalX = calculatePosition(x, y, 1)

        currentY = boxes[x][y].getYOne()
        tempX = boxes[x][y].getXOne()
        crossingX = x

        if finalX == x :
            inPosition = True
            hasBeenMoved = False
        else :
            inPosition = False
            hasBeenMoved = True


        while inPosition == False:
            drawBox(x, y, tempX, currentY, boxes[x][y].getColour())
            pygame.draw.rect(boxes[x][y].getScreen(), blue, (boxes[crossingX][y].getXOne(), boxes[x][y].getYOne(), boxLength, boxLength))
            pygame.display.update()

            if tempX == boxes[finalX][y].getXOne():
                inPosition = True

            for i in range(0, 4, 1):
                if tempX == boxes[i][y].getXOne() :
                    pygame.draw.rect(boxes[x][y].getScreen(), margins, (boxes[i][y].getXOne() - boxMargin, boxes[x][y].getYOne(), boxMargin, boxLength))
                    crossingX = i
            tempX += 5

            SCREEN.blit(boxes[x][y].getScreen(), (0,0))

        if hasBeenMoved == True:
            calculateNumber(x, y, finalX, y)

            boxes[finalX][y].updateBox(boxes[x][y].returnNumber())
            drawBox(finalX, y, tempX - 5, currentY, boxes[finalX][y].getColour())
            boxes[x][y].removeBox()


        pygame.display.update()

def moveBoxLeft(x, y) :
    if boxes[x][y].hasBox() == True and boxes[x][y].hasMerged() == False:
        finalX = calculatePosition(x, y, 2)

        currentY = boxes[x][y].getYOne()
        tempX = boxes[x][y].getXOne()
        crossingX = x

        if finalX == x :
            inPosition = True
            hasBeenMoved = False
        else :
            inPosition = False
            hasBeenMoved = True


        while inPosition == False :
            drawBox(x, y, tempX, currentY, boxes[x][y].getColour())
            pygame.draw.rect(boxes[x][y].getScreen(), blue, (boxes[crossingX][y].getXOne(), boxes[x][y].getYOne(), boxLength, boxLength))
            pygame.display.update()

            if tempX == boxes[finalX][y].getXOne():
                inPosition = True

            for i in range(2, -1, -1):
                if tempX + boxLength == boxes[i + 1][y].getXOne():
                    pygame.draw.rect(boxes[x][y].getScreen(), margins, (boxes[i][y].getXOne() + boxLength, boxes[x][y].getYOne(), boxMargin, boxLength))
                    crossingX = i
            tempX -= 5

            SCREEN.blit(boxes[x][y].getScreen(), (0,0))


        if hasBeenMoved == True:
            calculateNumber(x, y, finalX, y)

            boxes[finalX][y].updateBox(boxes[x][y].returnNumber())
            drawBox(finalX, y, tempX + 5, currentY, boxes[finalX][y].getColour())

            boxes[x][y].removeBox()

        pygame.display.update()

def moveBoxUp(x, y) :
    if boxes[x][y].hasBox() == True and boxes[x][y].hasMerged() == False:
        finalY = calculatePosition(x, y, 3)

        currentX = boxes[x][y].getXOne()
        tempY = boxes[x][y].getYOne()
        crossingY = y

        if finalY == y :
            inPosition = True
            hasBeenMoved = False
        else :
            inPosition = False
            hasBeenMoved = True

        while inPosition == False :
            drawBox(x, y, currentX, tempY, boxes[x][y].getColour())
            pygame.draw.rect(boxes[x][y].getScreen(), blue, (boxes[x][y].getXOne(), boxes[x][crossingY].getYOne(), boxLength, boxLength))
            pygame.display.update()

            if tempY == boxes[x][finalY].getYOne():
                inPosition = True

            for i in range(2, - 1, -1):
                if tempY == boxes[x][i].getYOne():
                    pygame.draw.rect(boxes[x][y].getScreen(), margins, (boxes[x][y].getXOne(), boxes[x][i].getYTwo(), boxLength, boxMargin))
                    crossingY = i
            tempY -= 5

            SCREEN.blit(boxes[x][y].getScreen(), (0,0))

        if hasBeenMoved == True:
            calculateNumber(x, y, x, finalY)

            boxes[x][finalY].updateBox(boxes[x][y].returnNumber())
            drawBox(x, finalY, currentX, tempY + 5, boxes[x][finalY].getColour())

            boxes[x][y].removeBox()

        pygame.display.update()

def moveBoxDown(x, y) :
    if boxes[x][y].hasBox() == True and boxes[x][y].hasMerged() == False:
        finalY = calculatePosition(x, y, 4)

        currentX = boxes[x][y].getXOne()
        tempY = boxes[x][y].getYOne()
        crossingY = y

        if finalY == y :
            inPosition = True
            hasBeenMoved = False
        else :
            inPosition = False
            hasBeenMoved = True

        while inPosition == False :
            drawBox(x, y, currentX, tempY, boxes[x][y].getColour())
            pygame.draw.rect(boxes[x][y].getScreen(), blue, (boxes[x][y].getXOne(), boxes[x][crossingY].getYOne(), boxLength, boxLength))
            pygame.display.update()

            if tempY == boxes[x][finalY].getYOne():
                inPosition = True

            for i in range(0, 4, 1):
                if tempY == boxes[x][i].getYOne():
                    pygame.draw.rect(boxes[x][y].getScreen(), margins, (boxes[x][y].getXOne(), boxes[x][i].getYOne() - boxMargin, boxLength, boxMargin))
                    crossingY = i
            tempY += 5

            SCREEN.blit(boxes[x][y].getScreen(), (0,0))

        if hasBeenMoved == True:
            calculateNumber(x, y, x, finalY)

            boxes[x][finalY].updateBox(boxes[x][y].returnNumber())
            drawBox(x, finalY, currentX, tempY - 5, boxes[x][finalY].getColour())
            boxes[x][y].removeBox()

        pygame.display.update()

#1 = right, 2 = left, 3 = up, 4 = down
def calculatePosition(x, y, direction):
    if direction == 1:
        if x != 3:
            for i in range(x + 1, 4, 1):
                if boxes[i][y].hasBox() == True and boxes[x][y].returnNumber() != boxes[i][y].returnNumber():
                    return (i - 1)
                if boxes[i][y].returnNumber() == boxes[x][y].returnNumber() :
                    return (i)
        return 3
    elif direction == 2:
        if x != 0:
            for i in range(x - 1, -1, -1):
                if boxes[i][y].hasBox() == True and boxes[x][y].returnNumber() != boxes[i][y].returnNumber():
                    return (i + 1)
                if boxes[i][y].returnNumber() == boxes[x][y].returnNumber():
                    return (i)
        return 0
    elif direction == 3:
        if y != 0:
            for i in range(y - 1, -1, -1):
                if boxes[x][i].hasBox() == True and boxes[x][y].returnNumber() != boxes[x][i].returnNumber():
                    return (i + 1)
                if boxes[x][i].returnNumber() == boxes[x][y].returnNumber() :
                    return (i)
        return 0
    elif direction == 4:
        if y != 3:
            for i in range(y + 1, 4, 1):
                if boxes[x][i].hasBox() == True and boxes[x][y].returnNumber() != boxes[x][i].returnNumber():
                    return (i - 1)
                if boxes[x][i].returnNumber() == boxes[x][y].returnNumber() :
                    return (i)
        return 3

def calculateNumber(xOne, yOne, xTwo, yTwo):
    global boardScore
    if boxes[xOne][yOne].returnNumber() == boxes[xTwo][yTwo].returnNumber() :
        boxes[xOne][yOne].changeNumber(boxes[xOne][yOne].returnNumber() + boxes[xTwo][yTwo].returnNumber())
        boardScore += boxes[xOne][yOne].returnNumber()

def undo():
    drawBoard()
    setOriginalArray()

    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            if previousBoxes[i][j].hasBox() == True:
                drawBox(i, j, boxes[i][j].getXOne(), boxes[i][j].getYOne(), boxes[i][j].getColour())

    drawScore()

    pygame.display.update()

def setOriginalArray():
    global boardScore, savedScore
    boardScore = savedScore
    #These are the initial box positions
    boxX = extraSpace
    boxY = boxMargin

    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            boxes[i][j] = Board(boxX, boxX + boxLength, boxY, boxY + boxLength, previousBoxes[i][j].returnNumber())
            if previousBoxes[i][j].hasBox() == True :
                boxes[i][j].changeHasBox()
            boxY += boxLength + boxMargin
        boxY = boxMargin
        boxX += boxLength + boxMargin

def endGame(buttonColour, winning) :
    #Makes the screen darker
    global ended
    ended = True
    opaque = (0, 0, 0, 25)  # Black

    screenTwo = pygame.Surface((windowWidth - extraSpace, windowHeight))
    screenTwo.set_alpha(150)
    screenTwo.fill((0, 0, 0))

    SCREEN.blit(screenTwo, (200, 0))

    if winning == True :
        win()
    elif winning == False :
        lose()

    repeatText = fontObj.render('Would you like to play again?', True, black, white)
    repeatTextSurface = repeatText.get_rect()
    repeatTextSurface.center = ((windowWidth + 200) / 2, 325)
    SCREEN.blit(repeatText, repeatTextSurface)

    yesDrawing((buttonColour))
    noDrawing((buttonColour))

def yesDrawing(buttonColour) :
    xCentre = (windowWidth + 200) / 2
    # Create a bordered yes and no box
    pygame.draw.rect(SCREEN, yellow, (xCentre - 92, 373, 84, 44))
    pygame.draw.rect(SCREEN, buttonColour, (xCentre - 90, 375, 80, 40))

    # Prints out the yes and no
    yesText = fontObjThree.render('Yes', True, black)
    yesTextSurface = yesText.get_rect()
    yesTextSurface.center = (xCentre - 50, 395)
    SCREEN.blit(yesText, yesTextSurface)
    pygame.display.update()

def noDrawing(buttonColour) :
    xCentre = (windowWidth + 200) / 2
    # Create a bordered yes and no box
    pygame.draw.rect(SCREEN, yellow, (xCentre + 12, 373, 84, 44))
    pygame.draw.rect(SCREEN, buttonColour, (xCentre + 14, 375, 80, 40))

    noText = fontObjThree.render('No', True, black)
    noTextSurface = noText.get_rect()
    noTextSurface.center = (xCentre + 55, 395)
    SCREEN.blit(noText, noTextSurface)
    pygame.display.update()

#Used when the user completes the game
def win() :
    winText = fontObj.render('You have won!', True, black, white)
    winTextSurface = winText.get_rect()
    winTextSurface.center = ((windowWidth + 200) / 2, (windowHeight / 2) - 200)
    SCREEN.blit(winText, winTextSurface)

def lose() :
    loseText = fontObj.render('You have lost', True, black, white)
    loseTextSurface = loseText.get_rect()
    loseTextSurface.center = ((windowWidth + 200) / 2, (windowHeight / 2) - 200)
    SCREEN.blit(loseText, loseTextSurface)

if __name__ == '__main__':
    main()
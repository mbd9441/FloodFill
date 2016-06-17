import random

class FloodFill:
    colors=["red", "blue", "green", "yellow", "purple", "orange"]
    colorvals=['r','b','g','y','p','o']
    board = []
    size = 0
    boardString = ''
    lastcolor = ''
    maxturn = 1
    turn = 0
    window = None
    game=True

    def __init__(self):
        print("Flood Fill Game")
        self.size = 0
        self.game=True
        self.board=[]
        self.turn=0
        self.boardString=''
        self.lastcolor = ''
        while not self.size:
            self.getSize()
        self.popBoard()
        self.getInput()

    def getSize(self):
        trysize = raw_input("How big do you want the board? (6 or higher): ")
        if trysize.isdigit():
            if int(trysize) >= 6:
                self.size = int(trysize)
                self.maxturn = int(round(2.5*self.size))

    def getInput(self):
        feedback = ''
        while True:
            self.printBoard()
            print(feedback)
            print("Turn: " + str(self.turn) + "/" + str(self.maxturn))
            if self.game:
                feedback = str(self.choice(str(raw_input("Color: ")).lower()))
            else:
                feedback = str(self.choice(str(raw_input()).lower()))

    def choice(self, action):
        color = ''
        feedback = ''
        if self.game:
            if action == 'exit' or action == 'quit':
                exit()
            elif action in self.colors:
                for c in range(len(self.colors)):
                    if self.colors[c] == action:
                        color = self.colorvals[c]
            elif action in self.colorvals:
                color = action
            elif action in 'check' or action == ' ':
                color = 'check'
            else:
                feedback = "Please type one of the following; "
                for cl in self.colors: feedback+=cl+' '
            if color:
                if color == 'check':
                    self.flood(" ", self.board[0][0], [])
                else:
                    if color != self.lastcolor:
                        self.turn+=1
                    self.flood(color, self.board[0][0], [])
                    self.lastcolor = color
                    feedback += "Filled " + str(next(cl for cl in self.colors if cl[0]==color))
            if self.checkWin():
                self.game=False
                feedback += '\nYou Win! \nPlay again? (Yes/No)'
            elif self.turn >= self.maxturn:
                self.game=False
                feedback += '\nOut of turns! \nPlay again? (Yes/No)'
            return feedback
        else:
            if action in 'yes':
                self.__init__()
            elif action in 'no':
                exit()
            else:
                return('Play again? (Yes/No)')

    def popBoard(self):
        for x in range(self.size):
            col = []
            for y in range(self.size):
                col.append(self.colors[random.randint(0,len(self.colors)-1)][0])
            self.board.append(col)

    def printBoard(self):
        self.boardString = ''
        for x in range(len(self.board)):
            col = self.board[x]
            for y in range(len(col)):
                self.boardString += col[y] + ' '
            self.boardString += '\n'
        print(self.boardString)

    def flood(self, colornew, colorold, visited, cursorx=0, cursory=0):
        visited.append((cursorx, cursory))
        self.board[cursorx][cursory] = colornew
        if (cursory>0):
            cursory-=1
            if (((cursorx, cursory) not in visited) and (self.board[cursorx][cursory]==colorold)):
                self.flood(colornew,colorold,visited,cursorx,cursory)
            cursory+=1
        if (cursorx>0):
            cursorx-=1
            if(((cursorx, cursory) not in visited) and (self.board[cursorx][cursory]==colorold)):
                self.flood(colornew,colorold,visited,cursorx,cursory)
            cursorx+=1
        if (cursory<len(self.board[cursorx])-1):
            cursory+=1
            if(((cursorx, cursory) not in visited) and (self.board[cursorx][cursory]==colorold)):
                self.flood(colornew,colorold,visited,cursorx,cursory)
            cursory-=1
        if (cursorx<len(self.board)-1):
            cursorx+=1
            if(((cursorx, cursory) not in visited) and (self.board[cursorx][cursory]==colorold)):
                self.flood(colornew,colorold,visited,cursorx,cursory)
            cursorx-=1

    def checkWin(self):
        width = len(self.board)
        height = len(self.board[0])
        goal =  width * height
        color = self.board[0][0]
        match=0
        for x in range(width):
            for y in range(width):
                if self.board[x][y]==color:
                    match+=1
        return match==goal

flood = FloodFill().__init__

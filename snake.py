class snake():
    snakeNumber = 0
    snakeName = ""
    snakeType = ""

    def __init__(self, snakeCount, name, theType):
        self.snakeNumber = snakeCount
        self.snakeName = name
        self.snakeType = theType

    def printSnake(self):
        print(str(self.snakeNumber)+": "+self.snakeName+" ("+self.snakeType+")")
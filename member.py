class member():
    membershipNumber = 0
    memberName = ""
    memberSnakes = []

    def __init__(self, memberCount, name, snakes):
        self.membershipNumber = memberCount
        self.memberName = name
        self.memberSnakes = snakes

    def printMember(self):
        print("Member "+self.memberName+" (#"+str(self.membershipNumber)+"):")
        print("Snakes:")
        for Snake in self.memberSnakes:
            Snake.printSnake()
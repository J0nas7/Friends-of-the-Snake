from snake import snake
from member import member

indexOfMembers = []
memberCount = 0
snakeCount = 0
newMemberName = ""
newMemberSnakes = []

def startMenu():
    print("Options:")
    print("1: Add a new member and the snakes")
    print("2: List a selected member and the snakes")
    print("3: List all members and the snakes")
    choise = input("What would you like to do?: ")
    print("")

    if choise == 1:
        addMember()
    elif choise == 2:
        printSelectedMember()
    elif choise == 3:
        printAllMembers()
    else:
        print("OPTION DOESN'T EXIST. TRY AGAIN.")

def addMember():
    global memberCount, newMemberName, snakeCount
    memberCount = memberCount+1
    newMemberName = raw_input("The members name: ")
    snakeCount = 0
    saveOrAdd()

def saveOrAdd():
    saveOrAdd_input = input("1: Save member or 2: Add a snake?: ")
    if saveOrAdd_input == 1:
        saveMember()
    elif saveOrAdd_input == 2:
        addSnake()
    
    saveOrAdd()

def saveMember():
    global newMemberName, newMemberSnakes, snakeCount
    theMember = member(memberCount, newMemberName, newMemberSnakes)
    indexOfMembers.append(theMember)
    newMemberName = ""
    newMemberSnakes = []
    snakeCount = 0
    startMenu()

def addSnake():
    global snakeCount, newMemberName, newMemberSnakes
    print("Add a snake to "+newMemberName+"'s list")
    snakeName = raw_input("Snake name: ")
    snakeType = raw_input("Snake type: ")
    
    if snakeType == "Mamba":
        print("WARNING: The snake is very toxic!")
    
    if snakeType == "Anaconda":
        print("INFO: The snake is protected and cannot be added!")
        return
    
    snakeCount = snakeCount+1
    theSnake = snake(snakeCount, snakeName, snakeType)
    newMemberSnakes.append(theSnake)

def printAllMembers():
    global indexOfMembers

    for Member in indexOfMembers:
        Member.printMember()
        print("")

    print("")
    startMenu()

def printSelectedMember():
    global indexOfMembers
    
    memberNumber = raw_input("Enter member number: ")
    
    for Member in indexOfMembers:
        if int(memberNumber) == Member.membershipNumber:
            Member.printMember()

    print("")
    startMenu()

if __name__ == '__main__':
    startMenu()
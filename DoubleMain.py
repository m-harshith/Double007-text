import random
import statistics
ammoGlitchCount = 0
userWins = 0
aiWins = 0
aiVictory = []
userVictory = []

def winCheck(user, ai):
    global gameOver
    global userWins
    global aiWins
    if user == ai and user == 2:
        print('User and ai shot each other, game is a tie')
        gameOver = True
    elif user == 2 and ai == 1:
        print('User shot ai, user wins')
        userWins = userWins + 1
        gameOver = True
    elif user == 1 and ai == 2:
        print('Ai shot user, ai wins')
        aiWins = aiWins + 1
        gameOver = True

def gameUpdate(userMove, aiMove):
    global userBulletCount
    global aiBulletCount
    if userMove == 1:
        userBulletCount = userBulletCount + 1
    if aiMove == 1:
        aiBulletCount = aiBulletCount + 1
    if userMove == 2:
        userBulletCount = userBulletCount - 1
    if aiMove == 2:
        aiBulletCount = aiBulletCount - 1

def legalAiMove():
    global aiBulletCount
    global turn
    global userBulletCount
    if turn == 1:
        return [1]
    if aiBulletCount > 0:
        if userBulletCount == 0:
            return [1,2,2,2]
        else:
            return [1, 2, 3]
    else:
        if userBulletCount > 0:
            return [1,3,3,3,3,3,3,3]
        else:
            return [1]

def legalUserMove():
    global aiBulletCount
    global turn
    global userBulletCount
    if turn == 1:
        return [1]
    if userBulletCount > 0:
        return [1, 2, 3]
    else:
        return [1, 3]

def average(lst):
    return sum(lst) / len(lst)

def memoryUpdate(userMove, aiMove):
    global userMovesMemory
    global aiMovesMemory
    for x in range(2):
        userMovesMemory[x] = userMovesMemory[x+1]
        aiMovesMemory[x] = aiMovesMemory[x+1]
    userMovesMemory[2] = userMove
    aiMovesMemory[2] = aiMove


for x in range(100):
    userWins = 0
    aiWins = 0
    turn = 1
    for i in range(100):
        print('New Game -------------------------------------------------------------------------------------')
        turn = 1
        userBulletCount = 0
        aiBulletCount = 0
        userMovesMemory = [0, 0, 0]
        aiMovesMemory = [0, 0, 0]
        gameOver = False
        textConverter = {1: 'reload', 2: 'shoot', 3: 'block'}
        while gameOver == False:
            #print(legalUserMove())
            #print(legalUserMove())
            userInput = random.choice(legalUserMove())
            aiInput = random.choice(legalAiMove())
            #print('userInput:', userInput, 'aiInput:', aiInput)
            gameUpdate(userInput, aiInput)
            #print('user bullet count:', userBulletCount,' ai bullet count: ', aiBulletCount)
            memoryUpdate(userInput,aiInput)
            print('user: ',textConverter[userInput], ' ai: ', textConverter[aiInput])
            print('user bullet count:', userBulletCount,' ai bullet count: ', aiBulletCount)
            #print("user's move memory: ", userMovesMemory[0], userMovesMemory[1], userMovesMemory[2])
            winCheck(userInput, aiInput)
            turn = turn + 1
            print('next ...')
    print(ammoGlitchCount)
    aiVictory.append(aiWins)
    userVictory.append(userWins)
print('User won: ',userWins)
print('Ai won: ',aiWins)
print('Number of user victories: ', userVictory)
print('Average of user victories: ', average(userVictory))
print('Standard Deviation of: ', statistics.stdev(userVictory))
print('Number of ai victories: ', aiVictory)
print('Average of ai victories: ', average(aiVictory))
print('Standard Deviation of: ', statistics.stdev(aiVictory))
print(average(aiVictory) - average(userVictory))
import random

firstBest = []
secondBest = []
thirdBest = []
listLength = 5                                                     #Variable that represents the size of species list

def calculateSpeciesScore(species):                                #Evaluates quality of each species, 1 = 0 points   2 = 1 point    3 = 2 points
    score = 0
    for i in range(len(species)):
        if int(species[i]) == 2:
            score += 1
        if int(species[i]) == 3:
            score += 2
    return score

def createBaseRandomSpecies(length):
    returnArray = []
    for i in range(length):
        returnArray.append(random.choice([1,2,3]))
    return returnArray

def fillBestThree(species):
    global firstBest
    global thirdBest
    global secondBest
    speciesScore = calculateSpeciesScore(species)
    if speciesScore > calculateSpeciesScore(thirdBest):
        thirdBest = species
        if speciesScore > calculateSpeciesScore(secondBest):
            thirdBest = secondBest
            secondBest = species
            if speciesScore > calculateSpeciesScore(firstBest):
                secondBest = firstBest
                firstBest = species

for i in range(10):
    currentRunSpecies = createBaseRandomSpecies(listLength)
    fillBestThree(currentRunSpecies)
    print('Species: ', currentRunSpecies, 'Score: ', calculateSpeciesScore(currentRunSpecies))

print('First best species: ',firstBest, 'Score: ', calculateSpeciesScore(firstBest))
print('Second best species: ',secondBest,'Score: ', calculateSpeciesScore(secondBest))
print('Third best species: ',thirdBest,'Score: ', calculateSpeciesScore(thirdBest))

#print(calculateSpeciesScore([3,3,3,3]))
#print(createBaseRandomSpecies(5))
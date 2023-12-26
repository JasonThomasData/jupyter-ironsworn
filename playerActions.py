from character import status
from gameModels import enemies, journeys, bonds, vows, progressByRank, inflictByRank, Progress

def health(change):
    status["health"] += change
    print(status)
    
def supply(change):
    status["supply"] += change
    print(status)
    
def spirit(change):
    status["spirit"] += change
    print(status)
    
def momentum(change):
    status["momentum"] += change
    print(status)

def printStatus():
    print(status)

def displayBondTrack():
    print("BONDS")
    print("name:     ", "allBonds")
    print("progress: ", bonds["allBonds"].progress)
    print("---")

def display(trackToDisplay, trackName):
    print(trackName)
    for key in trackToDisplay:
        print("name:     ", key)
        print("rank:     ", trackToDisplay[key].rank)
        print("progress: ", trackToDisplay[key].progress)
        print("---")

def newEnemy(name, rank):
    enemies[name] = Progress(rank, progressByRank[rank], inflictByRank[rank])
    display(enemies, "ENEMIES")
    
def newJourney(name, rank):
    journeys[name] = Progress(rank, progressByRank[rank], None)
    display(journeys, "JOURNEYS")

bonds["allBonds"] = Progress("epic", progressByRank["epic"], None)
def newBond():
    bonds["allBonds"].oneProgress()
    displayBondTrack()

def newVow(name, rank):
    vows[name] = Progress(rank, progressByRank[rank], None)
    display(vows, "VOWS")

def progressEnemy(name):
    enemies[name].oneProgress()
    display(enemies, "ENEMIES")

def progressJourney(name):
    journeys[name].oneProgress()
    display(journeys, "JOURNEYS")
    
def progressBond(name):
    bonds[name]["progress"] += bonds[name]["progressIncrement"]
    display(bonds, "BONDS")

def progressVow(name):
    vows[name]["progress"] += vows[name]["progressIncrement"]
    display(vows, "VOWS")

def enemyInflictsHarm(name):
    status["health"] -= enemies[name].inflictIncrement
    print(status)


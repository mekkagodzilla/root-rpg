#! python3
'''This module generates a woodland as per the rules in the Root RPG'''
import random
import pyinputplus as pyip

def roll(dice):
    '''rolls nd6 and returns the sum of their faces'''
    result = 0
    for die in range(dice):
        result += random.randint(1, 6)
    return result


def selectFactions():
    '''asks the user to select factions for the woodland generator'''
    factions = ['Marquisate', 'Eyrie Dynasties', 'Woodland Alliance', 
                'Riverfolk Company', 'Lizard Cult', 'Corvid Conspiracy', 
                'Grand Duchy']
    # denizens are always a part of the factions
    selectedFactions = ['Denizens']

    numFactionstoAdd = pyip.inputInt(prompt='How many Factions do you want to add?\n',
                        min=2, max=3)

    for num in range(numFactionstoAdd):
        selection = pyip.inputMenu(factions, numbered=True)
        factions.remove(selection)
        selectedFactions.append(selection)

    print('You have selected:', selectedFactions)
    return selectedFactions

clearingNames = ['Patchwood', 'Underleaf', 'Ironvein', 'Clutcher’s Creek', 'Pinehorn', 
                'Sundell', 'Rooston', 'Milltown', 'Oakenhold', 'Limberly', 'Allaburrow', 'Blackpaw’s Dam', 
                'Flathome', 'Tonnery', 'Firehollow', 'Opensky Haven', 'Icetrap', 'Windgap Refuge']

class Clearing:
    def __init__(self, name, paths):
        self.name = name 
        self.paths = paths
        self.dominantCommunity = ''
        self.dominantFaction = ''

    def __str__(self):
        return f"{self.name}, {self.paths} paths, populated by {self.dominantCommunity}, controlled by {self.dominantFaction}."

def rollPathNum():
    my_dict = { k:v for k,v in zip(range(2, 13),[1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5]) }
    return my_dict[roll(2)]

def woodlandGenerator():
    '''Takes a list of factions and generates the woodland'''
    factions = selectFactions()
    clearings = []
    for i in range(1, 13):
        name = random.choice(clearingNames)
        newClearing = Clearing(name, rollPathNum())
        clearingNames.remove(name)
        clearings.append(newClearing)

    #assign dominant species
    species = ['Rabbits'] * 4 + ['Mice'] * 4 + ['Foxes'] * 4
    random.shuffle(species)
    for index, clearing in enumerate(clearings):
        clearing.dominantCommunity = species[index]
    
    #TODO but probably too complex without building a real map: assign controlling faction

    # Print the 12 clearings
    for clearing in clearings:
        print(clearing)



#! python3
'''This module generates a woodland as per the rules in the Root RPG'''
import random
import pyinputplus as pyip
from clearings import Clearing
import rollers

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




def woodlandGenerator():
    '''Takes a list of factions and generates the woodland'''
    factions = selectFactions()
    clearingNames = ['Patchwood', 'Underleaf', 'Ironvein', 'Clutcher’s Creek', 'Pinehorn', 
                    'Sundell', 'Rooston', 'Milltown', 'Oakenhold', 'Limberly', 'Allaburrow', 'Blackpaw’s Dam', 
                    'Flathome', 'Tonnery', 'Firehollow', 'Opensky Haven', 'Icetrap', 'Windgap Refuge']
    clearings = []
    for i in range(1, 13):
        name = random.choice(clearingNames)
        newClearing = Clearing(name, rollers.rollPathNum())
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



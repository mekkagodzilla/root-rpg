#! python3
import random
import pyinputplus as pyip

factions = ['The Marquisate', 'The Eyrie Dynasties', 'The Woodland Alliance', 'The Denizens']


class PlayerCharacter:
    '''Base class modeling a Player Character'''
    def __init__(self, name):
        self.name = name
        self.reputations = {}
        for faction in factions:
            self.reputations[faction] = [0, 0, 0]
            # first number is notoriety boxes ticked, second is prestige boxes marked, last is current reputation with the 
            # faction


    def __repr__(self):
        return f'{self.name} is a vagabond.'


    def prestigeIncrease(self, faction, number):
        self.reputations[faction][1] += number
        # if bonus is currently negative but more than 5 boxes to its right are marked
        if self.reputations[faction][2] < 0 and self.reputations[faction][1] // 5 > 0:
            self.reputations[faction][2] += self.reputations[faction][1] // 5 #move the bonus by marked boxes //5
            self.reputations[faction][1] = 0 # clear the track
        else:
            if self.reputations[faction][1] // 5 > self.reputations[faction][2]:
                self.reputations[faction][2] += 1 # raise bonus by one
                self.reputations[faction][1] = 0 # clear the track


    def notorietyIncrease(self, faction, number):
        self.reputations[faction][0] += number
        # if bonus is currently positive but more than 3 boxes to its left are marked
        if self.reputations[faction][2] > -1 and self.reputations[faction][0] // 3 > 0:
            self.reputations[faction][2] -= self.reputations[faction][0] // 3
            self.reputations[faction][0] = 0 # clear the track
        else:
            if self.reputations[faction][0] // 3 > abs(self.reputations[faction][2]):
                self.reputations[faction][2] -= 1 # reduce bonus by 1
                self.reputations[faction][0] = 0 # clear the track
    
    def roll(self, stat):
        result = random.randint(1, 6) + random.randint(1, 6) + stat
        if result <= 6:
            return 'A miss.'
        elif 7 <= result <= 9:
            return 'A 7-9.'
        return 'A 10+ !'
        



class Vagrant(PlayerCharacter):
    '''Inherits from Player Character and sets specific stuff playbook stuff.'''
    def __init__(self, name):
        super(Vagrant, self).__init__(name)
        self.charm = 2
        self.cunning = 1
        self.finesse = -1
        self.luck = 0
        self.might = 0
    

    
#!python 3


class Clearing:
    '''Clearing object for the ROOT rpg'''
    def __init__(self, name, paths):
        self.name = name 
        self.paths = paths
        self.dominantCommunity = ''
        self.dominantFaction = ''

    def __str__(self):
        return f"{self.name}, {self.paths} paths, populated by {self.dominantCommunity}."

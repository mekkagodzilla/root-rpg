#!python3
'''dice rollers needed to randomize stuff'''
import random

def roll(dice):
    '''rolls nd6 and returns the sum of their faces'''
    result = 0
    for die in range(dice):
        result += random.randint(1, 6)
    return result

def rollPathNum():
    outcomes = { k:v for k,v in zip(range(2, 13),[1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5]) }
    return outcomes[roll(2)]
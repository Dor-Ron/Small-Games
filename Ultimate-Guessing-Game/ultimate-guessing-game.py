#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
import string
import sys
import time


print "Welcome to the Ultimate Guessing game, please select one of the four game mode below."
print "Enter 'q' at any time to quit the game."
print "You'll have 3 tries to guess the randomly generated number, letter, or punctuation sign. \n\t\t\t Good Luck!"

tries_left = 3
    
def initialize():
    '''get game mode from user'''
    game_type = raw_input("Select game mode: [N]umbers, [L]etters, [P]unctuation, [U]ltimate  ").upper()
    while game_type not in "NLPUQ":
        print "That's not a valid option, please choose again."
        game_type = raw_input("Select game mode: [N]umbers, [L]etters, [P]unctuation, [U]ltimate  ").upper()
    if game_type == "N":
        possibilities = [str(x) for x in range(1, 101)]
        print "Choose a number between 1-100"
    elif game_type == "L":
        possibilities = list(string.letters)
        print "Choose a letter. The lucky letter can be lower case or upper case."
    elif game_type == "P":
        possibilities = list("!@#$%^&*()_+-=[]{}\/.,<>`~\":;'")
        print "Choose one of the following: !@#$%^&*()_+-=[]{}\/.,<>`~\":;'"
    else:
        possibilities = list(string.letters) + list("!@#$%^&*()_+-=[]{}\/.,<>`~\":;'") + [str(x) for x in range(1, 101)]
        print "Choose either a number between 1-100, a letter upper or lower case, or one of the following punctuation marks: !@#$%^&*()_+-=[]{}\/.,<>`~\":;'"
    if game_type == "Q":
        sys.exit() 
    return possibilities

    
def randomize(possibilities):
    '''selects the answer'''
    lucky_choice = random.choice(possibilities)  # make list of ints so same method for all types. random.choice instead of random.randrange or random.randint
    return lucky_choice


def user_guess(possibilities):
    '''get guess from user, makes sure its valid'''   
    guess = raw_input("Please enter your guess: ")  # make numbers str that way even if numbers is selected this works 
    if guess == "Q":
        sys.exit()    
    while guess not in possibilities:
        print "Not a valid guess, please try again."
        guess = raw_input("Please enter your guess: ")
    return guess


def check_guess(attempt, lucky_choice):
    '''checks user guess and reacts accordingly to amount of guesses left'''
    guess = attempt
    lucky_choice = lucky_choice
    global tries_left
    if guess == lucky_choice:
        print "Congratulations!! You win!"
        time.sleep(2)
        sys.exit()
    else:
        tries_left -= 1
        print "Bummer! Wrong guess. You have %d guesses left" % tries_left
        if tries_left == 0:
            print "Sorry, you lost... \nThe answer was {}".format(lucky_choice) 
            time.sleep(2)
            sys.exit() 
    return tries_left  


def game_loop():
    '''continues game as long as there are tries left.'''
    options = initialize()
    correct = randomize(options)
    while tries_left > 0:
        user = user_guess(options)
        attempts_left = check_guess(user, correct)

if __name__ == "__main__":
    game_loop()

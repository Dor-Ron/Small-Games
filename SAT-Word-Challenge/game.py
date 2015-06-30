#!/usr/bin/env python
#-*- coding: utf-8 -*-

from random import choice
from sys import exit
from re import findall
import logging; logging.basicConfig(filename = "scores.log", level = "INFO")

#get results from scraper.py
sat_words = open("words.txt").read().split("\n")  # each word as separate index


#make lists of definitions
definitions = [] 
for word in sat_words:
    if ")" in word:
        definitions.append(word[word.index(")") + 2:])  # everything after part of speech


#make a list of words and corresponding parts of speech
words = []
for word in sat_words:
    if "(" in word:
        words.append(word[:word.index(")") + 1])  # everything before and including the part of speech


#make dictionary matching words and defintions
word_map = {}
for num in xrange(len(words)):
    word_map[words[num]] = definitions[num]


def random_definitions(word):
    '''Ensure that one of the options is the correct definition'''
    correct_definition = word_map[word]
    options = []
    for i in xrange(3):
        options.append(choice(definitions))
    options.append(correct_definition)
    return sorted(options)


def prompt_user():
    '''prompts user, can be usedd recursively'''
    stdin = raw_input("\nAnswer: ").lower()
    if stdin in "abcd":
        return stdin
    elif stdin == "q":
        logging.info(score)
        exit()
    else: 
        return prompt_user()

#to find previous high score
scores_file = open("scores.log").read()    
past_scores = findall(r'\d+', scores_file)
try: 
    high_score = max(past_scores)
except ValueError: #if past scores is empty
    pass

#game loop
wrong = 0
score = 0
query = "\nWord: {}\n a) {}\t b) {}\n c) {}\t d) {}"
print "Welcome to the SAT Practice Word Test.\nPlease select the letter representing the correct defintion for the presented word."
print "Enter a, b, c, or d for the answer. q to quit.\n"
print "The goal of the game is to beat your previous score, and learn the words of course. Good Luck!! :D"
print "+" * 50

while True:
    lucky_word = choice(words)
    options = random_definitions(lucky_word)
    print query.format(lucky_word, options[0], options[1], options[2], options[3])
    res = prompt_user()
    if res == "a" and word_map[lucky_word] == options[0]: 
        score += 10
    elif res == "b" and word_map[lucky_word] == options[1]: 
        score += 10
    elif res == "c" and word_map[lucky_word] == options[2]:
        score += 10
    elif res == "d" and word_map[lucky_word] == options[3]:
        score += 10
    else:
        print "\nYou're incorrect :/ The correct answer is: {}: {}".format(lucky_word, word_map[lucky_word])
        wrong += 1
        print "\nYou have " + str(3 - wrong) + " tries left.\n"

    print "Your score is: {}".format(score)
    try:
        print "The score to beat is %s" % high_score
    except NameError: #if variable doesn't exist yet
        pass

    if wrong == 3:
        logging.info(score)
        break

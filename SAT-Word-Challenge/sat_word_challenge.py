#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests
from string import ascii_letters

#Part 1: Parsing Words, definitions, and Part of Speech from SparkNotes website
soup = bs(requests.get("http://www.sparknotes.com/testprep/books/newsat/chapter15section4.rhtml").text)

strong = soup.find_all("b") #all words are encapsulated in bold tag
italics = soup.find_all("i") #all parts of speech are encapsulated in italics

bolded = [str(word) for word in strong] #convert elements from tag.object to str.object
italicized = [str(pos) for pos in italics] #same for parts of speech

#test1 - passed
#print bolded, italicized

word_list = []
parts_of_speech = []

for word in bolded:
    word_list.append(word[3:-4])  #not include the tags

for word in word_list:
    if word[0] == "1" or " ": #get rid of few bolded numbers
        word_list.remove(word)

#print word_list


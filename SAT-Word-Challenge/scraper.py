#!/usr/bin/env python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import requests
from os import system

# Part 1: Parsing Words, definitions, and Part of Speech from SparkNotes website
soup = bs(requests.get("http://www.sparknotes.com/testprep/books/newsat/chapter15section4.rhtml").text)


strong = soup.find_all("b")  # all words are encapsulated in bold tag
italics = soup.find_all("i")  # all parts of speech are encapsulated in italics
descriptions = soup.find_all("dl")


bolded = [str(word) for word in strong]  # convert elements from tag.object to str.object
italicized = [str(pos) for pos in italics]  # same for parts of speech
meaning = [str(desc) for desc in descriptions]


word_list = []
parts_of_speech = []
definition_list = []


for word in bolded:
    word_list.append(word[3: - 4])  # not include the tags

for word in word_list:
    if word[0] == "1" or "2" in word:  # get rid of few bolded numbers
        word_list.remove(word)

for pos in italicized:
    parts_of_speech.append(pos[3: - 4]) #get rid of <i> tag

for idx in parts_of_speech:
    if idx[-1] != ")":
        parts_of_speech.remove(idx)  # get rid of anything not enclosed in parenthesis since pos structured as (v.)

temp_list = []
for sent in meaning:
    temp_list.append(sent[sent.index("\n"): - 10])  # get rid of </dd> and </dl> tags

for defn in temp_list:
    definition_list.append(defn[2:defn.index("(") - 1])  # to deal with new-line character being printed


with open('words.txt', 'w') as word_file:
    for idx in range(len(word_list)):
        word_file.write("%s %s %s\n" % (word_list[idx], parts_of_speech[idx], definition_list[idx]))


system("cat words.txt") 

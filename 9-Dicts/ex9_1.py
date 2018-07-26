
# Exercise 1: Download a copy of the file from www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn't matter what the values are. 
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.


#import requests
#r = requests.get('http://www.py4e.com/code3/words.txt')
#txt = r.text

fh = open('words.txt','r')
wordlist, tmpd = [], {}

ftext = fh.read()
wordlist = ftext.split()

d = tmpd.fromkeys(wordlist,0)
# for s in fh:
#	li = s.split()
#	wordlist.append(li)

print(len(d))
# print(d.keys())
print(d['newfound']) 


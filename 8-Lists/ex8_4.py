'''
Exercise 8.4: 

Download a copy of the file from www.py4e.com/code3/romeo.txt
Write a program to open the file romeo.txt and read it line by line. 
For each line, split the line into a list of wordlist using the split function. 
For each word, check to see if the word is already in a list. 
  If the word is not in the list, add it to the list. 
When the program completes, sort and print the resulting wordlist in alphabetical order.
'''
wordlist = []

fhandle = open('romeo.txt', 'r')
for line in fhandle:
    # print(line, type(line))
    l = line.split()
    for inwords in l:
        if inwords in wordlist:
            continue
        else:
            wordlist.append(inwords)

wordlist.sort()
print(wordlist)

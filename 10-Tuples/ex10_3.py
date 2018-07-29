import string

#Import file to analyze
#fname = input("Enter filename: ")

testfile = open('../mbox-short.txt',r)
freq_dict = {} 

for l in testfile:
	c = l.split()
	cs = c.split().lower()
	cs.





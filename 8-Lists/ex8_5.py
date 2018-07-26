'''
Ex.8.5
Open the file mbox-short.txt and read it line by line.
When you find a line that starts with 'From ' like the following line:
	From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
Then print out a count at the end.
'''

count, emails = 0, []
with open('../mbox-short.txt', 'r') as mbfile:
    for es in mbfile:
        if es.startswith("From "):
            w2 = es.split()[1]
            emails.append(w2)
            print(w2)
            count = count + 1

print("There were", count, "lines in the file with From as the first word")


'''  THIS IS HOW IT HAD TO BE SUBMITTED TO THE AUTOGRADER   
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

count, emails = 0, []
mbfile = open(fname, 'r')
    
for es in mbfile:
        if es.startswith("From "):
            w2 = es.split()[1]
            emails.append(w2)
            print(w2)
            count = count + 1

print("There were", count, "lines in the file with From as the first word")
'''
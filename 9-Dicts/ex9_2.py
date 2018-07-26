# Exercise 9.2

#fname = input('Open File Name')
fname = 'wrongfile.txt'

try:
	fh = open(fname,'r')
except:
	fh = open('../mbox-short.txt','r')
	print('mbox-short.txt has been loaded')

# For loop with split[2] for day of the week
lst, wrdcounter = [], {} # Create word list and dict init
for echlne in fh:
	if not echlne.startswith("From "): 
		continue
	else:
		w = echlne.split()[2] # Assign the day of week to temp variable
		wrdcounter[w] = wrdcounter.get(w,0) + 1
"""
for k in lst:  # This loop is now unneccessary 
	wrdcounter[k] = wrdcounter.get(k,0) + 1 #set value to 1 if not seen before else add 1
"""
# print(lst)
print(wrdcounter)

# Sort the keys and reprint.
lst = wrdcounter.keys()
lst = sorted(lst)

for k in lst:
	print('key = {}, value = {}'.format(k,wrdcounter[k])) 

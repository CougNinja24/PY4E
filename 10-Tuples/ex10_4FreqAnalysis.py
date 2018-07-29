
#Freq Analysis, need to add def in this file for stringcleaning
import string
from stringcleaning import str_cleaner as SC

#fname = input('Enter file for analysis')
try:
    fh = open(fname,'r')
except:
    fh = open('../mbox-short.txt','r')

freq, cln_strngs = {}, []
for ls in fh:
    cln_strngs.append(SC(ls))
              
#print(cln_strngs[0:10])
              
for i in cln_strngs:
    t = i.lower()
    for c in t:
        if c in string.ascii_lowercase:
            freq[c] = freq.get(c,0) + 1

# Decorate
sl = []
for k,v in freq.items():
	sl.append((v,k)) # Value first for sorting

#Sort
sorted_list = sorted(sl, reverse=True)

print('Sorted Analysis by Value --> ',sorted_list)

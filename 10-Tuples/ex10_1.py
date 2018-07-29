# create list of tuples with most commits sent, both forward and reverse
fh = open('../mbox-short.txt', 'r')
emails = {}

for echlne in fh:
	if echlne.startswith('From '):
		addr = echlne.split()[1]
		emails[addr] = emails.get(addr,0) + 1
		
largest = None; key = 0
for k in list(emails.keys()):
    if largest is None or emails[k] > largest:
        largest, key = emails[k], k
        print(emails[k])
    
sort_list = []
for k,v in emails.items():
	sort_list.append((v,k)) #value first for sorting
	# print("Added {} to sort_list".format((k,v)))

s = sorted(sort_list)
s1 = sorted(sort_list, reverse=True)

print(s) #Normal sort
print(s1) #Reverse Sort
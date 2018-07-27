fh = open('../mbox-short.txt', 'r')
emails = {}

for echlne in fh:
	if echlne.startswith('From '):
		addr = echlne.split()[1]
		emails[addr] = emails.get(addr,0) + 1
		
largest = None; kval = 0
for k in list(emails.keys()):
    if largest is None or emails[k] > largest:
        largest, kval = emails[k], k
        print(emails[k])
    
    



print(largest,kval)
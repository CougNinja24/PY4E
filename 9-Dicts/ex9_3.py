#ex 9.3 - Build histrogram from sent emails in mbox-short.txt

fh = open('../mbox-short.txt', 'r')
emails = {}

for echlne in fh:
	if echlne.startswith('From '):
		addr = echlne.split()[1]
		emails[addr] = emails.get(addr,0) + 1

# print(emails)
'''
s_emails = sorted(emails)
for a in s_emails:
	print(emails.items())
'''

#ex 9.4 - Add the max min loop to find the largest sender and print it.

largest = None
for k,v in emails:
	if largest is None or v > largest:
		largest = k,v

print(largest, emails[largest])

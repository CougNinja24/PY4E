
fh = open('../mbox-short.txt', 'r')
emails = {}

for l in fh:
	if l.startswith("From "):
		w = l.split(':')[0]
		w = w.split()
		w = w[-1]
		emails[w] = emails.get(w,0) + 1

lst = []

for k,v in emails.items():
	lst.append((k,v))	

#print(lst)
#print('Sorted list \n',sorted(lst))
slist = sorted(lst)

for li in slist:
	print(li)


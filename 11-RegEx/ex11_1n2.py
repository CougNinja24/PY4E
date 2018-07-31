# Ex 11.2  - Search mbox-short and match 'New Revision: 39772' Format

import re
fh = open('../mbox-short.txt','r')
res = []
patt = '^New Revision: ([0-9]+)'
for l in fh:
	if re.findall(patt,l):
		t = l.rstrip()
		res.append(float(re.findall(patt,t)[0]))


cnt = 0; totalval = 0
for v in res:
	cnt += 1
	totalval += v

print('count = {}, totalval = {}'.format(cnt,totalval))
print('totalval/cnt  = {:9.4f}'.format(totalval/cnt)) #9 padding and 4 decimal spots.  'f' is required to work correctly

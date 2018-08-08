import re
#Regex practice
fh = open('../mbox-short.txt','r')

'''
SEARCH COMMAND
re.search()
'''

rp = '\\s?FROM\\s?.+\\['
rp2 = '\\[?(\\d+\\.){2,4}\\]?' #Look for 2,4 digit number sequences

#for l in fh:
#	if re.search(rp2,l):
#		print(l)

'''
EXTRACTING DATA - re.findall()
assign output to variable as list of matches
'''

farp1 = '(\\S+)@(\\S+)' #Whitespace @ whitespace, remove parenthesis to remove capture groups
txt = fh.read(2400)
m = re.findall(farp1,txt)
if len(m) > 0:
	print(m)

""" 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

Use the file name mbox-short.txt as the file name
"""
# Exercise used input, but for testing, put file name in variable

fname = input("Enter file name: ")
fh = open(fname)
occurs, vals = 0, []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    occurs += 1
    vals.append(line)
    # print(line)
# print(occurs, ' Occurences')
# print(vals)
numbers = []
for v in vals:
    v = v[v.find('0'):]
    # print(v)
    numbers.append(float(v))
print(numbers)

avg = 0
for n in numbers:
    avg += n
avg = avg / occurs
print(' Average spam confidence : ', avg)

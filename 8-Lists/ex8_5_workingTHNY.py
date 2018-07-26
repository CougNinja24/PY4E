count, emails = 0, []
with open('../mbox-short.txt', 'r') as mbfile:
    for es in mbfile:
        if es.startswith("From "):
            l2 = es.split()[1]
            emails.append(l2)
            count = count + 1
        
            
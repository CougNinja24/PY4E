# ex 8.1 Lists

'''
Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
'''

original_list = [1, 3, 4, 6, 8, 9, 65]


def chop(lst):
    del lst[0]  # First chop
    del lst[len(lst) - 1]  # Tail chop
    return


def middle(lst):
    return lst[1:-1] # returns a new list


m = middle(original_list)
chop(original_list)
print('m = ', m)
print('original_list = ', original_list)
print('m is original_list? ', m is original_list) #confirms not same

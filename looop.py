# add to list until 5 then stop

def sublist(lst):
    idx = 0
    sublst = []
    while idx < len(lst):
        if lst[idx] != 5:
            sublst.append(lst[idx])
        else:
            break;
        idx = idx + 1
    return sublst

# Checkout
# while loop
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()

# check until 7
def check_nums (lst):
    idx = 0
    nList = []
    while (idx < len(lst)):
        if lst[idx] != 7:
            nList.append(lst[idx])
        else:
            break
        idx = idx + 1
    return nList

#iterate over a string

def sublist(lst):
    sublist = []
    idx = 0
    while (idx < len(lst)):
        if lst[idx] != "STOP":
            sublist.append(lst[idx])
        else:
            break
        idx = idx + 1
    return sublist

#stop when z
def stop_at_z(lst):
    sub = []
    i = 0
    while i < len(lst):
        if lst[i] == "z":
            break
        else:
            sub.append(lst[i])
        i += 1
    return sub

#Challenge: Write a funct called beginning that takes  lst as input and contains a while loop that only stops once the eleme of the lst is string ‘bye’.
# What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element,
# the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge,
# do this without slicing
def beginning (lst):
    i = 0
    string = []
    while i < len(lst):
        if lst[i] == "bye":
            break
        else:
            string.append(lst[i])
        i += 1
        if len(string) == 10:
            break
    return string


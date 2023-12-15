#Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.
def test(x, y = True, dict1= {2:3, 4:5, 6:8}):
    if y:
        for key in dict1.keys():
            if key == x:
                return dict1[key]
    else:
        return  y

#

def checkingIfIn(x, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction:
        return x in d.keys()
    else:
        return x not in d.keys()

# calling the function to produce a specific behavior

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false

# Call the fucntion so that it returns True and assign it to the variable c_true

# Call the function so that the value of fruit is assigned to the variable fruit_ans

# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check


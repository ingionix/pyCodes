numbs = [5, 10, 15, 20, 25]
n_numbs = []
for num in numbs:
    n_numbs.append(num + 5)
    print(n_numbs)

# filter a letter in item of a list
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois", "Peach", "Beige"]

for position in range(len(colors)):
    color = colors[position]
    print(color)
    if color[0] in ["P", "B", "T"]:
        del colors[position]
print(colors)

# count number of mark >= 90 in the list
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = 0
list_score = scores.split(" ")
for score in list_score :
    if int(score) >= 90:
        a_scores += 1

# create acronym from a list or a string

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sent_list = sent.split(" ")
acro = ""
for word in sent_list:
    if word not in stopwords:
        acro += (word[:2] + ". ")
        print(acro)
acro = acro.upper()
acro = acro[:len(acro)-2]

# A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome
# by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase
# to the variable r_phrase so that we can check your work.
p_phrase = "was it a car or a cat I saw"
r_phrase = ""
for letter in p_phrase:
    r_phrase = letter + r_phrase
print(r_phrase)

# Provided is a list of data about a store’s inventory where each item in the list represents the name of an item,
# how much is in stock, and how much it costs. Print out each item in the list with the same formatting,
# using the .format method (not string concatenation). For example, the first print statment should read
# The store has 12 shoes, each for 29.99 USD.
#Exo for format method, list, split and accessing string element inside list.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    name, quantity, price = item.split(",")
    print("The store has{} {}, each for{} USD.".format(quantity, name, price))
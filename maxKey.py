#
# d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}
#
# ks = d.keys()
# # initialize variable best_key_so_far to be the first key in d
# print(ks)
# best_key_so_far = d["a"]
#
#
# #Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum value, it’s OK to print out either one. Fill in the skeleton code
#
# d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}
#
# ks = d.keys()
# best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
# for k in ks:
#     if d[k] > d[best_key_so_far]:
#         best_key_so_far = k
#
# print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))
#
# #Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}

# for c in placement:
#     if c not in d:
#         d[c] = 0
#     d[c] = d[c] + 1
# print(d)
#
# keys =d.keys()
# min_value = list(keys)[0]
# for k in d:
#     if d[k] < d[min_value]:
#         min_value = k
# print((min_value))

# Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
product = "iphone and android phones"
print(product.lower())
# lett_d = {}
# for char in product:
#     if char not in lett_d:
#         lett_d[char] = 0
#     lett_d[char] = lett_d[char] + 1
# print(lett_d)
# keys = list(lett_d.keys())
# print(keys)
# max_value = keys[0]
# print(max_value)
# for k in lett_d:
#     if lett_d[k] > lett_d[max_value]:
#         max_value = k
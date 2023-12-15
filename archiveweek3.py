# Create one conditional to find whether “false” is in string str1. If so, assign variable output the string “False.
# You aren’t you?”. Check to see if “true” is in string str1 and if it is then assign “True! You are you!” to the variable output.
# If neither are in str1, assign “Neither true nor false!” to output.
str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"

if "False" in str1:
    output = "False. You aren’t you?"
elif "true" in str1 :
    output = "True! You are you!"
else :
    output = "Neither true nor false!"

# Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched up the strings exactly.
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []

for percent in percent_rain:
    if percent > 90:
        resps.append('Bring an umbrella.')
    elif percent > 80:
        resps.append('Good for the flowers?')
    elif percent > 50:
        resps.append('Watch out for clouds!')
    else:
        resps.append('Nice day!')

print(resps)

# find a max value
nums = [9, 3, 8, 11, 5, 29, 2]
best_num = 0
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

# if finish by 'e', add 'd', else add 'ed'.
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
count = 0
for word in words:
    if word[-1] == 'e':
        past_tense.append(word + 'd')
    else:
        past_tense.append(word + "ed")
count += 1
print(past_tense)
# count rain greater than 3
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
count = 0
rain = rainfall_mi.split(",")
for r in range(len(rain)):
    n = float(rain[r])
    if n > 3:
        count += 1
#count number of 'w' in each element of items and sum them
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for string in items:
    if 'w' in string:
        acc_num += 1
#count number of words that starts and ends with the same letter, including one word letter.
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = 0
words = sentence.split(" ")
#if (sentence[0] and sentence[0])
print(words[6])
count = 0
for word in words:
    if (word[0] == word[-1]) or len(word) == 1:
        count += 1
print(count)

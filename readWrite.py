# #count number of char in a text file
with open("school_prompt2.txt", "r") as file:
    string = file.read()
num_char = 0
for char in string:
    num_char += 1
print(num_char)

#read number of lines

with open("travel_plans2.txt", "r") as file0:
    lines = file0.readlines()
num_lines = 0
for line in lines:
    num_lines += 1
print(num_lines)

# #code that return first 40 char of string
with open("emotion_words2.txt", "r") as file1:
    first_forty = file1.read(40)
print(len(first_forty) )

#code that return number of line
total = 0
with open("emotion_words.txt", "r") as emotion:
    lines = emotion.readlines()
print(len(lines) )

# #count number of word in a file
with open("emotion_words.txt", "r") as emotion:
    num_lines = emotion.read()
    words =num_lines.split()
    num_words = len(words)
print(num_words)

# assign third word to a list
with open("school_prompt2.txt","r") as school:
    lines = school.readlines()
    for line in lines:
        words = line.split()
print(lines)
print(words)

#Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017 about the S&P 500 closing prices as well as some other financial
# indicators, including the “Long Term Interest Rate”, which is interest rate paid on 10-year U.S. government bonds. Write a program that computes
# the average closing price (the second column, labeled SP500) and the highest long-term interest rate. Both should be computed only for the period
# from June 2016 through May 2017. Save the results in the variables mean_SP and max_interest.

# # The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# # Find the total number of characters in the file and save to the variable num.
# with open("travel_plans.txt", "r") as travel:
#     num = 0
#     file = travel.read()
#     for char in file:
#         num += 1
#
# #We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# # Find the total number of words in the file and assign this value to the variable num_words.
#
# with open("emotion_words.txt", "r") as emotion:
#     num_lines = emotion.read()
#     words =num_lines.split()
#     num_words = len(words)
# print(num_words)
#
# #Assign to the variable num_lines the number of lines in the file school_prompt.txt.
#
# # with open("school_prompt.txt","r") as school:
# #     lines = school.readlines()
# #     num_lines = 0
# #     for line in lines:
# #         num_lines  += 1
#
# #Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
# # with open("school_prompt.txt","r") as school:
# #     string = school.read(30)
# # beginning_chars = string
#
# #Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
#
# three = []
# with open("school_prompt.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         words = line.split()
#         three.append(words[2])
#
# # #Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
# # with open("emotion_words.txt", "r")as file:
# #     lines = file.readlines()
# #     emotions = []
# #     for line in lines:
# #         words = line.split()
# #         emotions.append(words[0])
#
# #Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
# # with open("travel_plans.txt", "r")as file:
# #     first_chars = file.read(33)

# #Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

with open("school_prompt.txt", "r") as file:
    lines = file.read()
    p_words = []
    words = lines.split()
    for i in range(len(words)):
        if "p" in words[i]:
            p_words.append(words[i])



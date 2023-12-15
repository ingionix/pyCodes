#first define function for removing unwanted char from the input string

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    for char in punctuation_chars:
        s = s.replace(char, "")
    return s

# second retrieve the number of positive words from the string

def strip_punctuation(s):
    for char in punctuation_chars:
        s = s.replace(char, "")
    return s


punctuation_chars = ["'", '"', ",", ".", ":", ";", '#', '@', "!"]
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(s1):
    num_pos_words = 0
    words = s1.split()
    for word in words:
        if strip_punctuation(word).lower() in positive_words:
            num_pos_words = num_pos_words + 1
    return num_pos_words
# third retrieve the number of negative words from the string
def strip_punctuation(s):
    for char in punctuation_chars:
        s = s.replace(char, "")
    return s

negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(s1):
    num_neg_words = 0
    words = s1.split()
    for word in words:
        if strip_punctuation(word).lower() in negative_words:
            num_neg_words = num_neg_words + 1
    return num_neg_words


# calling the functions and getting result

def strip_punctuation(s):
    for char in punctuation_chars:
        s = s.replace(char, "")
    return s.lower()  # Convert to lowercase after stripping punctuation

punctuation_chars = ["'", '"', ",", ".", ":", ";", '#', '@', "!"]

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(s1):
    num_pos_words = 0
    words = s1.split()
    for word in words:
        if strip_punctuation(word) in positive_words:
            num_pos_words += 1
    return num_pos_words

negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(s1):
    num_neg_words = 0
    words = s1.split()
    for word in words:
        if strip_punctuation(word) in negative_words:
            num_neg_words += 1
    return num_neg_words

def net_score(s1):
    return get_pos(s1) - get_neg(s1)

# Read the Twitter data file
with open("project_twitter_data.csv", "r") as tw:
    tw_text = tw.readlines()

# Write the results to a new CSV file
with open("resulting_data.csv", "w") as result:
    result.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    for line in tw_text[1:]:  # Skip the header row
        data = line.strip().split(',')  # Split the line into parts
        tweet_text = data[0]  # Extract the tweet text
        retweet_count = data[1]  # Extract the retweet count
        reply_count = data[2]  # Extract the reply count
        # Write the data to the file
        result.write(f"{retweet_count}, {reply_count}, {get_pos(tweet_text)}, {get_neg(tweet_text)}, {net_score(tweet_text)}\n")

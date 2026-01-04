# Program to read feedback.txt and count characters, lines and words

# initializing counters
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0
line_count = 0
word_count = 0

# opening the file in read mode
file = open("feedback.txt", "r")

# reading file line by line
for line in file:
    line_count = line_count + 1
    
    # splitting line into words
    words = line.split()
    word_count = word_count + len(words)
    
    # checking each character in the line
    for ch in line:
        if ch.isupper():
            upper_count = upper_count + 1
        elif ch.islower():
            lower_count = lower_count + 1
        elif ch.isdigit():
            digit_count = digit_count + 1
        elif ch != ' ' and ch != '\n':
            special_count = special_count + 1

# closing the file
file.close()

# displaying the results
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
print("Number of digits:", digit_count)
print("Number of special characters:", special_count)
print("Total number of lines:", line_count)
print("Total number of words:", word_count)

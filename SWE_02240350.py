###########################################
"https://github.com/namgaylhamo24/SWE_CAP1_Dzo_Spell_Checker.git"
#


#Namgay Lhamo
#SWE 'A'
#02240350 
#############################################
#REFERENCES
#-Chat GPT-https://openai.com/index/chatgpt/
#-W3 School-https://www.w3schools.com/
#-python Document-https://docs.python.org/3/
#-YouTube Videos-https://www.youtube.com/watch?v=LyymFN9t4kw&list=PPSV

##################################################
#SOLUTION
##################################################

# Read Input file
import requests

file_link = "https://csf101-server-cap1.onrender.com/get/input/350"
request_file = requests.get(file_link)

with open('350.txt', 'wb') as file:
    data = file.write(request_file.content)

print("Now procceding the : 350.txt")


# Claering the dictionary file
import re

def to_clean_dictionary(text):
    dzongkha_pattern = re.compile(r'[\u0F00-\u0FFF]+')
    return '\n'.join(dzongkha_pattern.findall(text))

input_txt = 'dictionary.txt'
dictionary = 'cleaned_dict.txt'

# Read from the input file
with open(input_txt, 'r', encoding='utf-8') as file:
    content = file.read()
 
# Filter the content to retain only Dzongkha characters
cleaned_dict = to_clean_dictionary(content)

# Create a new file and write the filtered content
with open(dictionary, 'w', encoding='utf-8') as file:
    file.write(cleaned_dict)

print("Filtered Dzongkha characters written to", dictionary)


# Check Spelling
def load_dictionary(dictionary_file):
    """Load dictionary words from a file into a set."""
    with open(dictionary_file, 'r', encoding='utf-8') as f:
        dictionary = set(word.strip() for word in f.readlines())
    return dictionary

def check_spelling(input_file, dictionary):
    """Check for misspelled words in the input file and track their positions."""
    misspelled_words_info = []  # To store misspelled word details

    with open(input_file, 'r', encoding='utf-8') as f:
        # Read line by line to track line numbers
        for line_num, line in enumerate(f, start=1):
            # Split the line into words (split by whitespace)
            words = line.split()

            # Check each word in the line
            for word_num, word in enumerate(words, start=1):
                if word not in dictionary:
                    # Collect misspelled word information: line number, word number, word itself
                    misspelled_words_info.append((line_num, word_num, word))

    return misspelled_words_info

def main(dictionary_file, input_file):
    # Load the dictionary
    dictionary = load_dictionary(dictionary_file)

    # Check for misspelled words
    misspelled_words = check_spelling(input_file, dictionary)

    if misspelled_words:
        print("Misspelled words found:")
        for line_num, word_num, word in misspelled_words:
            print(f"Line {line_num}, Word {word_num}: {word} is incorrect!")
    else:
        print("No misspelled words found!")

# Example usage
if __name__ == "__main__":
    # Replace with your actual file paths
    dictionary_file = 'cleaned_dict.txt'  # File with dictionary words
    input_file = '350.txt'            # File with text to check

    main(dictionary_file, input_file)



















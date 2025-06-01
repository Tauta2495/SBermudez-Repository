import math

kasiski_dictionary = {}
dictionary = {}
cyphered_text = ""
uncyphered_text = ""
most_used_letters = ['E', 'A', 'T', 'O', 'I', 'S', 'N', 'H', 'D', 'R',
'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X',
'Q', 'Z']
FILE_PATH = "/home/kali/Desktop/picoCTF/Cryptography/la_cifra_de/encrypted_text.txt"
letter_count = {}

def run_kasiski():

    global cyphered_text, kasiski_dictionary
    aux_letter = cyphered_text[0] 
    list_counter = []
    counter = 0

    


def organize_dictionary():

    global letter_count

    letter_count = dict(sorted(letter_count.items(), key = lambda item: item[1]))
    letter_count = {key: value for key,value in reversed(letter_count.items())}

def fill_dictionary():#fill the cyphered dictionary with all the equivalent letters

    global dictionary, letter_count, most_used_letters

    keys = letter_count.keys()

    dictionary = {key: value for key, value in zip(keys, most_used_letters)} 
    
def most_used_letter():
    # Create a dictionary to store letter frequencies
    global cyphered_text
    global letter_count
    # Convert the input string to lowercase to make it case-insensitive
    cyphered_text = cyphered_text.lower()

    # Iterate through the characters in the string
    for char in cyphered_text:
        # Ignore non-alphabetic characters
        if char.isalpha():
            # If the letter is not in the dictionary, add it with a count of 1
            if char not in letter_count:
                letter_count[char] = 1
            else:
                # If the letter is already in the dictionary, increment its count
                letter_count[char] += 1

def main():

    global cyphered_text, letter_count, most_used_letters, dictionary, uncyphered_text

    file = open(FILE_PATH, "r")
    cyphered_text = file.read()

    print (cyphered_text)

    most_used_letter()
    organize_dictionary()
    print(letter_count)
    fill_dictionary()
    #print(dictionary)

    run_kasiski()

    for i in cyphered_text:
        for key, value in dictionary.items():

            if i == key:
                uncyphered_text = uncyphered_text + value

            elif i == " ":

                uncyphered_text = uncyphered_text + " "

            

    #print(uncyphered_text)

    return 0

if __name__ == "__main__":
    main()
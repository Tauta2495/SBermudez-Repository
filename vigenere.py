import math

reference_dictionary = {'a':0, 'b':1, 'c':2, 'd':3 , 'e':4, 'f':5, 'g':6, 'h':7,
						'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
						'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21,
						'w':22, 'x':23, 'y':24, 'z':25}

#GLOBAL VARIABLES/////////////

cypher_text = ""
decyphered_text = ""
FILE_PATH = "/home/kali/Desktop/picoCTF/Cryptography/Vigenere/cipher.txt"
KEY = "CYLAB"

#GLOBAL VARIABLES/////////////

def get_key_from_value(value):
    for key, val in reference_dictionary.items():
        if val == value:
            return key
    return None

def key_minus_decyphered_text(k, c):

	result = reference_dictionary.get(c) - reference_dictionary.get(k)
	
	if result < 0:
		result = result%26
		
		return get_key_from_value(result)

	else:
		return get_key_from_value(result)

def decrypt():

	global cypher_text, KEY, decyphered_text, reference_dictionary
	cypher_text = cypher_text.lower()
	KEY = KEY.lower()
	aux_key = 0

	for char in cypher_text:
		if char.isalpha():
			decyphered_text = decyphered_text + key_minus_decyphered_text(KEY[aux_key], char)
			aux_key = aux_key + 1

		elif char == " ":
			decyphered_text = decyphered_text + char
			aux_key = aux_key + 1


		else:
			decyphered_text = decyphered_text + char
			

	print (decyphered_text)

def make_lenght_of_key_bigger():

	global KEY, cypher_text
	ORIGINAL_KEY = KEY
	aux = 0 
	
	for char in cypher_text:

		if char.isalpha():

			if aux > len(ORIGINAL_KEY) - 1:
				aux = 0
				KEY = KEY + KEY[aux]
				aux = aux + 1
			else:

				KEY = KEY + KEY[aux]
				aux = aux + 1

		elif char == " ":
			if aux > len(ORIGINAL_KEY) - 1:
				aux = 0
				KEY = KEY + KEY[aux]
				aux = aux + 1
			else:

				KEY = KEY + KEY[aux]
				aux = aux + 1

	KEY = KEY[:-len(ORIGINAL_KEY)]

	print(KEY, len(KEY)) 

def main():

	global cypher_text

	file = open(FILE_PATH, "r")
	cypher_text = file.read()
	cypher_text = cypher_text.replace(" ", "")

	print(cypher_text)
	make_lenght_of_key_bigger()
	decrypt()

	return 0


if __name__ == "__main__":
    main()
import math
import string

FENCE_GRID = []

FILE = "message.txt"
COLUMNS = 0 #number of characters in the message
ROWS = 0

def print_fence():
	for row in FENCE_GRID:
		print (row)


def initialize_grid(c,r):
	
	for rows in range(r):
		FENCE_GRID.append([])


	for rows in FENCE_GRID:
		for i in range(c):
			rows.append('*')

	return 0

def padding(m, c, r):#c being columns and m message and r rows

	while ((c % (2 * (r - 1))) != 0):
		print("NEEDS PADDING")
		m = m + '-'
		c = c + 1
	
	return m, c

def fill_2d_array(r, m):#c being columns and m message

	#remember that k = l / (2(N - 1)) if and only
	#k = len(m) / (2 * (r - 1))
	#print ("Number of characters in the first and last line: ", k)
	#print ("Number of characters in the middle lines: ", 2 * k)

	#Remember that if you get decimals on k and 2k, that means that you need to
	#work with the whole numbers closest to the decimal you got. 1 unit up and down
	#Always use the biggest one first for the row that comes first

	#for i in FENCE_GRID 

	return 0


def main():
	f = open(FILE, 'r')
	message = f.read()

	ROWS = int(input("How many rows does the grid have?"))
	print("Input succesful")

	print(message)

	COLUMNS = len(message)
	print("Number of characters in string: ", COLUMNS)
	
	
	#message, COLUMNS = padding(message, COLUMNS, ROWS)
	#print("New Message: ", message)
	#print("Number of characters in padded string: ", COLUMNS)

	initialize_grid(COLUMNS,ROWS)
	print_fence()
	#fill_2d_array(ROWS,message)

main ()
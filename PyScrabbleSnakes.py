#    Name: PyScrabbleSnakes.py
#  Author: Justin L.  Brown
# Purpose: Generate a list of Scrabble(TM) words whose successive substrings
#          after removing the leading letter are also valid words
#          (down to three letters).
#   Notes: twl06.txt is available from
#          https://www.wordgamedictionary.com/twl06/
import argparse

# Command-line arguments
parser = argparse.ArgumentParser(description='Find some Scrabble snakes.')
parser.add_argument('wordlist',help='path to a word list file')
parser.add_argument('scrabblesnakes',help='path to the output file')
args = parser.parse_args()

# "Someone take this bag of snakes and lay them out straight."
# - Dan Aykroyd, Evolution, 2001.
def main():
	# Initialize a set of 3+ letter words from a word list.
	words = set()
	with open(args.wordlist, "r") as file:
		for word in file:
			if len(word.strip()) >= 3:
				words.add(word)

	# Put all the living snakes into a bag.
	bag = []
	for snake in words:
		if isSnakeAlive(snake, words):
			bag.append(snake)

	# Sort the snakes by length and then alphabetically, and then lay them out
	# straight in a text file.
	bag.sort(key=lambda snake: (-len(snake), snake))
	with open(args.scrabblesnakes, "w") as file:
		file.writelines(bag)

def isSnakeAlive(snake, words):
	# A living snake is itself a word, and
		# it is three letters long, or
		# if cutting off its tail (the left-most letter) leaves another living
		# snake.
	if snake not in words:
		return False
	elif len(snake.strip()) == 3:
		return True
	else:
		return isSnakeAlive(snake[1:], words)

if __name__ == "__main__":
	main()
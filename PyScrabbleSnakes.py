# Parse command-line arguments.
import argparse
parser = argparse.ArgumentParser(description='Find some Scrabble snakes.')
parser.add_argument('wordlist',help='path to a word list file')
parser.add_argument('scrabblesnakes',help='path to the output file')
args = parser.parse_args()

# "Someone take this bag of snakes and lay them out straight."
# - Dan Aykroyd, Evolution, 2001.
def main():
    # Initialize a collection of 3+ letter words from a word list.
    snakes = set()
    with open(args.wordlist, "r") as file:
        for word in file:
            if len(word.rstrip()) >= 3:
                snakes.add(word.rstrip())

    # Put all the living snakes into a bag.
    bag = []
    for snake in snakes:
        if isSnakeAlive(snake, snakes):
            bag.append(snake)

	# Sort the snakes in the bag by length and then alphabetically,
	# and then lay them out straight in a text file.
    bag.sort(key=lambda snake: (-len(snake), snake))
    with open(args.scrabblesnakes, "w") as file:
        file.writelines(snake + '\n' for snake in bag)

def isSnakeAlive(snake, snakes):
	# A living snake is itself a word, and
		# it is three letters long, or
		# if cutting off its tail (the left-most letter) leaves a living snake.
	if snake not in snakes:
		return False
	elif len(snake) == 3:
		return True
	else:
		return isSnakeAlive(snake[1:], snakes)

if __name__ == "__main__":
    main()
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
    snakes = {}
    with open(args.wordlist, "r") as file:
        for word in file:
            if len(word.strip()) >= 3:
                snakes[word] = None

    # Check every snake for life.
    for key in list(snakes):
        if snakes[key] is None:
            snakes[key] = isSnakeAlive(key, snakes)

    # Put all the living snakes into a bag.
    bag = list({snake:isAlive for snake,isAlive in snakes.items() if isAlive == True})

    # Sort the snakes in the bag by length and then alphabetically,
    # and then lay them out straight in a text file.
    bag.sort(key=lambda snake: (-len(snake), snake))
    with open(args.scrabblesnakes, "w") as file:
        file.writelines(bag)

def isSnakeAlive(snake, snakes):
    # The snake must be a word to be alive.
    if snake not in snakes.keys():
        return False
    # Check a snake for life at most once.
    elif snakes.get(snake) is None:    
        # A snake is alive if it is three letters long.
        if len(snake.strip()) == 3:
            snakes[snake] = True
        # A snake is alive if cutting off its tail leaves a living snake.
        else:
            snakes[snake] = isSnakeAlive(snake[1:], snakes)
    # Return the result of checking the snake for life.
    return snakes[snake]

if __name__ == "__main__":
    main()
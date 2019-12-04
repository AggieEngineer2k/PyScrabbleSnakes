# PyScrabbleSnakes
> Take any three letter word. Add a letter to the left side to make another word. Keep doing this and see how big of a word you can make.

Searches for the words that are solutions to the challenge.

## Installation

Download any word list text file, with one word per line.

###### TWL06

 _twl06.txt_ is available from https://www.wordgamedictionary.com/twl06/.

## Usage Examples

```sh
C:\> py PyScrabbleSnakes.py -h
usage: PyScrabbleSnakes.py [-h] wordlist scrabblesnakes

Find some Scrabble snakes.

positional arguments:
  wordlist        path to a word list file
  scrabblesnakes  path to the output file

optional arguments:
  -h, --help      show this help message and exit
```

```sh
C:\> py PyScrabbleSnakes.py "c:/temp/twl06.txt" "c:/temp/scrabblesnakes.txt"
```

## Release History

* 0.1.0
    * Snakes are checked for life at most once.
* 0.0.1
    * Work in progress
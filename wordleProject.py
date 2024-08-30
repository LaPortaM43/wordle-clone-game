# Wordle_Game_Lab.py
# Daniel Gonzalez, s1345078
# Matthew LaPorta, s1359142
# Ivan Martinez Agurto, s1320639
# Alexander Metz, s1358598

# Fix out of place so that letters stay there until its correct 
import random

import sys

# Function to validate guess returns false if guess is not in the word list
def isValid(guessedWord, wordList):  #function checks if word is valid
  valid = False

  for word in wordList: 
    if guessedWord == word.rstrip():
      valid = True
      break

  if valid:
    return valid
  else:
    print("Invalid guess")
    return valid

  
# Function to check if the letter is in the correct spot
# returns "$ " if it is and "" if it is not
def correctPosition(letter, index, randomWord):
  if letter == randomWord[index]:
    return '$ '

  return ''


# Function to check if the letter is in the wrong place
# returns "> " if it is and "" if it is not
def wrongPosition(letter, index, randomWord):
  for l in range(5):
    if letter == randomWord[l] and index != l:
      return '> '
  return ''

# Prints the the correct, wrongPlace, and notInWord lists 
def displayLetters(correct, wrongPlace, notInWord):

  print('Correct: ', end='')

  for i in range(len(correct)):
    print(f'{correct[i].upper()} ', end='')
  print()

  print('Out of place: ', end='')

  for i in range(len(wrongPlace)):
    print(f'{wrongPlace[i].upper()} ', end='')

  print('\nNot in word: ', end='')

  for i in range(len(notInWord)):
    print(f'{notInWord[i].upper()} ', end='')

  print('\n**********************************************************')
  print()

# Returns the summary of all guesses
def getSummary(hints):

  summary = '\n**********************************************************\n'
  summary += 'Summary:\n\n'
  for hint in hints:
    summary += hint + '\n'

  return summary

def main():
  # open file
  try:
    file = open('five_letter_eldrow_words.txt', 'r')
  except FileNotFoundError:
    print('Input file not found. Could there be a different file name?')
    sys.exit(1)

  # Skips the first four lines in word list to skip comments
  for i in range(4):
    file.readline()
    
  # create word list and get random word
  wordList = file.readlines()
  randomWord = random.choice(wordList).rstrip()
  # print(randomWord)

  count = 0
  win = False
  hints = []
  #correct = []
  notInWord = []
  wrongPlace = []

  print("Welcome to Wordle. Get 6 chances to guess a 5-letter word.")
  print()
  print('**********************************************************')
  print()

  while count < 6:
    # get the guess
    count += 1

    guessedWord = input(f"Enter guess #{count}: ")

    # check to see if guess is valid if not ask user for another guess
    while not isValid(guessedWord, wordList):
      guessedWord = input("Enter another guess: ")

    index = 0
    hint = ""
    correct = []
    #wrongPlace = []
    print()

    for letter in guessedWord:

      result = correctPosition(letter, index, randomWord)
      # if letter is in the correct position then add to correct list if not already       # there and symbol to hint
      if result == '$ ':
        hint += result
        if letter not in correct:
          correct.append(letter)
          correct.sort()
          if letter in wrongPlace:
            wrongPlace.remove(letter)
        index += 1
        continue
      # if letter is not in the right spot the add to wrongPosition if not already         # there and symbol to hint
      result = wrongPosition(letter, index, randomWord)
      if result == '> ':
        hint += result
        if letter not in wrongPlace:
          wrongPlace.append(letter)
          wrongPlace.sort()
        index += 1
        continue
      # if letter is not in word then add to notInWord if not already there and            # symbol to hint
      hint += 'x '
      if letter not in notInWord:
        notInWord.append(letter)
        notInWord.sort()
      index += 1

    print(hint)
    for i in range(5):
      print(f'{guessedWord[i].upper()} ', end='')

    hints.append(hint)

    print()

    # for letter in guessedWord:
    if guessedWord == randomWord:
      win = True
      break

    print()
    displayLetters(correct, wrongPlace, notInWord)

  if win:

    print()
    print(getSummary(hints))

  else:
    print("You lose")
    print()
    print(getSummary(hints))
    print(randomWord)

  file.close()

main()

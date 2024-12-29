import os
import random

# Define colors
# It is possible that for different Operating Systems different methods are needed for colors. This method should be supported by Linux.
class bcolors:
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[33m'
    ENDC = '\033[0m'

def print_wordles(correct_word, tried_combinations, allowed_guesses):
    # go through all possible allowed guesses
    for i in range(0,allowed_guesses):
        # if i is larger than the length of tried combinations, we print underscores for left guesses; otherwise we will print the letters with colors.
        if i >= len(tried_combinations):
            print("_ _ _ _ _")
        else:
            # this will collect the different letters with its colors 
            output_word = ""
            
            # go through all letters of a guess
            for x in range(0,5):
                # first check if letter is at correct place
                if correct_word[x] == tried_combinations[i][x]:
                    output_word += bcolors.OKGREEN + tried_combinations[i][x] + bcolors.ENDC + " "
                # second check if letter is in word but at wrong place
                elif tried_combinations[i][x] in correct_word:
                    output_word += bcolors.OKYELLOW + tried_combinations[i][x] + bcolors.ENDC + " "
                # third add letter if not in word
                else:
                    output_word += tried_combinations[i][x] + " "
            
            # print collected letters
            print(output_word)
    print("\n#################")
    

def start_game(word, allowed_guesses):
    tried_combinations = []
    invalid = False
    while True:
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print words
        print_wordles(word, tried_combinations, allowed_guesses)

        # Check if last entered word was correct
        if len(tried_combinations) != 0 and word == tried_combinations[len(tried_combinations) - 1]:
            print("Yay - you won!\nThe Word was", word)
            return
        
        if len(tried_combinations) >= allowed_guesses:
            print("Tries exhausted - better luck next time!\nThe word was", word)
            return

        # If try was invalid we choose a different text
        if invalid:
            text = "Guess invalid - only five letter tries allowed!\nInput a guess:\n"
            invalid = False
        else:
            text = "Input a guess:\n"

        # Get word from user with input text
        input_word = input(text)

        # Do input validation
        if len(input_word) != 5:           
            invalid = True
            continue

        # Add guess to list of guesses
        tried_combinations.append(input_word)

def get_word():
    # Can be extended to have a larger list or download one from the internet
    return random.choice(["Hello", "World"])

def main():
    # Get a random word
    word = get_word()

    # Start the game with the random word and allowed_guesses
    start_game(word, 6)

if __name__ == "__main__":
    main()
import random
#Hangman game!

#Function that returns a list of the indices of word in which the guess occur.
def findOccurrences(secret_word, guess):
    return [index for index, letter in enumerate(secret_word) if letter == guess]

# Define a list of words
word_list = ['pizza', 'skola', 'chimpans', 'flaggstång', 'hustak', 'motorbåt']

# Let computer choose a random word from the list
secret_word = random.choice(word_list)

# Welcome player to the game
print('Välkommen till spelet Hangman! Du vinner spelet genom att gissa vilket ord som datorn har valt.\nVid 10 felaktiga gissningar så förlorar du.')

# Define and print player list of the same length as the secret word
player_list = []
for element in secret_word:
    player_list.append('_')
print(player_list)

# Define a counter that will exit the game of number of faulty guesses reaches 10.
nbr_guesses = 0

while nbr_guesses < 10:
    # Take a character guess from the player
    guess = input('Gissa på en bokstav: ')

    # See if the character exists in the secret word. If yes, add it to the player list and print the list.
    if guess in secret_word:
        print('Bokstaven finns i ordet!')
        positions = findOccurrences(secret_word, guess)
        for i in positions:
            player_list[i] = guess
        print(player_list)

        # If no empty slots left in the player list, the player has won the game!
        if '_' not in player_list:
            print(f'Grattis! Du har vunnit!')
            exit()
    else:
        print('Bokstaven finns INTE i ordet.')
        nbr_guesses += 1
        print(f'Antal felaktiga gissningar: {nbr_guesses}')

print('Du har förlorat!')
exit()
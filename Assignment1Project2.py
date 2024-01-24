import random
import string

# Memory spel!

# Generera lista av angiven längd med slumpmässiga bokstäver.
def generate_list(nbr_char):
    char_list = []
    for i in range(0,nbr_char):
        char_list.append(random.choice(string.ascii_letters).lower())
    return char_list

# Tar en list som input och returnerar en lista med samma element men i en annan ordning.
def shuffle_list(list):
    shuffled_list = list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

# Datorn väljer ett antal slumpmässiga siffror eller bokstäver (beroende på svårighetsgrad) och visar dem i en viss ordning.

print(f'\nVälkommen, nu spelar vi memory!')
print('Du kommer få se en lista med bokstäver, därefter kastas bokstäverna om och din uppgift är att ange deras ursprungliga ordning.')
level = input('Välj svårighetsgrad genom att skriva lätt, medel eller svår:')
level = level.lower()

if level == 'lätt':
    nbr_char = 3
    correct_list = generate_list(nbr_char)
elif level == 'medel':
    nbr_char = 5
    correct_list = generate_list(nbr_char)
elif level == 'svår':
    nbr_char = 7
    correct_list = generate_list(nbr_char)
else:
    print('Du har angivet ett ogiltigt värde. Svårighetsgrad sätts automatiskt till lätt.')
    nbr_char = 3
    correct_list = generate_list(nbr_char)

print(f'\n{correct_list}\n')
ready = input('Har du memorerat bokstävernas ordning i listan? Skriv ok och tryck enter när du är redo:')

# Sedan visar datorn samma siffror eller bokstäver igen, men denna gång blandat.
shuffled_list = shuffle_list(correct_list)
print('\n' * 100)
print(f'{shuffled_list}\n')

# Spelaren ska gissa i vilken ordning siffrorna eller bokstäverna visades första gången.
# Spelet fortsätter tills spelaren har gissat rätt ordning.
counter = 0
print('Skriv ovanstående bokstäver i rätt ordning, ange en bokstav i taget och tryck enter.')
while counter < nbr_char:
    guess = input('Ange en bokstav:').lower()
    if correct_list[counter] == guess:
        print(f'Korrekt! Bokstaven på plats {counter+1} av {nbr_char} är {guess}.')
        counter = counter + 1
    else:
        print(f'Fel! Fortsätt med en ny gissning.')

print(f'\nGRATTIS! Du satte ihop denna korrekta lista och klarade spelet: {correct_list}.')

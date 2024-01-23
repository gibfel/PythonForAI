import random

# Program för att spela Sten-Sax-Påse

choice_list = ['sten', 'sax', 'påse']
game_on = True
print(f'Välkommen till spelet Sten-Sax-Påse!')

while game_on == True:

    bot_choice = random.choice(choice_list)
    user_choice = input('Välj mellan sten, sax eller påse:')
    print(f'Du spelade {user_choice} och datorn spelade {bot_choice}.')

    if user_choice == bot_choice:
        print(f'Ni valde samma. Spela igen.')

    elif (user_choice == 'sten' and bot_choice == 'sax') or (user_choice == 'sax' and bot_choice == 'påse') or (user_choice == 'påse' and bot_choice == 'sten'):
        print(f'Grattis du vann!\nSpelet avslutas.')
        game_on = False

    else:
        print(f'Du förlorade.\nSpelet avslutas.')
        game_on = False

exit()
import random
import string

def get_words():
    with open('words.txt') as file:
        words = [word.strip() for word in file.readlines()]
    return words

def mess_words(player_word, word, letter):
    for i, let in enumerate(word):
        if let == letter:
            player_word[i] = letter
    return player_word

while True:
    chose = input('Do you want to play? (y/n)')
    if chose == 'y':
        solved = False
        attempts = 3
        letters = list(string.ascii_lowercase)
        word = random.choice(get_words())
        player_word = ['_'] * len(word)
        while attempts > 0:
            letter = input((f'Word:{" ".join(player_word)}. \n' \
                f'You have {attempts} attempts left. ' \
                f'Choose your letter: {"".join(letters)}?'))
            
            if letter not in letters:
                print("There is no such letter in list!")
                continue
            
            if letter not in word:
                print('Wrong letter!')
                attempts -= 1
                letters.remove(letter)
                continue
            else:
                letters.remove(letter)
                player_word = mess_words(player_word, word, letter)
                if player_word == word:
                    solved = True
                    break
        if solved:
            print('Congratulation! You won!')
        else:
            print('Sorry. You lost!')
        print(f'The right word is {word}')
    elif chose == 'n':
        break
    else:
        print('Uncorrect input!')

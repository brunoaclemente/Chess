from Bruno_Project.lib import *

men = ['Encoder', 'Decoder', 'Logout']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# lzahch whyhkh jvt v zlb uvcv jhsklpyhv
# uhv lzahylp lt jhzh
# vsh jvtv chp cvjl
# gym rmyuxum
# lt bth ilsh uvpal kl thuoh
# al'k fgl s yggvtqw. al'k s kww qgm dslwj

while True:
    option = menu(men)
    if option == 1:
        text = readStr('Text: ').lower()
        key = readStr('Key: ').lower()
        while len(key) != 1:
            print('Write ONLY one letter for the key')
            key = readStr('Key: ').lower()

        encoded_text = []

        for word in text:
            for letter in word:
                if letter not in alphabet:
                    encoded_text.append(letter)
                elif letter in alphabet:
                    number = alphabet.index(letter) + alphabet.index(key)
                    if number > 25:
                        number -= 26
                    new_letter = alphabet[number]
                    encoded_text.append(new_letter)
        encoded_text = ''.join(encoded_text)
        print()
        print(color(encoded_text.capitalize()))
        print()
        print()
    elif option == 2:
        text = readStr('Text: ').lower()
        f = frequency(text)
        keys = []
        decoded_texts = []
        position = 0
        for letter in f:
            keys.append(letter[1])
        for key in keys:
            alphabet2 = [key]
            for c in range(1, 26):
                nl = alphabet.index(key) + c
                if nl > 25:
                    nl -= 26
                alphabet2.append(alphabet[nl])
            list_of_text = list(text)
            decoded_text = []
            for letter in list_of_text:
                if letter in alphabet:
                    decoded_text.append(alphabet[alphabet2.index(letter)])
                else:
                    decoded_text.append(letter)
            decoded_text = ''.join(decoded_text)
            decoded_text = decoded_text.split()
            correct_words = 0
            for word in decoded_text:
                if checker('salas.txt', word):
                    correct_words += 1

            decoded_text = ' '.join(decoded_text)
            decoded_texts.append([correct_words, decoded_text, key])
        decoded_texts.sort(reverse=True)
        while True:
            print()
            print(f'Text: {color(decoded_texts[position][1].capitalize())}')
            print(f'Key: {color(decoded_texts[position][2].upper(), "green")}')
            print()
            question = readStr('is that right? [Y/N] ').lower()
            while question not in 'yn':
                print('write Y for yes or N for no')
                question = readStr('is that right? [Y/N] ').lower()

            if question == 'y':
                print()
                decoded_text = decoded_texts[position][1].split()
                for word in decoded_text:
                    if not checker('salas.txt', word):
                        access('salas.txt', word)
                print('New registered words')
                break
            else:
                position += 1
            if position > 25:
                print()
                print(color('Those were all the solutions, I think it should not it be a cesar cipher', 'blue'))
                break
    elif option == 3:
        header('Logging out of the system... cya!')
        sleep(0.5)
        break

# Dictionary representing the morse code chart
from email.errors import MessageError


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return f"Your Encrypted Morse Code is : {cipher}"


def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys()
                                 )[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher


def main():
    choice = int(input("1.Words to Morse Code \n2.Morse Code to Words\n"))
    if choice == 1:
        message = input("Type your message here:  normal text:\n")
        result = encrypt(message.upper())
        print(result)
    elif choice == 2:
        message = input(
            "Type your message here:Morse code using '.', '-' or '_',separating letters by spaces:\n")
        result = decrypt(message)
        print(result)
    else:
        print('Invalid choice!\nPlease Enter a valid Choice number.\n1.Words to Morse Code \n2.Morse Code to Words"')


if __name__ == '__main__':
    main()

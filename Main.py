def decryptMorseCharacter(morseCharacter):
    chr = ""
    if morseCharacter == '._':
        chr = 'A'
    elif morseCharacter == '_...':
        chr = 'B'
    elif morseCharacter == '_._.':
        chr = 'C'
    elif morseCharacter == '_..':
        chr = 'D'
    elif morseCharacter == '.':
        chr = 'E'
    elif morseCharacter == '.._.':
        chr = 'F'
    elif morseCharacter == '__.':
        chr = 'G'
    elif morseCharacter == '....':
        chr = 'H'
    elif morseCharacter == '..':
        chr = 'I'
    elif morseCharacter == '.___':
        chr = 'J'
    elif morseCharacter == '_._':
        chr = 'K'
    elif morseCharacter == '._..':
        chr = 'L'
    elif morseCharacter == '__':
        chr = 'M'
    elif morseCharacter == '_.':
        chr = 'N'
    elif morseCharacter == '___':
        chr = 'O'
    elif morseCharacter == '.__.':
        chr = 'P'
    elif morseCharacter == '__._':
        chr = 'Q'
    elif morseCharacter == '._.':
        chr = 'R'
    elif morseCharacter == '...':
        chr = 'S'
    elif morseCharacter == '_':
        chr = 'T'
    elif morseCharacter == '.._':
        chr = 'U'
    elif morseCharacter == '..._':
        chr = 'V'
    elif morseCharacter == '.__':
        chr = 'W'
    elif morseCharacter == '_.._':
        chr = 'X'
    elif morseCharacter == '_.__':
        chr = 'Y'
    elif morseCharacter == '__..':
        chr = 'Z'
    return chr

def encryptCharacter(character):
    morse=""
    if character == 'A' or character == 'a':
        morse = '._'
    elif character == 'B' or character == 'b':
        morse = '_...'
    elif character == 'C' or character =='c':
        morse = '_._.'
    elif character == 'D' or character =='d':
        morse = '_..'
    elif character == 'E' or character =='e':
        morse = '.'
    elif character == 'F' or character =='f':
        morse = '.._.'
    elif character == 'G' or character =='g':
        morse = '__.'
    elif character == 'H' or character =='h':
        morse = '....'
    elif character == 'I' or character =='i':
        morse = '..'
    elif character == 'J' or character =='j':
        morse = '.___'
    elif character == 'K' or character =='k':
        morse = '_._'
    elif character == 'L' or character =='l':
        morse = '._..'
    elif character == 'M' or character =='m':
        morse = '__'
    elif character == 'N' or character =='n':
        morse = '_.'
    elif character == 'O' or character =='o':
        morse = '___'
    elif character == 'P'  or character =='p':
        morse = '.__.'
    elif character == 'Q' or character =='q':
        morse = '__._'
    elif character == 'R' or character =='r':
        morse = '._.'
    elif character == 'S' or character =='s':
        morse = '...'
    elif character == 'T' or character =='t':
        morse = '_'
    elif character == 'U' or character =='u':
        morse = '.._'
    elif character == 'V' or character =='v':
        morse = '..._'
    elif character == 'W' or character =='w':
        morse = '.__'
    elif character == 'X' or character =='x':
        morse = '_.._'
    elif character == 'Y' or character =='y':
        morse = '_.__'
    elif character == 'Z' or character =='z':
        morse = '__..'
    return morse
def decryptSentence(morseString):
    morse_character = ""
    sentence= ""
    for i in range(len(morseString)):
        if morseString[i] == " ":
            sentence += decryptMorseCharacter(morse_character)
            morse_character = ""
            if morseString[i + 1] == " ":
                sentence+= " "
                i+=1                    #increment value because do not take " " again
        else:
            morse_character+=morseString[i]
    sentence+=decryptMorseCharacter(morse_character)
    return sentence
def encryptSentence(inputString):
    morseString = ""
    for i in range(len(inputString)):
        if inputString[i] == " ":
            morseString = morseString + "  "
        morseString = morseString + " " + encryptCharacter(inputString[i])
    return morseString

while(True):
    print("1 Encryption")
    print("2 Decryption")
    print("3 Exit")
    choice=int(input("enter the choice:"))
    if choice == 1:
        input_string_encrypt = input("enter the input for encryption:")
        encrypt=encryptSentence(input_string_encrypt)
        print("encrypted string:", encrypt)
    elif choice == 2:
        input_string_decrypt = input("enter the input for decryption:")
        decrypt=decryptSentence(input_string_decrypt)
        print("decrypted string:",decrypt)
    elif choice == 3:
        break
    else:
        print("Invalid choice!")





#hangman
import getpass

word = getpass.getpass(prompt = 'Type hidden word: ')      #str(input("Type hidden word: "))
word_list = list(word)

# either ask for how many attempts, or just keep count or both
tries = int(input("Number of wrong guesses allowed: "))
print('\n')

#replace letters with *
asterisk_word = ''
word_length = len(word)
for i in range(word_length):
    asterisk_word += '*'

#making the asterisk_word into a list
ast_word_list = list(asterisk_word)

#function for turning lists into strings
def ListtoStringWComma(lst):
    new_str = ''
    for i in lst:
        new_str += i + ' '
    return new_str
def ListtoString(lst):
    new_str = ''
    for i in lst:
        new_str += i
    return new_str

#ask for a letter and save it in a list
used_letters = []

if '*' in ast_word_list:
    while '*' in ast_word_list:
        ins_letter = str(input("Type a single letter: "))
        if ins_letter == 'exit':
            break
        used_letters.append(ins_letter)
        print('letters used:', ListtoStringWComma(used_letters), '\n')  #, ' | ', 'Attempts:', len(used_letters), '\n')


#checking if ins_letter is in hidden word, and where it is
        pos = [position for position, letter in enumerate(word) if letter == ins_letter]
        if len(pos) == 0:
            tries = tries - 1
            print("Letter not in hidden word. Wrong guesses left:", tries, '\n')
            if tries == 0:
                print(ListtoString(ast_word_list),'\n'+'You lost! The hidden word was:', word+'.', '\n')
                break

        elif len(pos) >= 1:
            print("Correct letter!")
            for i in pos:
                num_index = int(i)
                if word_list[num_index] == ins_letter:
                    ast_word_list[num_index] = ins_letter
        print(ListtoString(ast_word_list), '\n', '\n')

if '*' not in ast_word_list:
    print('Congratulations! The hidden word was',word+'.', '\n')

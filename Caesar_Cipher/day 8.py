import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text,shift): ##alternative approach
    cipher_text = ""
    for each_letter in text:

        letter_position = alphabet.index(each_letter)
        new_position = letter_position + shift

        if new_position > 25:
            new_position = new_position - 25 - 1

        cipher_text += alphabet[new_position]
    print(f"the encrypted text is {cipher_text} ")
    print("\n")
def decrypt(text,shift):
    decipher_text = ""

    for each_letter in text:
        letter_position = alphabet.index(each_letter)
        new_position = letter_position - shift

        decipher_text += alphabet[new_position]
    print(f"the decrypted message is {decipher_text}")
    print("\n")


def caesar(starting_text,shift_amount,cipher_direction):    ##combined encrypt and decrypt into a single function
    end_text = ""
    if cipher_direction == "decode":
        shift_amount = shift_amount *-1

    for letter in starting_text:
        if letter not in alphabet:
            end_text += letter

        elif letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
        
            if new_position > 25: ##accounts for the looping for 1 round.
                new_position = new_position % 26 ##this modulo effectively accounts for looping one round

            end_text += alphabet[new_position]

    print(f"your {cipher_direction}d message is {end_text}")

def encrypt1(text,shift):
    list = []
    en_list = []
    for each_letter in text: ##change all alphabats to its number index equivalent,stores in a list
        list.append(alphabet.index(each_letter))
    
    for each_letter in list: ##apply arithemtic shifting to the numbers index
        en_list.append(int(each_letter) + shift)
    
    print("Your encrypted message is: ")
    for i in en_list:
        print(alphabet[i],end="")

    print("\n")
def decrypt1(text,shift):
    list = []
    en_list = []
    for each_letter in text:
        en_list.append(each_letter)
    for each_letter in en_list:
        list.append(alphabet.index(each_letter))
    for i in list:
        print(alphabet[i - shift],end="")


print(art.logo)

go_again = True

while go_again :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Type your message:\n").lower()
    input_shift = int(input("Type the shift number:\n"))
    
    caesar(input_text,input_shift,direction)
    user_input = input("type 'yes' to go again, and 'no' to quit ")
    if "yes" in user_input:
        go_again = True
    elif "no" in user_input:
        go_again = False
import random 

# importing time modeuldes
import time 

print("Welcome to Encryption and Decryption App")
time.sleep(2)

alphabet = []

# run again function
def play_again():
    play_it_again = input("Want to run again ").lower()
    if play_it_again == 'y':
        play_again()
    elif play_it_again == 'n':
        print("Thank you for playing")
        exit()
    while play_it_again not in ['Y', 'YES', 'N', 'NO', 'y','yes', 'n', 'no']:
        print("Invalid input")
        play_again()


def caeser_secret():

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
    "o","p","q","r","s","t","u","v","w","x","y","z"]
    direction = input("Enter encode to encrpt or decode to decrypt ").lower()

    if direction == "encode":
        text = input("Enter the message to encrypt ")
        shift = int(input("Enter the shift amount "))
        def encrypt(plain_text, shift_amount):
            cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = (position + shift_amount) % 26
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            print(f"Your encrypted message is {cipher_text}")
            play_again()

        encrypt(plain_text=text, shift_amount=shift)

    elif direction == "decode":
        text =  input("Enter the message to decrypt ")
        shift = int(input("Enter the shift amount "))
        def decrypt(plain_text, shift_amount):
            decrypted_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = ( position - shift_amount ) % 26
                new_letter = alphabet[new_position]
                decrypted_text += new_letter
            print(f"Your encoded message is {decrypted_text}")
            play_again()

        decrypt(plain_text=text, shift_amount=shift)

    else:
        print("Invalid input")
    

caeser_secret()



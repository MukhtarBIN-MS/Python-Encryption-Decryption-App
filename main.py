# import random 

# # importing time modeuldes
# import time 

# print("Welcome to Encryption and Decryption App")
# time.sleep(2)

# alphabet = []

# # run again function
# def play_again():
#     play_it_again = input("Want to run again ").lower()
#     if play_it_again == 'y':
#         play_again()
#     elif play_it_again == 'n':
#         print("Thank you for playing")
#         exit()
#     while play_it_again not in ['Y', 'YES', 'N', 'NO', 'y','yes', 'n', 'no']:
#         print("Invalid input")
#         play_again()


# def caeser_secret():

#     alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
#     "o","p","q","r","s","t","u","v","w","x","y","z"]
#     direction = input("Enter encode to encrpt or decode to decrypt ").lower()

#     if direction == "encode":
#         text = input("Enter the message to encrypt ")
#         shift = int(input("Enter the shift amount "))
#         def encrypt(plain_text, shift_amount):
#             cipher_text = ""
#             for letter in plain_text:
#                 position = alphabet.index(letter)
#                 new_position = (position + shift_amount) % 26
#                 new_letter = alphabet[new_position]
#                 cipher_text += new_letter
#             print(f"Your encrypted message is {cipher_text}")
#             play_again()

#         encrypt(plain_text=text, shift_amount=shift)

#     elif direction == "decode":
#         text =  input("Enter the message to decrypt ")
#         shift = int(input("Enter the shift amount "))
#         def decrypt(plain_text, shift_amount):
#             decrypted_text = ""
#             for letter in plain_text:
#                 position = alphabet.index(letter)
#                 new_position = ( position - shift_amount ) % 26
#                 new_letter = alphabet[new_position]
#                 decrypted_text += new_letter
#             print(f"Your encoded message is {decrypted_text}")
#             play_again()

#         decrypt(plain_text=text, shift_amount=shift)

#     else:
#         print("Invalid input")
    

# caeser_secret()

import time

def print_slow(msg, delay=0.05):
    """
    Prints a message character by character with a delay.

    Parameters:
        msg (str): The message to print.
        delay (float): The delay between printing each character.
    """
    for char in msg:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def play_again():
    """
    Asks the user if they want to play again.
    """
    while True:
        play_it_again = input("Do you want to run again? (Y/N): ").lower()
        if play_it_again in ['y', 'yes']:
            return True
        elif play_it_again in ['n', 'no']:
            print("Thank you for playing!")
            return False
        else:
            print("Invalid input. Please enter Y or N.")

def caesar_cipher(direction):
    """
    Encrypts or decrypts a message using the Caesar Cipher.

    Parameters:
        direction (str): 'encode' for encryption, 'decode' for decryption.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = input(f"Enter the message to {direction}: ").lower()
    shift = int(input("Enter the shift amount: "))

    result = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encode":
                new_index = (index + shift) % 26
            elif direction == "decode":
                new_index = (index - shift) % 26
            result += alphabet[new_index]
        else:
            result += letter  # Keep non-alphabetic characters unchanged

    print(f"Your {direction}d message is: {result}")

def main():
    print_slow("Welcome to the Encryption and Decryption App")
    while True:
        direction = input("Enter 'encode' to encrypt or 'decode' to decrypt: ").lower()
        if direction in ['encode', 'decode']:
            caesar_cipher(direction)
            if not play_again():
                break
        else:
            print("Invalid input. Please enter 'encode' or 'decode'.")

if __name__ == "__main__":
    main()


import string
from art import cypher_logo_symbols

print(cypher_logo_symbols)

alphabet =list(string.ascii_lowercase)

def cesar(chosen_direction,original_text,shift_amount):
    cipher_text= ""
    if chosen_direction == "decode":
        shift_amount *= -1

    for character in original_text:

        if character not in alphabet:
            cipher_text += character
        else:
            shifted_position = alphabet.index(character) + shift_amount
            shifted_position %=len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"here is the {chosen_direction}d statement:{cipher_text}\n")


continue_process = True
while continue_process:
    direction = input(f"Type 'encode' to encode a massage or 'decode' to decode it:\n").lower()
    text = input("type your massage:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cesar(direction,text,shift)

    repeat = input("would you like to continue:Type yes to continue otherwise type no.").lower()
    if repeat == "no":
        continue_process = False
        print("goodbye")






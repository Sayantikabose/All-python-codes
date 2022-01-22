alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) 

def encrypt(text,shift): 
    cyper=""
    for letters in text:
        position = alphabet.index(letters)
        new_position=position+shift
        new_letter = alphabet[new_position]
        cyper = cyper + new_letter 
    print(cyper)

encrypt(text,shift) 
def decrypt(text, shift):
    cyber=""
    for letters in text:
        position = alphabet.index(letters)
        new_position=position-shift
        new_letter = alphabet[new_position]
        cyber = cyber + new_letter 
    print(cyber)

decrypt(text,shift)
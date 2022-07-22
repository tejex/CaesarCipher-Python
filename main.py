from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
def caesar(direction,text,shift):
  caesar_text = ''
  if direction == 'encode':
    for letter in text:
      if letter in alphabet:
        caesar_text += alphabet[alphabet.index(letter) + shift]
      else:
        caesar_text += letter
    print(f"Your encrypted word is {caesar_text}")
  if direction == 'decode':
    for letter in text:
      if letter in alphabet:
        caesar_text += alphabet[alphabet.index(letter) - shift]
    print(f"Your decrypted word is {caesar_text}")

want_more = False
while not want_more:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(direction,text,shift)
  proceed = input("Would you like to continue? Type Yes or No: ").lower()
  if proceed == 'yes':
    want_more = False
  if proceed == 'no':
    want_more = True
    print("Goodbye")

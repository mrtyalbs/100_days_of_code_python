alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö' 'p', 'q', 'r', 's', 'ş' 't', 'u', 'ü',
            'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift_amount):
    if direction == "encode":
        shifted_text = ""
        for letter in text:
            if letter in alphabet:
                plain_index = alphabet.index(letter)
                shifted_index = plain_index + shift_amount

                if shifted_index <= len(alphabet) - 1:
                    letter = alphabet[shifted_index]
                    shifted_text += letter
                else:
                    shifted_text += alphabet[shifted_index - len(alphabet)]
            else:
                shifted_text += letter

        print(f"The encoded text is: {shifted_text}")

    elif direction == "decode":
        plain_text = ""
        for letter in text:
            if letter in alphabet:
                shifted_index = alphabet.index(letter)
                plain_index = shifted_index - shift_amount

                letter = alphabet[plain_index]
                plain_text += letter
            else:
                plain_text += letter

        print(f"The decoded text is: {plain_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = (int(input("Type the shift number:\n"))) % 26

    caesar(direction, text, shift)

    ask_continue = input("If you want to go again type 'yes'. Otherwise type 'no'.\n").lower()

    if ask_continue == "no":
        should_continue = False

print("Goodbye")

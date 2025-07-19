import art
logo = art.logo

over = False
while not over:

    print(logo)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    print()

    text = input("Type your message:\n").lower()
    print()

    shift = int(input("Type the shift number:\n"))
    print()

    def caesar(direction___, text___, shift___):

        if direction___ == "encode":
            cipher_text = ""

            for i in text___:
                if i not in alphabet:
                    cipher_text += i
                else:
                    shifted_position = alphabet.index(i) + shift___
                    shifted_position %= len(alphabet)
                    cipher_text += alphabet[shifted_position]

            print(f"Here is the encoded result: {cipher_text} \n")

        elif direction___ == "decode":
            cipher_text = ""

            for i in text___:
                if i not in alphabet:
                    cipher_text += i
                else:
                    shifted_position = alphabet.index(i) - shift___
                    shifted_position %= len(alphabet)
                    cipher_text += alphabet[shifted_position]

            print(f"Here is the decoded result: {cipher_text} \n")


    caesar(direction, text, shift)

    answer =input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()
    if answer == "no":
        over = True
    else:
        print("\n" * 50)
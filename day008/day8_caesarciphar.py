# Day 8 - Caesar Cipher

alphabets = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

# Input
choice = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
original_text = input("Enter your message: ")
shift_amount = int(input("Enter shift number: "))

output_text = ""

# Process
for letter in original_text:

    if letter in alphabets:
        position = alphabets.index(letter)

        if choice == "encode":
            new_position = (position + shift_amount) % len(alphabets)

        elif choice == "decode":
            new_position = (position - shift_amount) % len(alphabets)

        else:
            print("Invalid choice!")
            break

        output_text += alphabets[new_position]

    else:
        output_text += letter   # keep spaces & symbols


# Output
print("Result:", output_text)


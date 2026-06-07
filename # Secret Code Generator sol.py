# Secret Code Generator

def encode_message(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result


def decode_message(message, shift):
    return encode_message(message, -shift)


while True:
    print("\n--- Secret Code Generator ---")
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        print("Encoded Message:", encode_message(text, shift))

    elif choice == "2":
        text = input("Enter coded message: ")
        shift = int(input("Enter shift value: "))
        print("Decoded Message:", decode_message(text, shift))

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
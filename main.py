def encrypt():
    print("Encrypt - Coming Soon")


def decrypt():
    print("Decrypt - Coming Soon")


def attack():
    print("Attack - Coming Soon")


def analyze():
    filename = "datasets/sample1.txt"

    with open(filename, "r") as file:
        text = file.read()

    characters = len(text)
    words = len(text.split())
    lines = len(text.splitlines())
    unique_characters = len(set(text))

    print("\n===== File Analysis =====")
    print("Characters :", characters)
    print("Words      :", words)
    print("Lines      :", lines)
    print("Unique Characters :", unique_characters)

    print("\nLetter Frequency:")

    frequency = {}

    for ch in text.lower():
        if ch.isalpha():
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

    for letter in sorted(frequency):
        print(letter, ":", frequency[letter])


def show_menu():
    print("\n===== CryptoLabX =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            encrypt()

        elif choice == "2":
            decrypt()

        elif choice == "3":
            attack()

        elif choice == "4":
            analyze()

        elif choice == "5":
            print("Thank you for using CryptoLabX.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

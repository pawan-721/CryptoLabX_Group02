import string
import re

ALPHABET = string.ascii_lowercase

def frequency_analysis(text):
    freq = {}

    for ch in text.lower():
        if ch.isalpha():
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1

    total = sum(freq.values())

    print("\nLETTER FREQUENCY")
    print("Letter  Count  Percentage")

    for ch in sorted(freq, key=freq.get, reverse=True):
        percentage = (freq[ch] / total) * 100
        print(f"{ch.upper():<7}{freq[ch]:<7}{percentage:.2f}%")

    print("\nMost frequent letters:")
    for ch in sorted(freq, key=freq.get, reverse=True)[:5]:
        print(ch.upper(), end=" ")
    print()

    return freq


def word_frequency_analysis(text):
    words = re.findall(r"[A-Za-z]+", text.lower())
    freq = {}

    for word in words:
        if word not in freq:
            freq[word] = 0
        freq[word] += 1

    print("\nWORD FREQUENCY")

    for word in sorted(freq, key=freq.get, reverse=True):
        if freq[word] > 1:
            print(f"{word}: {freq[word]}")

    print("\nONE-LETTER WORDS")
    for word in words:
        if len(word) == 1:
            print(word, end=" ")
    print()

    print("\nTWO-LETTER WORDS")
    for word in words:
        if len(word) == 2:
            print(word, end=" ")
    print()

    print("\nTHREE-LETTER WORDS")
    for word in words:
        if len(word) == 3:
            print(word, end=" ")
    print()

    return freq


def pattern_of_word(word):
    pattern = {}
    next_number = 0
    result = []

    for ch in word.lower():
        if ch not in pattern:
            pattern[ch] = next_number
            next_number += 1
        result.append(pattern[ch])

    return tuple(result)


def pattern_analysis(text):
    words = re.findall(r"[A-Za-z]+", text.lower())
    patterns = {}

    for word in words:
        pattern = pattern_of_word(word)

        if pattern not in patterns:
            patterns[pattern] = []

        if word not in patterns[pattern]:
            patterns[pattern].append(word)

    print("\nREPEATED LETTER PATTERNS")

    for pattern in patterns:
        if len(patterns[pattern]) > 1:
            print(pattern, "->", ", ".join(patterns[pattern]))

    return patterns


def apply_substitution(text, key):
    result = ""

    for ch in text:
        lower = ch.lower()

        if lower in key:
            new_ch = key[lower]
            if ch.isupper():
                new_ch = new_ch.upper()
            result += new_ch
        else:
            result += ch

    return result


def display_partial_plaintext(ciphertext, key):
    partial = ""

    for ch in ciphertext:
        lower = ch.lower()

        if lower in key:
            new_ch = key[lower]
            if ch.isupper():
                new_ch = new_ch.upper()
            partial += new_ch
        elif ch.isalpha():
            partial += "_"
        else:
            partial += ch

    print("\nPARTIAL PLAINTEXT")
    print(partial)


def verify_solution(plaintext, ciphertext, key):
    encrypted = apply_substitution(plaintext, key)

    if encrypted == ciphertext:
        print("\nVerification successful.")
        print("Recovered key correctly re-encrypts the plaintext.")
        return True

    print("\nVerification failed.")
    return False


def create_key():
    print("\nEnter substitution alphabet.")
    print("Example: qwertyuiopasdfghjklzxcvbnm")
    print("It must contain 26 different letters.")

    while True:
        substitution = input("Substitution alphabet: ").lower()

        if len(substitution) == 26:
            valid = True

            for ch in substitution:
                if ch not in ALPHABET:
                    valid = False

            if len(set(substitution)) == 26 and valid:
                key = {}

                for i in range(26):
                    key[ALPHABET[i]] = substitution[i]

                return key

        print("Invalid key. Enter 26 different letters.")


def show_key(key):
    print("\nSUBSTITUTION KEY")
    print("Plain : " + ALPHABET)
    print("Cipher: " + "".join(key[ch] for ch in ALPHABET))


def main():
    try:
        with open("plaintext.txt", "r", encoding="utf-8") as file:
            plaintext = file.read()
    except FileNotFoundError:
        print("plaintext.txt not found.")
        print("Create plaintext.txt and add the required text.")
        return

    print("===== MONOALPHABETIC SUBSTITUTION CIPHER =====")

    print("\nPlaintext loaded.")
    print("Characters:", len(plaintext))

    key = create_key()
    show_key(key)

    ciphertext = apply_substitution(plaintext, key)

    with open("ciphertext.txt", "w", encoding="utf-8") as file:
        file.write(ciphertext)

    print("\nCiphertext generated and saved to ciphertext.txt")

    print("\n===== CIPHERTEXT =====")
    print(ciphertext)

    frequency_analysis(ciphertext)
    word_frequency_analysis(ciphertext)
    pattern_analysis(ciphertext)

    print("\n===== CRYPTANALYSIS =====")

    print("Use the observations above to propose substitutions.")
    print("Enter substitutions one by one.")
    print("Example: Q E")
    print("Type DONE when finished.")

    recovered_key = {}

    while True:
        value = input("Substitution: ").strip().lower()

        if value == "done":
            break

        parts = value.split()

        if len(parts) != 2:
            print("Enter in format: cipher_letter plain_letter")
            continue

        cipher_letter = parts[0]
        plain_letter = parts[1]

        if len(cipher_letter) != 1 or len(plain_letter) != 1:
            print("Enter single letters.")
            continue

        recovered_key[cipher_letter] = plain_letter

        display_partial_plaintext(ciphertext, recovered_key)

    print("\n===== RECOVERED PLAINTEXT =====")
    recovered_plaintext = apply_substitution(ciphertext, recovered_key)
    print(recovered_plaintext)

    print("\n===== VERIFICATION =====")
    verify_solution(plaintext, ciphertext, key)


if __name__ == "__main__":
    main()
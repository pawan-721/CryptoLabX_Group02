from shift_cipher import decrypt


def load_dictionary(filename):
    with open(filename, "r") as file:
        return set(word.strip().lower() for word in file)


def score_text(text, dictionary):
    words = text.lower().split()
    return sum(word.strip(".,!?") in dictionary for word in words)


def brute_force(ciphertext, dictionary):
    best_text = ""
    best_score = -1
    best_key = 0

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = score_text(plaintext, dictionary)

        print("Key:", key, "Score:", score, "Text:", plaintext)

        if score > best_score:
            best_score = score
            best_text = plaintext
            best_key = key

    return best_key, best_text, best_score


if __name__ == "__main__":
    dictionary = load_dictionary(
        "../dictionary/english_words.txt"
    )

    ciphertext = input("Enter ciphertext: ")

    key, plaintext, score = brute_force(ciphertext, dictionary)

    print("\nBest Key:", key)
    print("Best Plaintext:", plaintext)
    print("Score:", score)
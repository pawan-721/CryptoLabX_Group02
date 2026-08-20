from shift_cipher import decrypt

ENGLISH_FREQ = [
    8.167, 1.492, 2.782, 4.253, 12.702, 2.228,
    2.015, 6.094, 6.966, 0.153, 0.772, 4.025,
    2.406, 6.749, 7.507, 1.929, 0.095, 5.987,
    6.327, 9.056, 2.758, 0.978, 2.360, 0.150,
    1.974, 0.074
]


def chi_square_score(text):
    counts = [0] * 26
    total = 0

    for ch in text.lower():
        if 'a' <= ch <= 'z':
            counts[ord(ch) - ord('a')] += 1
            total += 1

    if total == 0:
        return float('inf')

    score = 0

    for i in range(26):
        expected = total * ENGLISH_FREQ[i] / 100
        if expected > 0:
            score += (counts[i] - expected) ** 2 / expected

    return score


def find_key(ciphertext):
    best_key = 0
    best_score = float('inf')
    best_plaintext = ""

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = chi_square_score(plaintext)

        print("Key:", key, "Score:", round(score, 2))

        if score < best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext, best_score


if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")

    key, plaintext, score = find_key(ciphertext)

    print("\nBest Key:", key)
    print("Best Plaintext:", plaintext)
    print("Chi-Square Score:", round(score, 2))
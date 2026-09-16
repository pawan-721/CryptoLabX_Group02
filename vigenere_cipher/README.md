# Assignment 6 - Vigenere Cipher Cryptanalysis

## Objective

The objective of this assignment is to implement cryptanalysis of a Vigenere cipher and recover the plaintext and encryption key from the given ciphertext.

## Cryptanalysis Techniques Used

1. Kasiski Examination
2. Index of Coincidence (IC)
3. Frequency Analysis
4. Key Length Estimation
5. Key Recovery
6. Vigenere Decryption
7. Re-encryption Verification

## Working of the Program

The program performs the following steps:

1. Cleans the ciphertext by removing spaces and non-alphabetic characters.
2. Finds repeated patterns in the ciphertext.
3. Calculates distances between repeated patterns.
4. Finds common factors of the distances using Kasiski examination.
5. Calculates the Index of Coincidence for possible key lengths.
6. Estimates the most suitable key length.
7. Divides the ciphertext into groups according to the estimated key length.
8. Performs frequency analysis on every group.
9. Determines the Caesar shift for each group.
10. Combines the shifts to recover the Vigenere key.
11. Decrypts the ciphertext using the recovered key.
12. Re-encrypts the recovered plaintext to verify the result.

## Important Functions

The following functions are implemented in main.py:

- clean_ciphertext()
- find_repeated_patterns()
- calculate_distances()
- find_factors()
- calculate_ic()
- kasiski_analysis()
- split_into_groups()
- frequency_analysis()
- find_shift()
- find_key()
- vigenere_decrypt()
- vigenere_encrypt()
- verify()
- format_freq_table()

## Results

### Ciphertext Length

758 characters

### Estimated Key Length

12

### Recovered Key

UNITEDSTATES

### Frequency Analysis

The ciphertext was divided into 12 groups according to the estimated key length.

Frequency analysis was performed on each group and the letter frequencies were compared with standard English letter frequencies to determine the corresponding shifts.

## Recovered Plaintext

The recovered plaintext begins with:

WETHEREFORETHEREPRESENTATIVESOFTHEUNITEDSTATESOFAMERICAINGENERALCONGRESSASSEMBLEDAPPEALINGTOTHESUPREMEJUDGE...

The complete recovered plaintext is stored in:

recovered_plaintext.txt

## Verification

The recovered plaintext was encrypted again using the recovered key.

The resulting ciphertext matched the original ciphertext.

[SUCCESS] Re-encryption matches original ciphertext.

## Files

vigenere_cipher/
├── main.py
├── README.md
├── recovered_plaintext.txt
├── outputs/
└── reports/

## How to Run

Open the terminal inside the vigenere_cipher directory and run:

python3 main.py

The program displays:

- Ciphertext length
- Kasiski and IC analysis
- Frequency analysis
- Estimated key length
- Recovered key
- Partial recovered plaintext
- Verification result

The complete plaintext is automatically saved to:

recovered_plaintext.txt

## Conclusion

The given Vigenere ciphertext was successfully cryptanalyzed using Kasiski examination, Index of Coincidence, and frequency analysis.

The estimated key length was 12 and the recovered encryption key was:

UNITEDSTATES

The ciphertext was successfully decrypted and the recovered plaintext was verified by re-encrypting it with the recovered key.

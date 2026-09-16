# Monoalphabetic Substitution Cipher and Cryptanalysis

## Group
Group 02

## Objective

The objective of this assignment is to implement a Monoalphabetic Substitution Cipher and perform its cryptanalysis using frequency analysis, word frequency analysis, and pattern analysis.

The plaintext was taken from the assigned page of the book "Modern Cryptography" by Katz and Lindell.

For Group 02, the assigned page is Page 32.

## Features

The program performs the following tasks:

1. Generate ciphertext using a monoalphabetic substitution cipher.
2. Perform letter frequency analysis.
3. Perform word frequency analysis.
4. Perform pattern analysis.
5. Apply guessed substitutions to the ciphertext.
6. Display the partially recovered plaintext.
7. Recover the substitution key.
8. Verify the recovered solution by re-encrypting the plaintext.

## Required Functions

The program contains the following functions:

- `frequency_analysis()`
- `word_frequency_analysis()`
- `pattern_analysis()`
- `apply_substitution()`
- `display_partial_plaintext()`
- `verify_solution()`

## Monoalphabetic Substitution Cipher

In a monoalphabetic substitution cipher, each plaintext letter is replaced by a fixed ciphertext letter.

The key used for encryption was:

Plaintext alphabet:

abcdefghijklmnopqrstuvwxyz

Ciphertext alphabet:

qwertyuiopasdfghjklzxcvbnm

Therefore, the encryption mapping is:

a -> q
b -> w
c -> e
d -> r
e -> t
f -> y
g -> u
h -> i
i -> o
j -> p
k -> a
l -> s
m -> d
n -> f
o -> g
p -> h
q -> j
r -> k
s -> l
t -> z
u -> x
v -> c
w -> v
x -> b
y -> n
z -> m

## Cryptanalysis

The ciphertext was analyzed using the following methods.

### 1. Frequency Analysis

The frequency of every ciphertext letter was counted.

The letters were arranged according to their frequency. The most frequent ciphertext letters were examined first because frequent letters in English plaintext commonly correspond to frequently occurring English letters.

### 2. Word Frequency Analysis

The ciphertext was divided into words and repeated words were examined.

One-letter, two-letter, and three-letter words were also considered while proposing substitutions.

### 3. Pattern Analysis

Repeated letter patterns inside words were examined.

For example, if a ciphertext word has the same letter appearing at the same positions, the corresponding plaintext word should preserve the same pattern.

### 4. Iterative Substitution

Candidate substitutions were entered one at a time.

After each substitution, the partial plaintext was displayed.

If the resulting text became meaningful, the substitution was retained. If it produced an incorrect pattern, the hypothesis was rejected or reconsidered.

This process was continued until the plaintext became readable.

## Recovered Plaintext

The recovered plaintext is the same text that was used to generate the ciphertext.

The recovered text discusses encryption schemes, perfect secrecy, probability distributions, Bayes' theorem, and perfect indistinguishability.

The complete plaintext is stored in:

`plaintext.txt`

## Ciphertext

The generated ciphertext is stored in:

`ciphertext.txt`

## Recovered Key

The recovered decryption mapping is:

q -> a
w -> b
e -> c
r -> d
t -> e
y -> f
u -> g
i -> h
o -> i
p -> j
a -> k
s -> l
d -> m
f -> n
g -> o
h -> p
j -> q
k -> r
l -> s
z -> t
x -> u
c -> v
v -> w
b -> x
n -> y
m -> z

## Verification

After recovering the substitution key, the recovered plaintext was verified by re-encrypting it using the recovered key.

The generated ciphertext matched the original ciphertext.

Output:

Verification successful.

Recovered key correctly re-encrypts the plaintext.

## Files

```text
monoalphabetic_cipher/
├── README.md
├── main.py
├── plaintext.txt
├── ciphertext.txt
├── outputs/
└── reports/
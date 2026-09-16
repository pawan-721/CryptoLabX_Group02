# Cryptanalysis Report

## Group 02

## Objective

The ciphertext generated using the monoalphabetic substitution cipher was
cryptanalyzed using frequency analysis, word frequency analysis, and pattern
analysis.

The plaintext was recovered iteratively by testing possible substitutions
and observing the resulting partial plaintext.

## Cryptanalysis Decision Table

| Step | Observation | Possible Substitution | Substitution Tested | Result | Decision |
|------|-------------|-----------------------|----------------------|--------|----------|
| 1 | `q` was a frequent ciphertext letter and appeared in useful word patterns | q -> a | q -> a | Common English words started appearing | Accepted |
| 2 | `t` appeared very frequently | t -> e | t -> e | Words became more readable | Accepted |
| 3 | `o` occurred frequently | o -> i | o -> i | Partial plaintext improved | Accepted |
| 4 | `f` appeared frequently | f -> n | f -> n | English word patterns became clearer | Accepted |
| 5 | `l` appeared in repeated word patterns | l -> s | l -> s | Several words became meaningful | Accepted |
| 6 | `e` occurred in useful positions | e -> c | e -> c | Text became more readable | Accepted |
| 7 | Repeated word patterns suggested `k` as `r` | k -> r | k -> r | Meaningful words appeared | Accepted |
| 8 | Word patterns suggested `n` as `y` | n -> y | n -> y | Plaintext improved | Accepted |
| 9 | `h` appeared in patterns matching `p` | h -> p | h -> p | Meaningful text appeared | Accepted |
| 10 | Frequency and word pattern suggested `z` as `t` | z -> t | z -> t | Words became readable | Accepted |
| 11 | `g` appeared in positions matching `o` | g -> o | g -> o | Plaintext improved | Accepted |
| 12 | `d` appeared in patterns matching `m` | d -> m | d -> m | Meaningful words appeared | Accepted |
| 13 | `s` appeared in repeated patterns | s -> l | s -> l | Plaintext became clearer | Accepted |
| 14 | `y` appeared in positions matching `f` | y -> f | y -> f | Text became readable | Accepted |
| 15 | Word patterns suggested `j` as `q` | j -> q | j -> q | "exactly equal" became readable | Accepted |
| 16 | Remaining pattern analysis suggested `m` as `z` | m -> z | m -> z | Complete plaintext became readable | Accepted |

## Recovered Plaintext

After applying the substitutions iteratively, the plaintext became fully
readable.

The recovered text contains discussion of:

- Encryption schemes
- Perfect secrecy
- Bayes' theorem
- Probability distributions
- Perfect indistinguishability

The complete recovered plaintext is stored in `plaintext.txt`.

## Recovered Decryption Key

The final recovered mapping is:

```text
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


Verification

The recovered key was used to re-encrypt the recovered plaintext.

The resulting ciphertext matched the original ciphertext.

Therefore, the recovered substitution key was successfully verified.

Verification successful.

Conclusion

The monoalphabetic substitution cipher was successfully implemented and
cryptanalyzed.

Frequency analysis, word frequency analysis, and pattern analysis were used
to recover the substitution mapping. The plaintext was recovered iteratively
by testing substitutions and examining the resulting partial plaintext.

The final recovered key was verified by re-encrypting the recovered plaintext.
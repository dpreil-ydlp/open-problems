# Spanish Strip Cipher — Part 3

Clean text transcription of Luis Alberto Benthin Sanguino's MysteryTwister PDF, with printed slide labels through 10/10. The image-only Figure 1 on printed page 4/10 is in part3-figure1.png.

Source: https://mysterytwister.org/media/challenges/pdf/mtc3-sanguino-03-SSC-03-en.pdf
Author/date on PDF: Luis Alberto Benthin Sanguino, February 2014.

## Printed page 1/10

SPANISH STRIP CIPHER – PART 3

Author: Luis Alberto Benthin Sanguino

February 2014

## Printed pages 2–3/10 — Introduction

The Spanish Strip Cipher (SSC) is a homophonic substitution cipher, in which a plaintext letter not only maps to one ciphertext character (as in monoalphabetic substitution ciphers), but it can map to different ones. In this kind of ciphers, the ciphertext characters are called homophones, which are arranged in a table, where each column is mapped by one letter of the plaintext alphabet. During the Spanish civil war (1936–1939) this method was widely adopted by both sides, Republicans and Nationalists.

Normally, the number of homophones in a column is related with the frequency of a plaintext letter. For example, in a Spanish text, the letter E occurs with a frequency of 13.68% approximately. On the other hand, the letter N approximately occurs with a frequency of 6.71%. Thus, the column assigned to the letter E should contain more homophones than the column assigned to the letter N. In this way, frequency analysis attacks become more difficult. Contradictorily, in the original variant of SSC a column contains 3 or 4 homophones, regardless of the letters frequency.

## Printed page 4/10 — Key elements and diagram

In addition to the homophones table, the SSC encompasses three more elements (see Figure 1): a random alphabet, a keyword, which is used to generate the random alphabet, and an initial position that is used to shift the random alphabet.

Figure 1 labels: keyword “cryptool”; initial position “B in C”; ordered alphabet A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z. The random alphabet and homophone table appear in the linked image.

## Printed page 5/10 — Encryption

In order to encrypt a plaintext, sender and receiver agree on a key which consists of three elements: a keyword, a homophones table, and an initial position. After generating and shifting the random alphabet, the encryption can begin. For each plaintext letter:

1. We look for the same letter in the random alphabet.
2. We substitute the plaintext letter by one the homophones of the same column of the random-alphabet letter.

For instance, the plaintext letter A can be replaced by the homophones 27, 52 and 79. The selection of one of these homophones can be performed either sequentially or randomly.

## Printed page 6/10 — Encryption example

A plaintext is encrypted using the key from Figure 1.

Plaintext: U N I V E R S I D A D  
Ciphertext: 36 22 14 18 17 12 10 43 11 27 38

## Printed page 7/10 — Decryption

The decryption is a straightforward process, in which each ciphertext homophone is replaced by its corresponding letter of the random alphabet.

Example: A ciphertext is decrypted using the key shown in Figure 1.

Ciphertext: 10 17 35 12 39 33  
Plaintext: S E C R E T

## Printed page 8/10 — Challenge

Please find the corresponding plaintext!

No capitalization, spacing, punctuation, null, or answer formatting rule appears on this page.

## Printed page 9/10 — Challenge transcript

23 22 31 02 30 58 10 68 55 14 03 16 90 41 81 05 17 44 35 50 45
31 78 68 04 05 50 32 48 23 84 83 77 51 47 44 81 83 14 08 17 32
76 38 10 81 24 19 04 35 38 32 16 45 03 16 32 10 68 28 03 83 64
19 60 81 69 32 98 45 03 40 22 32 34 35 48 73 05 55 31 16 51 47
82 78 98 90 63 81 48 06 31 83 74 08 32 98 62 68 65 90 91 76 63
64 68 84 16 05 83 28 32 39 31 48 69 44 90 83 11 68 74 82 48 10
08 43 44 90 14 81 74 51 18 35 32 50 49 44 84 14

## Printed page 10/10 — Hints

1. This telegram was sent during the Spanish civil war (Summer/Fall 1936). It is most likely to be a Spanish text. However, it can also be a text written in Basque.
2. It is likely that this telegram was encrypted with the SSC. Nonetheless, some variants should be considered:
   - The columns may content between 3 and 5 homophones [sic].
   - The ordered alphabet can include the digraphs LL and CH, or also can exclude the letter W.

## Challenge-specific findings

- Language: most likely Spanish; Basque is also explicit.
- Date: Summer/Fall 1936. No day or exact month is given.
- Sender: not named in the PDF.
- Expected plaintext: an original telegram. No more precise genre or content is given.
- Crib: none is supplied.
- Key: the PDF does not say that the key is new or shared with parts 1 or 2.
- Answer format: the PDF only asks for the corresponding plaintext. It gives no case, spaces, punctuation, or encoding rule.

The current MysteryTwister listing was checked on 2026-10-15. It describes an original Spanish Civil War telegram, says no new solutions have been accepted since July 2026, and shows 0 solves. No account or submission was used.

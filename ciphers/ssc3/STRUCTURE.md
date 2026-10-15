# Spanish Strip Cipher: structure and evidence

## Scope

This note separates the rules stated in the MysteryTwister (MTC) PDFs from options in the CrypTool 2 (CT2) implementation. Part 3 allows variants. Do not assume every CT2 option was used for the historical telegram.

## Alphabet

The standard alphabet shown in Sanguino's Figure 1 and CT2's 27-letter option is:

A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z

It has 27 symbols. Ñ is a separate letter. K and W are included. [1, printed p. 4/10; 2, settings source lines 50–55]

CT2 also implements a 29-symbol variant. It inserts CH between C and D and LL between L and M. CT2 encodes those digraphs internally as single symbols. Part 3 says its ordered alphabet may include LL and CH, or may exclude W. Part 3 does not state the order for those variants. [2, user documentation; 3, printed p. 10/10]

## Keyword alphabet and shift

The key has a keyword, a homophone table, and an initial position. The keyword generates an unordered alphabet strip; the initial position shifts that strip against the standard ordered strip. [1, printed pp. 4–5/10; 2, user documentation]

CT2 documents this generation procedure:

1. Remove repeated keyword letters, keeping the first occurrence.
2. Append the unused ordered-alphabet letters in their normal order.
3. Write the resulting sequence in rows, with the distinct keyword length as row width.
4. Read each column from top to bottom. The concatenated columns form the random alphabet.
5. Rotate the random alphabet until the selected generated letter is over the selected ordered-alphabet letter. Example: B -> C aligns random-alphabet B with ordered-alphabet position C.

CT2 example: CRYPTOOL becomes CRYPTOL. Row filling and column reading gives C A I S R B J U Y D K V P E M W T F N X O G Ñ Z L H Q. The two-letter alignment is a cyclic shift modulo alphabet length. [2, user documentation; 2, settings source lines 129–170]

This is a keyword-based columnar rearrangement followed by a cyclic rotation. It is not an unrestricted random permutation. Part 3 does not identify its keyword or offset.

## Homophones and numeric assignment

For a plaintext letter, locate it on the random alphabet strip and replace it with one number below the same strip position. The numbers below a position are that letter's homophones. [1, printed p. 5/10; 2, user documentation]

Parts 1 and 2 state that all 99 numbers from 01 through 99 are randomly entered in the table, with 3 or 4 numbers in each of the 27 columns. Therefore there are 18 four-number columns and 9 three-number columns. The PDFs do not name which letters have which column size. [4, printed p. 10/10; 5, printed p. 10/10]

Part 3 permits 3 to 5 numbers per column. Its hint page does not give the number range. Use 01–99 as a strong baseline because parts 1/2 use it, but keep the range open. CT2 documentation describes table ranges of 01–99 or 10–99; these documented ranges omit 00. Part 3's ciphertext contains no 00. [3, printed p. 10/10]

Homophones are not consecutive numeric runs and no arithmetic relation is stated. Parts 1/2 explicitly say values were randomly placed. CT2's random-table code shuffles the number list and separately shuffles the column sizes, then groups successive entries of that shuffled list. Values adjacent in the shuffled list are not numerically adjacent in a meaningful way. [2, settings source lines 60–68, 101–127]

The table is separate from the keyword alphabet. The keyword and shift determine which plaintext letter reaches a strip position; the number group under that position determines its ciphertext choices. CT2 has a random table and fixed-table options, including one 90-number table from 10 to 99. Those are implementation options, not evidence for part 3. [2, user documentation and settings source lines 60–127]

## Choosing a homophone

Sanguino says senders can select homophones sequentially or randomly. Part 1 says its values were selected sequentially. Part 2 says its values were selected randomly. Part 3 does not identify the mode. [1, printed p. 5/10; 4, printed p. 10/10; 5, printed p. 10/10; 3, printed pp. 9–10/10]

CT2 supports random selection and round-robin selection. Round-robin advances the per-letter offset after each use. This is a candidate model only; it does not establish part 3's mode. [2, settings source line 70; 6, source lines 140–177]

## Spaces, punctuation, and nulls

The PDFs do not state a historical rule for spaces, punctuation, or nulls. Their examples contain letters only. Parts 1 and 2 require answers in uppercase without spaces. CT2 says input plaintext must contain only letters from the selected alphabet. Its decryption code removes non-digit characters and reads two-digit symbols, so spaces in a ciphertext transcript are token separators. No null procedure is described. [1, printed pp. 5–8/10; 4, printed p. 8/10; 5, printed p. 8/10; 2, user documentation; 6, source lines 110–177]

Do not assume historical operators inserted nulls or preserved word boundaries.

## Sources

1. Luis Alberto Benthin Sanguino, Spanish Strip Cipher – Part 3, MysteryTwister PDF, Feb. 2014: https://mysterytwister.org/media/challenges/pdf/mtc3-sanguino-03-SSC-03-en.pdf. Page numbers here are the printed x/10 labels.
2. CrypTool 2 Spanish Strip Cipher component: user documentation https://github.com/CrypToolProject/CrypTool-2/blob/main/CrypPlugins/SpanishStripCipher/DetailedDescription/doc.xml and settings https://github.com/CrypToolProject/CrypTool-2/blob/main/CrypPlugins/SpanishStripCipher/SpanishStripCipherSettings.cs.
3. MysteryTwister, Part 3 PDF above, printed pp. 9–10/10.
4. Luis Alberto Benthin Sanguino, Spanish Strip Cipher – Part 1: https://mysterytwister.org/media/challenges/pdf/mtc3-sanguino-01-SSC-01-en.pdf, printed p. 10/10.
5. Luis Alberto Benthin Sanguino, Spanish Strip Cipher – Part 2: https://mysterytwister.org/media/challenges/pdf/mtc3-sanguino-02-SSC-02-en.pdf, printed p. 10/10.
6. CrypTool 2 cipher component source: https://github.com/CrypToolProject/CrypTool-2/blob/main/CrypPlugins/SpanishStripCipher/SpanishStripCipher.cs.
7. Luis Alberto Benthin Sanguino, Gregor Leander, Christof Paar, Bernhard Esslinger, and Ingo Niebel, “Analyzing the Spanish strip cipher by combining combinatorial and statistical methods,” Cryptologia 40(3), pp. 261–284 (2016 print; online 2015), DOI https://doi.org/10.1080/01611194.2015.1050332. Its public abstract describes 3–5 ciphertext symbols per letter and an attack based on homophone-table analysis, letter frequencies, and dictionary search. The full paper was not publicly accessible in this review; no paper page number is claimed.


## Related Cipherbrain coverage

Klaus Schmeh's post “A beautiful Spanish Encryption device” (24 Mar. 2018) discusses the Criptografo Palacios, a Spanish strip-based device. The post says it likely implements a polyalphabetic strip cipher and does not identify it as the Spanish Strip Cipher discussed here. Treat it as related historical context, not an SSC rule source: https://scienceblogs.de/klausis-krypto-kolumne/2018/03/24/a-beautiful-spanish-encryption-device/. Searches for “Spanish Strip Cipher”, “Sanguino”, and “spanische Streifenchiffre” did not find a Cipherbrain post specifically about the SSC.

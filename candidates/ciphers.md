# Classical cipher candidates

Access date for this review: 2026-10-15.

The requested minimum was 8 candidates. Only one candidate passed all inclusion checks with the evidence available. I have not filled the remaining rows with short, already solved, method-unknown, or inadequately sourced ciphertexts.

| Rank | Name | Source URL | Year | Symbols | Alphabet size | Suspected method | Language | Hints | Solved-status evidence | Tractability | Reason |
|---:|---|---|---:|---:|---:|---|---|---|---|---:|---|
| 1 | Spanish Strip Cipher — Part 3 | [MysteryTwister challenge](https://mysterytwister.org/challenges/level-x/spanish-strip-cipher-part-3); [ciphertext transcript PDF](https://mysterytwister.org/media/challenges/pdf/mtc3-sanguino-03-SSC-03-en.pdf) | 1936 | 142 | 55 observed two-digit tokens (nominal code space 00–99) | Spanish Strip Cipher: homophonic substitution with a keyword-generated mixed alphabet and initial shift | Probably Spanish; Basque is also possible | Spanish Civil War telegram, summer/fall 1936. Source describes the cipher family and lists possible variants: 3–5 homophones per letter, optional LL/CH, and possible W omission. | MysteryTwister’s current Level X page shows 0 solves and no published-solution notice. Searches for the exact challenge title with “solved” and “solution” found no credible solution. | 3/5 | 142 tokens give usable statistics; the homophone structure is known. Unknown Spanish/Basque language and variant rules add search cost. |

## Frequency summary

| Candidate | IC | Distinct symbols | Distribution |
|---|---:|---:|---|
| Spanish Strip Cipher — Part 3 | 0.019678 | 55 | Homophonic/flat. IC is over two-digit tokens, not letters; the many distinct codes lower it. |

## Source sweep and exclusions

- **Cipher Mysteries:** Search results found relevant topics, including Scorpion and Gaines material, but article opens returned HTTP 502. I moved on as requested and did not treat search snippets as verified ciphertext transcripts.
- **Wikipedia, “List of ciphertexts”:** The unsolved list is dominated by explicit hard exclusions. Other entries in the relevant range lacked evidence of a classical hand cipher and a verbatim transcript that met the length gate.
- **r/codes and r/cryptography wikis:** Searches did not surface unsolved-cipher wiki pages. The Reddit hits were mostly discussion threads or user-created ciphers with custom/unknown systems. I did not promote those to historical classical candidates.
- **Cipherbrain / Klaus Schmeh:** Searches found relevant posts, but article opens returned HTTP 502. I did not use them as the basis for a candidate transcription.
- **American Cryptogram Association:** The public site identifies archived issues as member-area material. I did not log in. The public sample material includes solved practice items, not an eligible unsolved target.
- **MysteryTwister Level X:** The current listing and source PDFs were checked. Spanish Strip Cipher Part 3 is the one candidate that meets the length, method, transcript, and current status checks. Vatican Part 4 has two recorded solves, so I did not call it genuinely unsolved. Other long classical entries in the list show published solutions. The murder-case challenge concerns Ricky McCormick and is explicitly excluded.
- **Recent-status check:** A current ADFGVX audit reports ten messages still open, but also says the known-key hill-climb and key-free attack fail at these lengths, and that a new key or original archive transcript is needed. That does not meet the “plausibly solvable tonight” bar. See [the audit](https://dbourdeau.github.io/cyphersolver/adfgvx.html).

## First attack

1. **Spanish Strip Cipher — Part 3.** Best fit in the verified set: a substantial published transcript, known historical cipher family, and concrete method variants. Use Spanish and Basque language models separately. The target is homophonic, so a simple one-to-one substitution hill-climber is not sufficient.

Only one of the requested top three can be recommended from the candidates that passed every gate. A second or third choice would require relaxing at least one explicit inclusion rule.

## Files

- Ciphertext: [spanish-strip-cipher-part-3.txt](ciphers/spanish-strip-cipher-part-3.txt)
- Metadata and metrics: [spanish-strip-cipher-part-3.meta.json](ciphers/spanish-strip-cipher-part-3.meta.json)

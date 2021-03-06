import string
import itertools

ciphertext = input()
ciphertext = ciphertext.upper()

alphabet = string.ascii_uppercase

KEYLEN = 6

ciphers = []

for i in range(0, KEYLEN):
    ciphers.append("")

# Split into separate texts
for i in range(0, len(ciphertext)):
    ciphers[i%KEYLEN] += ciphertext[i]

key = ""
key2 = ""
key3 = ""

for section in ciphers:
    # Generate alphabet dict
    counts = {}
    for letter in alphabet:
        counts[letter] = 0

    for char in section:
        counts[char] += 1

    largest_letter = ""
    largest_count = 0

    for letter in alphabet:
        if counts[letter] > largest_count:
            largest_count = counts[letter]
            largest_letter = letter

    key += alphabet[(alphabet.index(largest_letter) - alphabet.index("E")) % 26]
    key2 += alphabet[(alphabet.index(largest_letter) - alphabet.index("T")) % 26]
    key3 += alphabet[(alphabet.index(largest_letter) - alphabet.index("H")) % 26]

    print(counts)

print(key)
print(key2)
print(key3)

combinations = [''.join(s) for s in itertools.product(*zip(key,key2))]
all_combinations = []
for combo in combinations:
    all_combinations.extend([''.join(s) for s in itertools.product(*zip(combo,key3))])

combinations = list(set(all_combinations))

plaintexts = []
for test_key in combinations:
    plaintext = ""
    for i in range(0, len(ciphertext)):
        plaintext += alphabet[(alphabet.index(ciphertext[i]) - alphabet.index(test_key[i%len(test_key)])) % 26]
    plaintext = test_key + ":\n" + plaintext + "\n"
    plaintexts.append(plaintext)

plaintexts.sort(key=lambda x: x.count('THE'))

for plaintext in plaintexts:
    print(plaintext)

print(len(plaintexts))

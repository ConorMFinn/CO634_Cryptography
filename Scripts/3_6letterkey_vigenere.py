import string
import itertools

ciphertext = input()
ciphertext = ciphertext.upper()

alphabet = string.ascii_uppercase

ciphers = ["", "", "", "", "", ""]

# Split into separate texts
for i in range(0, len(ciphertext)):
    ciphers[i%6] += ciphertext[i]

key = ""
key2 = ""


for section in ciphers:
    # Find the most common letter in the ciphertext
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

    # Generate keys based on the two most common letters
    key += alphabet[(alphabet.index(largest_letter) - alphabet.index("E")) % 26]
    key2 += alphabet[(alphabet.index(largest_letter) - alphabet.index("T")) % 26]

print(key)
print(key2)

# Find all the combinations of those two keys
combinations = [''.join(s) for s in itertools.product(*zip(key,key2))]

# Create a plaintext for each of the combined keys
plaintexts = []
for test_key in combinations:
    plaintext = ""
    for i in range(0, len(ciphertext)):
        plaintext += alphabet[(alphabet.index(ciphertext[i]) - alphabet.index(test_key[i%len(test_key)])) % 26]
    plaintext = test_key + ":\n" + plaintext + "\n"
    plaintexts.append(plaintext)

# The more "THE"s are found, the more likely it's the true plaintext
plaintexts.sort(key=lambda x: x.count('THE'))

# Find the correct plaintext manually. 
for plaintext in plaintexts:
    print(plaintext)

# EX3: FUXUHD
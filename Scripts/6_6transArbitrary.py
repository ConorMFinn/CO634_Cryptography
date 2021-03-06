import itertools

text = input()

# Row length
CY_LEN = 6

splits = int(len(text)/CY_LEN)

# Split the ciphertext into sections depending on the row length
sections = [text[i:i+splits] for i in range(0, len(text), splits)]

print(sections)

# Generate all permutations of the sections (CY_LEN! (factorial))
combinations = list(itertools.permutations(sections, CY_LEN))

plaintexts = [""] * len(combinations)

# Create all the plaintexts from the combinations
for j in range(len(plaintexts)):
    for i in range(len(text)):
        plaintexts[j] += combinations[j][int(i%CY_LEN)][int(i/CY_LEN)]

# Most "THE"s last so seen first in the terminal
plaintexts.sort(key=lambda x: x.count('THE'))

# Print to manually review
for plaintext in plaintexts:
    print(plaintext)

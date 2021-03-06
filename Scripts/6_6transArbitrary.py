import itertools

text = input()

CY_LEN = 6

splits = int(len(text)/CY_LEN)

sections = [text[i:i+splits] for i in range(0, len(text), splits)]

print(sections)

combinations = list(itertools.permutations(sections, CY_LEN))

plaintexts = [""] * len(combinations)

for j in range(len(plaintexts)):
    for i in range(len(text)):
        plaintexts[j] += combinations[j][int(i%CY_LEN)][int(i/CY_LEN)]

plaintexts.sort(key=lambda x: x.count('THE'))

for plaintext in plaintexts:
    print(plaintext)

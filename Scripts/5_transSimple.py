text = input()

# Try with cypher lengths between 4 and 6
CY_LEN = 4

splits = int(len(text)/CY_LEN)

sections = [text[i:i+splits] for i in range(0, len(text), splits)]

print(sections)

plaintext = ""

for i in range(len(text)):
    plaintext += sections[int(i%4)][int(i/4)]

print(plaintext)
import string

# Start by analysing the original text for the frequency of each letter
full_text = open('tess27.txt').read()

alphabet = string.ascii_uppercase + '|'

percentages = {}

for letter in alphabet:
    percentages[letter] = 0.0

for letter in alphabet:
    percentages[letter] = full_text.count(letter)/len(full_text)

# Then analyse the ciphertext to find the frequency of each letters in that

ciphertext = input()

percentages_cipher = {}

for letter in alphabet:
    percentages_cipher[letter] = 0.0

for letter in alphabet:
    percentages_cipher[letter] = ciphertext.count(letter)/len(ciphertext)

# Match up similar % values to get a baseline decryption mapping

percentages = dict(sorted(percentages.items(), key=lambda item: item[1]))
percentages_cipher =  dict(sorted(percentages_cipher.items(), key=lambda item: item[1]))

mapping = {}

for cipher_letter, plain_letter in zip(percentages_cipher.keys(), percentages.keys()):
    mapping[cipher_letter] = plain_letter


# Started with mapping directly between the frequency of letters in the full 
# text of tess27.txt and the frequency of letters in the ciphertext. Then went
# though the generated plain(ish)text until I found words I recognised that 
# were wrong by just one or two characters. Slowly generated this list of 
# amended mappings to get the final plaintext before checking it exists in the 
# full, original text. 
mapping['A'] = 'W'
mapping['C'] = 'I'
mapping['D'] = 'R'
mapping['F'] = 'D'
mapping['H'] = 'G'
mapping['J'] = 'B'
mapping['L'] = 'S'
mapping['N'] = 'N'
mapping['P'] = 'V'
mapping['Q'] = 'O'
mapping['R'] = 'J'
mapping['U'] = 'L'
mapping['V'] = 'Z'
mapping['W'] = 'M'
mapping['X'] = 'K'
mapping['Y'] = 'C'
mapping['Z'] = 'X'
mapping['|'] = 'F'

for map in mapping.keys():
    print(map + ": " + mapping[map])

# Generate the plaintext
plaintext = ""
for letter in ciphertext:
    plaintext += mapping[letter]

print(plaintext)

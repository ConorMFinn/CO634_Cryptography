import string

# Take ciphertext from CLI
ciphertext = input()
ciphertext = ciphertext.upper()

alphabet = string.ascii_uppercase

# Key given by exercise
key = "TESSOFTHEDURBERVILLES"

plaintext = ""

# Use key to decrypt using position in alphabet of key letter to shift each ciphertext letter.
for i in range(0, len(ciphertext)):
    plaintext += alphabet[(alphabet.index(ciphertext[i]) - alphabet.index(key[i%len(key)])) % 26]

print(plaintext)

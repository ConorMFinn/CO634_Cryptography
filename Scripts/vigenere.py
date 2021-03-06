import string

ciphertext = input()
ciphertext = ciphertext.upper()

alphabet = string.ascii_uppercase

key = "TESSOFTHEDURBERVILLES"

plaintext = ""

for i in range(0, len(ciphertext)):
    plaintext += alphabet[(alphabet.index(ciphertext[i]) - alphabet.index(key[i%len(key)])) % 26]

print(plaintext)

import string

text = input()
text = text.upper()

alphabet = string.ascii_uppercase

counts = {}

for letter in alphabet:
    counts[letter] = 0

for char in text:
    counts[char] += 1

largest_letter = ""
largest_count = 0

for letter in alphabet:
    if counts[letter] > largest_count:
        largest_count = counts[letter]
        largest_letter = letter

print(largest_letter)

shift_e = alphabet.index(largest_letter) - alphabet.index("E")
shift_t = alphabet.index(largest_letter) - alphabet.index("T")
shift_a = alphabet.index(largest_letter) - alphabet.index("A")


decode_e = ""
for char in text:
    decode_e += alphabet[(alphabet.index(char) - shift_e) % 26]

decode_t = ""
for char in text:
    decode_t += alphabet[(alphabet.index(char) - shift_t) % 26]

decode_a = ""
for char in text:
    decode_a += alphabet[(alphabet.index(char) - shift_a) % 26]

print("E: \n" + decode_e + "\n")
print("T: \n" + decode_t + "\n")
print("A: \n" + decode_a + "\n")

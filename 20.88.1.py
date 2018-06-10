ask = input(" enter the letter :").lower()
letters = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in ask:
    if letter in alphabet:
        if letter not in letters :
            letters[letter] = 1
        else :
            letters[letter] += 1

for letter in sorted(letters):
    print(letter, letters[letter])
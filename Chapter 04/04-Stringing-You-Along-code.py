"Franz"

'Ferdinand'

"That is Franz's cat toy."

'The ball is Ferdinand\'s.'

"You can see the\nnewline character here."

print("But 'print' breaks\nthe line at the character.")

"""
I've broken
this string
over several lines.
"""

fix = """This fixes my
   problem with extra newlines."""

fix

print(fix)

"""A single quote (') and a double quote (")."""

"C:\\src\\code\\chapter-01"

r"C:\src\code\chapter-01"

print(r"There is no newline \n in this string.")

"Quantum" in "Quantum computing"

"QUANTUM" not in "Quantum computing"

"QUANTUM".casefold() in "Quantum computing".casefold()

"Charles Darwin".upper()

"CAUTION: HELMETS MUST BE WORN".lower()

"this NEEDS to look like A Sentence!".capitalize()

guitars = "Fender Gibson Taylor"
guitars[0]

guitars[-1]

guitars[-5]

guitars.find("o")

guitars.find("o", 12)

guitars.find("o", 2, 9)

letters = "abcd"
letters + "efg"

letters

letters += "efg"
letters

brands = [
    "Fender",
    "Gibson",
    "Ibanez"
    ]

"I own " + str(len(brands)) + " brands of guitars"

f"I own {len(brands)} brands of guitars"

f"This is 1/7 to 3 decimal places: {(1/7):.3f}"

f"This is 1/7 to 6 decimal places: {(1/7):.6f}"

f"{(1/7000):.5E}"

for j in [1, 141, 1441, 14441]:
    print(f"| {j:5} | {j*j:010} |")

words = ['If', 'you', 'have', 'a', 'list']

print("".join(words))

print(' '.join(words))

print('\n'.join(words))

"My favorite guitar is a Fender.".replace("Fender", "Gibson")

"My favorite guitar is a Fender.".replace("e", "E")

"My favorite guitar is a Fender.".replace("e", "E", 1)

"My favorite guitar is a Fender.".replace(" guitar", "")

characters = []

for c in "Fender":
    characters.append(c)

characters

guitars

for c in guitars:
    if c.isupper():
        print(c)

"".join([c for c
    in "OX63 5WC - SL46 3AP - BN96 0VU"
    if c.isdigit()])

for a, b in zip("123", [1, 2, 3]):
    print(f"{a = }   {b = }")

word = "sesquipedalianism"
len(word)

print(word[3:9])
print(word[:7])
print(word[7:])

print(word[::3])
print(word[::-1])

def validate(name):
    if name:
        if name[0] != '_' and not name[0].isalpha():
            return False
        for character in name[1:]:
            if character != '_' and not character.isalnum():
                return False
        return True
    return False

validate("")

validate("_")

validate("income2021")

validate("income_2021")

validate("income-2021")

validate("2021_income")

"##hashtaghashtag".startswith("##")

"##hashtaghashtag".startswith("##H")

text = "  SPECIAL  #  SALE  #  TODAY  "

text.split('#')

[word.strip() for word in text.split('#')]

[word.lstrip() for word in text.split('#')]

[word.rstrip() for word in text.split('#')]

"936g9477-A9y7-23j9-zz8r-387".split('-', 2)

"936g9477-A9y7-23j9-zz8r-387".rsplit('-', 2)


"z Fe" in "Franz Ferdinand"

"Ferd" not in "Franz Ferdinand"

"a aa aaa aaaa aaaaa".count("aa")

"a aa aaa aaaa aaaaa".count("aa", 8, 13)

len("a aa aaa aaaa aaaaa")

"a aa aaa aaaa aaaaa".find("B")

"a aa aaa aaaa aaaaa".find("aa")

"a aa aaa aaaa aaaaa".find("aa", 8, 13)

"a aa aaa aaaa aaaaa".rfind("B")

"a aa aaa aaaa aaaaa".rfind("aa")

"a aa aaa aaaa aaaaa".rfind("aa", 8, 13)

"a aa aaa aaaa aaaaa".index("aa")

"a aa aaa aaaa aaaaa".rindex("aa")

"# This is a Python comment".startswith('#')

"abcdef".startswith(('b', 'B'), 1)

"Is this a question?".endswith('?')

"This could be a sentence!".endswith(('.', '!', '?'))

"-A-A-A-A-A-A-A-".replace("-A-", "=B=")

"-A-A-A-A-A-A-A-".replace("-A-", "=B=", 2)

string = "Economic, ecological ecosystem"

def my_search(string, substring):
    if not string or not substring:
        return None

    def have_a_match(n):
        for m in range(0, len(substring)):
            if n >= len(string):
                return False
            if string[n] != substring[m]:
                return False

            n += 1
        return True

    for j in range(len(string)):
        if have_a_match(j):
            return (j, len(substring))

    return None

print(my_search(string, "Eco"))

print(my_search(string, "stem"))

print(my_search(string, "ABC"))

print(my_search(string, "ecom"))

print(my_search(string, "ecos"))

import re

string = "Economic, ecological ecosystem"

pattern = re.compile(r"ecos")
pattern

result = pattern.search(string)
print(result)

def print_match(result, group_number=0):
    if result is not None:
        # Display the matched substring
        print(f"group({group_number}) = "
              f'{result.group(group_number)}"  ', end="")

        # Display the starting index and index after end of match
        print(f"start({group_number}) = {result.start(group_number)}  "
              f"end({group_number}) = {result.end(group_number)}")
    else:
        print(None)


print_match(result)

pattern = re.compile(r"ecom")
print_match(pattern.search(string))

pattern = re.compile(r"eco[ls]")
pattern

result = pattern.search(string)
print_match(result)

pattern.findall(string)

pattern = re.compile("[e][c][o][ls]")
pattern.findall(string)

pattern = re.compile(r"eco[lns]", re.IGNORECASE)
pattern

print_match(pattern.search(string))

pattern.findall(string)

for match in pattern.finditer(string):
    print(match)

string = "[1] Sutor, Robert S. (2019). Dancing with Qubits."

def print_matches(string, pattern):
    for match in re.compile(pattern).finditer(string):
        print(match)

string = "economic ecosystem center"

# match 'e' followed by any lowercase letter

re.compile(r"e[a-z]").findall(string)

# match 'e' at the beginning of the string
# followed by any lowercase letter

re.compile(r"^e[a-z]").findall(string)

# match any character that is not 'e' that is
# followed by any lowercase letter

re.compile(r"[^e][a-z]").findall(string)

# match 'E' at the beginning of the string
# followed by any lowercase letter

re.compile(r"^E[a-z]").findall(string)

string = "economic ecosystem center"

pattern = re.compile(r"c e")
print_match(pattern.search(string))

pattern = re.compile(r"c\se")
print_match(pattern.search(string))

print_matches(string, r"c\s?e")

string = "economic ecosystem bookkeeping center"

print_matches(string, r"[eko]{2}")

re.compile(r"[cb]o*").findall(string)

re.compile(r"[cb]o+").findall(string)

string = "914-555-1234"

pattern = re.compile(r"[2-9]\d{2}-[2-9]\d{2}-\d{4}")
print_match(pattern.search(string))

string = "too much credit reduction can put you in the red"

print_matches(string, r"red")

print_matches(string, r"\bred\b")

print_matches(string, r"\bred")

print_matches(string, r"\Bred\B")

print_matches(string, r"red\B")

fstring = 'f"{x} {y} {A_1}"'

string = "Do you have the red piece, the green piece, and the blue piece?"

print_matches(string, r"(red)|(green)|(blue)")

print_matches(string, r"(red)|(green)|(blue) piece")

print_matches(string, r"((red)|(green)|(blue)) piece")

pattern = re.compile(r"\b([A-Z][a-z]*)\s+([A-Z])\.\s+([A-Z][a-z]*)\b")
result = pattern.search("My name is Robert S. Sutor")
print_match(result)

def print_match(result, group_number=0):
    if result is not None:
        # Display the matched substring
        print(f"group({group_number}) = "
              f'{result.group(group_number)}"  ', end="")

        # Display the starting index and index after end of match
        print(f"start({group_number}) = {result.start(group_number)}  "
              f"end({group_number}) = {result.end(group_number)}")
    else:
        print(None)


for g in range(1, 4):
    print_match(result, g)

len(result.groups())

pattern = re.compile(r"\b([A-Z]([a-z]*))\s+([A-Z])\.\s+([A-Z][a-z]*)\b")
result = pattern.search("My name is Robert S. Sutor")

for g in range(1 + len(result.groups())):
    print_match(result, g)

pattern= re.compile(r"\b(.+)\s+City\s+is\s+in\s+\1\b")

print_match(pattern.search("New York City is in New York"))

print_match(pattern.search("Iowa City is in Iowa"))

print_match(pattern.search("Jefferson City is in Missouri"))

pattern = re.compile(r"\b(?:[A-Z][a-z]*)\s+([A-Z])\.\s+(?:[A-Z][a-z]*)\b")
result = pattern.search("My name is Robert S. Sutor")
for g in range(1 + len(result.groups())):
    print_match(result, g)

pattern= re.compile(r"\b(?P<city>.+)\s+City\s+is\s+in\s+(?P=city)\b")

result = pattern.search("New York City is in New York")

result.group("city")

result.groupdict()

pattern = re.compile(r"\b([2-9]\d{2}-[2-9]\d{2}-\d{4})\b")

string = "My phone number is 914-555-1234."
result = pattern.search(string)
print_match(result, 1)

pattern.sub("***-***-****", string)

pattern.sub(r"+1-\1", string)

string = "212-555-0123   585-555-9876   320-555-3467"
pattern.sub("***-***-****", string)

pattern.sub(r"+1-\1", string, 2)

string = "212-555-0123   185-555-9876   320-555-3467"
pattern.subn("***-***-****", string)

string = "Hilbert 40 Charlie 35 Gideon 28"

pattern = re.compile(r"\s*\d{2}\s*")
pattern.split(string)

pattern = re.compile(r"(\s*\d{2}\s*)")
pattern.split(string)

pattern = re.compile(r"\s*(\d{2})\s*")
pattern.split(string)

the_text ="I'm making mor freid green tomatos."
the_text

corrections = {
  "accross":    "across",
  "definately": "definitely",
  "freid":      "fried",
  "mor":        "more",
  "neeed":      "need",
  "tomatos":    "tomatoes",
  "wierd":      "weird"
}

def clean_text(text):
    for wrong, right in corrections.items():
        text = text.replace(wrong, right)
    return text

result = clean_text(the_text)
result

clean_text(result)

import re

def clean_text(text):
    for wrong, right in corrections.items():
        pattern = re.compile(fr"\b({wrong})\b")
        text = pattern.sub(f"{right}", text)
    return text

result = clean_text(the_text)
result

clean_text(result)

from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor(case_sensitive=True)

for wrong, right in corrections.items():
    keyword_processor.add_keyword(wrong, right)

result = keyword_processor.replace_keywords(the_text)
result

keyword_processor.replace_keywords(result)

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("I'm making more fried green tomatoes.")

print(" | ".join([token.text for token in doc]))

for token in doc:
    print(f"{token.text:9} {token.lemma_:8} "
          f"{token.pos_:8} {token.dep_:8}")

from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I'm making more fried green tomatoes.")
format_options = {"distance": 125, "add_lemma": True}

doc = nlp("William Shakespeare ate crumpets in England in 1597.")

for ent in doc.ents:
    print(f'{ent.label_}: "{ent.text}"')

from spacy.matcher import Matcher

pattern = [
    {"TEXT": {"IN": ["I", "brother", "father", "mother", "sister"]}},
    {"OP": "*"},
    {"POS": "VERB", "LEMMA": {"IN": ["bake", "cook", "make"]}},
    {"OP": "*"},
    {"LEMMA": {"IN": ["cake", "peach", "bean", "pea", "tomato"]}}
]

def on_match(matcher, doc, id, matches):
    # Callback function for matcher
    # Show the span of text that we matched
    for id, start, end in matches:
        print(doc[start:end])

matcher = Matcher(nlp.vocab)
matcher.add("Cooking", [pattern], on_match=on_match)

doc = nlp("I'm making more fried green tomatoes.")
matches = matcher(doc)

matches = matcher(nlp("My sister cooked peas."))

matches = matcher(nlp("My father will bake three cakes."))

matcher.remove("Cooking")

pattern = [
    {"SHAPE": "ddd"}, {"TEXT": "-"},
    {"SHAPE": "ddd"}, {"TEXT": "-"},
    {"SHAPE": "dddd"}
]

matcher.add("PhoneNumber", [pattern], on_match=on_match)
matches = matcher(nlp("My phone number is 914-555-1234."))

pattern = [
    {"TEXT": {"REGEX": r"[2-9]\d{2}"}},
    {"TEXT": "-"},
    {"TEXT": {"REGEX": r"[2-9]\d{2}"}},
    {"TEXT": "-"},
    {"TEXT": {"REGEX": r"\d{4}"}}
]

matcher = Matcher(nlp.vocab)
matcher.add("PhoneNumber", [pattern], on_match=on_match)
matches = matcher(nlp("My phone number is 914-555-1234."))


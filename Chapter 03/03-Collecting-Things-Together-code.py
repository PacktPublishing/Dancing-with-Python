brands = ["Fender", "Gibson", "Ibanez"]
brands

[]

list()

len(brands)

len([])

brands = [
    "Fender",
    "Gibson",
    "Ibanez"
    ]

brands

brands[0]

brands[len(brands) - 1]

brands[-1]

brands[-len(brands)]

try:
    print(brands[10])
except:
    print("Whoops, something went wrong.")

print("We are still working after try!")

try:
    print(brands[2])
except:
    print("Whoops, something went wrong.")
else:
    print("We got the list item!")

print("We are still working after try!")

def try_try(n):
    try:
        print(brands[n])
    except:
        print("Whoops, something went wrong.")
        return 1
    else:
        print("We got the list item!")
        return 0
    finally:
        print("We can finalize processing here.")

try_try(2)

try_try(20)

def error_tester(index, divisor):
    try:
        print(brands[index // divisor])
    except IndexError as error:
        print(f"Index problem:\n'{error}'")
    except ZeroDivisionError:
        print("Did you mean to divide by 0?")
    except:
        print("Something unexpected happened.")

error_tester(6, 1)

error_tester(2, 0)

error_tester(4, "hello")

brands = [
    "Fender",
    "Gibson",
    "Ibanez"
    ]
brands_2 = brands

print(f"{brands = }")
print(f"{brands_2 = }")

del brands[2]
print(f"{brands = }")
print(f"{brands_2 = }")

brands.pop(0)

brands

brands.pop()

brands = [
    "Fender",
    "Gibson",
    "Ibanez"
    ]

original_brands = brands.copy()

brands.index("Ibanez")

try:
    del brands[brands.index("Ibanez")]
    print("'Ibanez' was present and was removed")
except ValueError:
    print("'Ibanez' was not present and so not removed")

brands

brands = original_brands.copy()

try:
    del brands[brands.index("Gretsch")]
    print("'Gretsch' was present and was removed")
except ValueError:
    print("'Gretsch' was not present and so not removed")

brands

brands = original_brands.copy()

try:
    brands.remove("Ibanez")
    print("'Ibanez' was present and was removed")
except:
    print("'Ibanez' was not present and so not removed")

brands

brands = original_brands.copy()

if "Ibanez" in brands:
    brands.remove("Ibanez")

brands

a = [1, 2, 3]
b = a
a = []
print(f"{a = }")
print(f"{b = }")

a = [1, 2, 3]
b = a
a.clear()
print(f"{a = }")
print(f"{b = }")

brands = original_brands.copy()

brands[2] = "Gretsch"
brands

array = [[1, 2], [3, 4]]
array

array[0]

array[0][1]

array[0][1] = 2.001

array

the_list = ["a", "b", "c", "d", "e", "f"]
the_list

the_list[0:]

the_list[:]

the_list[2:]

the_list[10:]

the_list[:2]

the_list[1:3]

the_list[::2]

the_list[1::3]

the_list[::-1]

the_list = ["a", "b", "c", "d", "e", "f"]

the_list[:1] = [1, 2, 3]
the_list

the_list[6:] = [7, 8, 9]
the_list

the_list[4:6] = ["alpha", "beta", "gamma"]
the_list

brands = [
    "Fender",
    "Gibson",
    "Ibanez"
    ]

original_brands = brands.copy()

brands.append("Gretsch")
brands

brands = original_brands.copy()
brands.insert(0, "Gretsch")
brands

brands = original_brands.copy()
brands.insert(1, "Gretsch")
brands

brands = original_brands.copy()
brands.extend(["Epiphone", "Paul Reed Smith"])
brands

brands = original_brands.copy()

for brand in ["Epiphone", "Paul Reed Smith"]:
    brands.append(brand)

brands

brands = original_brands.copy()

for brand in ["Epiphone", "Paul Reed Smith"]:
    brands.insert(0, brand)

brands

brands = original_brands.copy()
index = 0

for brand in ["Epiphone", "Paul Reed Smith"]:
    brands.insert(index, brand)
    index += 1

brands

models = [
    "Stratocaster",
    "Telecaster",
    "Les Paul",
    "Flying V",
    "RG"
    ]

first_model, *remaining_models = models

first_model

remaining_models

*starting_models, last_model = models

starting_models

last_model

first_model, *middle_models, last_model = models

first_model

middle_models

last_model

years = [1954, 1950, 1952, 1958, 1987]
years

years.reverse()
years

years.sort()
years

years.sort(reverse=True)
years

years = [1954, 1950, 1952, 1958, 1987]
years

sorted(years)

years

a, b = 3, -2
print(f"{a = }   {b = }")

a, b = (9, 0.3)
print(f"{a = }   {b = }")

(a, b) = ("a", "b")
print(f"{a = }   {b = }")

t = 2, -4, 9
t
list(t)
tuple([-16, 25, -36])

(3.14)

(3.14,)

def quo_rem(dividend, divisor):
    if not isinstance(dividend, int):
        raise TypeError("dividend must be an integer")
    if not isinstance(divisor, int):
        raise TypeError("divisor must be an integer")

    if divisor == 0:
        raise ZeroDivisionError("divisor is 0")

    return dividend // divisor, dividend % divisor

quo_rem(11, 4)

tens = [10, 20, 30, 40]

index = 0
for item in tens:
    print(f"[{index}] {item}")
    index += 1

for index in range(len(tens)):
    print(f"[{index}] {tens[index]}")

for index, item in enumerate(tens):
    print(f"[{index}] {item}")

brands = ["Fender", "Gibson", "Ibanez"]
brands.copy()

brands[:]

[brand for brand in brands]

brands_copy = []

for brand in brands:
    brands_copy.append(brand)

brands_copy

[brand for brand in brands if brand[1] in "aeiou"]

brands_filtered = []

for brand in brands:
    if brand[1] in "aeiou":
        brands_filtered.append(brand)

brands_filtered

[brand for brand in brands
    if len(brand) > 1 and brand[1] in "aeiou"]

[brand.upper() for brand in brands
    if len(brand) > 1 and brand[1] in "aeiou"]

[x**2 for x in range(13) if x % 3 == 0]

m = [[0 for i in range(4)] for j in range(4)]
m

for i in range(4): m[i][i] = 1
m

def one_or_zero(x, y):
    if x == y:
        return 1
    return 0

[[one_or_zero(i, j) for i in range(4)] for j in range(4)]

def one_or_zero(x, y): return 1 if x == y else 0

[[one_or_zero(i, j) for i in range(4)] for j in range(4)]

[[1 if i == j else 0 for i in range(4)] for j in range(4)]

[f"i + j = {i+j} for {i = } and {j =}"
    for i in range(2) for j in range(3)]

brands = ["Fender", "Fender", "Gibson",
    "Gibson", "Ibanez"]
models = ["Stratocaster", "Telecaster",
    "Les Paul", "Flying V", "RG"]
years = [1954, 1950, 1952, 1958, 1987]

for brand, model, year in zip(brands, models, years):
    print(f"The {brand} {model} was first introduced in {year}.")

for number, brand, model, year in \
    zip(range(len(brands)), brands, models, years):
        print(f"{number + 1}. The {brand} {model} "
            + f"was first introduced in {year}.")

{}

dict()

{"Fender Stratocaster": 1954, "Fender Telecaster": 1950}

guitars = {
    "Fender Stratocaster": 1954,
    "Fender Telecaster": 1950,
    "Gibson Les Paul": 1952,
    "Gibson Flying V": 1958,
    "Ibanez RG": 1987
    }

if guitars:
    print("Our guitar dictionary is not empty.")

len(guitars)

"Fender Stratocaster" in guitars

"Martin BC-16E" not in guitars

guitars["Gibson Les Paul"]

3 is None

"None" is not None

None is None

guitars.get("Gibson Les Paul")

guitars.get("Martin BC-16E") is None

guitars.get("Martin BC-16E", "Sometime in the 20th century")

for model in guitars: print(model)

for year in guitars.values(): print(year)

for model, year in guitars.items():
    print(f"The {model} was introduced in {year}")

for model in reversed(sorted(guitars)): print(model)

numbers = {1: "one", 2: "two"}

numbers[3] = "three"

numbers

numbers[3] = "THREE"

numbers

other_numbers = {4: "four", 5: "five"}

{**numbers, **other_numbers}

numbers

del numbers[2]
numbers

numbers.clear()
numbers

{model : year for model, year
    in guitars.items() if 1950 < year and year < 1958}

{year : model.upper() for model, year
    in guitars.items() if 1955 < year}

my_brands = {"Fender", "Fender", "Ovation", "Ovation", "Gibson"}
their_brands = {"Gibson", "Gibson", "Gretsch", "Fender"}

my_brands

len(my_brands)

their_brands

len(their_brands)

my_original_brands = my_brands.copy()
their_original_brands = their_brands.copy()

set()

isinstance({ }, dict)

type({ })

set(["b", "o", "b"])

set(("b","o","o","k","k","e","e","p","i","n","g"))

"Gibson" in my_brands

"Ibanez" in my_brands

"Gretsch" not in my_brands

my_brands.add("Ibanez")
my_brands

my_brands.update(their_brands)
my_brands

their_brands.clear()
their_brands

my_brands.discard("Ibanez")
my_brands

for brand in my_brands: print(brand)

my_brands
my_brands.pop()

my_brands

my_brands = my_original_brands.copy()
my_brands

their_brands = their_original_brands.copy()
their_brands

print(my_brands == my_brands)
print(my_brands == their_brands)
print(my_brands != their_brands)

print({"Gibson"} <= my_brands)
print(my_brands <= my_brands)
print(my_brands < my_brands)

print(my_brands > {"Gibson", "Ovation"})
print(my_brands >= {"Gibson", "Ovation"})
print(my_brands > my_brands)

my_brands.union({"Martin", "Taylor"})

guitars = my_brands.copy()
guitars | {"Martin", "Taylor"}

guitars |= {"Martin", "Taylor"}
guitars

my_brands.intersection(their_brands)

my_brands & their_brands

my_brands.difference(their_brands)

my_brands - their_brands

[i * j for i in range(1,5) for j in range(2,5)]

{i * j for i in range(1,5) for j in range(2,5)}


-4

0

837375400388826538847463290993837000004846673

-3.6836

17.9817359935767429962445362777253636

10000000000000000000000000000000000000000000000000000.1

1_000_000_000

'Better a witty fool, than a foolish wit.'

"Some are born great, others achieve greatness."

"I use single quotes around single characters like 'Z'."

'I\'ll use a backslash in front of my single quote.'

[12, 16, 19]

["Robin", "Robert", "Roberta"]

["Robin", 12, "Robert", 16, "Roberta", 19]

ages = [12, 16, 19]

ages

len(ages)

ages[0]

"Maria"[1]

robins_age, roberts_age, robertas_age = ages

robins_age

roberts_age

robertas_age

a = b = 10
a

b

m, n = 17, 6

not True

not False

a = 10
-a == -10

a == "10"

str(a)

str(a) == "10"

"London" != "london"

3 < 4

-3 <= -4

20 > -6

0 >= 0.01

m, n = 17, 6

m + n

-n

n - m

m * n

5 * 3.4

5 * 3.0

a = 100000000000000000000

b = 100000000000000000000.

a == b

100000000000000000000 == 100000000000000000000.1

2.75/4.0

2.75/4

11/4

-13/5

11 // 4

11 % 4

quotient, remainder = divmod(-13, 5)

quotient

remainder

quotient * 5 + remainder

4**3

4**-3

1/(4**3)

abs(78.3)

abs(0)

abs(-3)

round(2.7)

round(-7.51)

round(2.71828, 2)

round(714, 0)

round(714, 2)

round(714, -2)

round(83567356.3846, -5)

max(0, 19.7)

min(0, 19.7)

max(0, 19.7, -8, 33.2)

min(0, 19.7, -8, 33.2)

max([0, 19.7, -8, 33.2])

min([0, 19.7, -8, 33.2])

count = 0
count

count = count + 1
count

count = 0
count += 1
count

quote = "perchance to dream"
quote

quote_length = len(quote)
quote_length

quote[0]

quote[quote_length - 1]

quote[-1]

quote[-quote_length]

quote

quote.find("dream")

quote.find("snooze")

quote

quote.find('a', 7)

quote.find('a', 3, 8)

quote.find('a', 0, 4)

"dream" in quote

"nightmare" in quote

"Hamlet" not in quote

quote

quote[3:9]

quote[:5]

quote[5:]

"Finely baked bread"

"Finely baked bread" + " available today!"

text = "la "
text + text + text

3 * text

10 * text

0 * text

a = 2
b = 5
f"The sum of a and b is {a + b}"

years = [2021, 1983, 1976, 1997, 1990]
years

len(years)

years[0]

years[-2]

years[1:3]

years[0] = 2000
years

letters = "abcd"
letters

letters = "A" + letters[1:]
letters

years = [2021, 1983, 1976, 1997, 1990]
years

years + [1961, 1980]

years

years.extend([1961, 1980])
years

years.append(2012)
years

years.insert(1, 1812)
years

years.pop(1)

years

years.pop()

years

"This is a sample string"

print("This is a sample string")

print(17 + 4)

print(57, 99, -4.3)

print("Last year's revenue was " + "3" + " million euros")

print("Last year's revenue was " + str(3) + " million euros")

print(f"Last year's revenue was {3} million euros")

"Don't use \"odd\" quoted words in your prose."

"See how I broke\nthis line?"

print("See how I broke\nthis line?")

print("First string")
print("Second string")

print("First string", end=' ')
print("Second string")

1 + 2 + 3 + 4 + 5

sum, count = 0, 1

while count <= 500:
    sum += count
    count += 1

sum

sum, count = 0, 1

while count <= 5:
    sum += count
    count += 1
    print(f"{count = } and {sum = }")

sum

sum, count = 0, 1

while True:
    sum += count
    count += 1
    if count > 500:
        break

sum

sum, count = 0, 1

while count <= 500:
    if count % 2 == 0:
        count += 1
        continue

    sum += count
    count += 1

sum

sum = 0

for count in range(1, 501):
    sum += count

sum

sum = 0

for count in range(1, 501, 2):
    sum += count

sum

for year in [2020, 2022, 2025, 2026]:
    print(year)

for character in "abc":
    print(character)

string = "Zdrasti"

for index in range(len(string)):
    print(string[0:index + 1])

[x*x for x in range(1, 6)]

def identity(x):
    return x

identity(7)

identity("just a string")

identity(["one", 2, 3.0])

def double(x):
    return 2 * x

double(7)

double("just a string")

double(["one", 2, 3.0])

def half(x):
    return x // 2

half(7)

numbers = [3, 2, 1, 4]

for index in range(1, 4):
    if numbers[0] > numbers[index]:
        numbers[0], numbers[index] = numbers[index], numbers[0]

numbers

def least_first(items):
    for index in range(1, len(items)):
        if items[0] > items[index]:
            items[0], items[index] = items[index], items[0]
    return items

least_first([3, 2, 1, 4])

least_first([5, -1, 8, -3, 0])

least_first([10])

least_first([])

def selection_sort(items):
    for i in range(0, len(items) - 1):
        for j in range(i + 1, len(items)):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
    return items

selection_sort([3, 2, 1, 4])

selection_sort([5, -1, 8, -3, 0])

selection_sort([10])

selection_sort([])

def nested_selection_sort(items):
    def test_and_swap(first_index, second_index):
        if items[first_index] > items[second_index]:
            items[first_index], items[second_index] = \
                items[second_index], items[first_index]

    for i in range(0, len(items) - 1):
        for j in range(i + 1, len(items)):
            test_and_swap(i, j)

    return items

nested_selection_sort([3, 2, 1, 4])

def recursive_selection_sort(items, first_index=0):
    if first_index < len(items) - 1:
        for second_index in range(first_index + 1, len(items)):
            if items[first_index] > items[second_index]:
                items[first_index], items[second_index] = \
                    items[second_index], items[first_index]
        recursive_selection_sort(items, first_index + 1)

    return items

recursive_selection_sort([3, 2, 1, 4])

def do_nothing():
    # do_nothing does nothing whatsoever
    pass


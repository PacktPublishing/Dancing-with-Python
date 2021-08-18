"C:\\src\\part-I\\Working-with-Files.html"

r"C:\src\part-I\Working-with-Files.html"

import os

pn = "/src/part-I/Working-with-Files.html"

os.path.split(pn)

os.path.basename(pn)

os.path.splitext(pn)

os.path.splitext(os.path.basename(pn))

os.path.splitdrive("C:\\src\\part-I\\Working-with-Files.html")

mod_time = os.path.getmtime("src/part-I/Working-with-Files.html")
mod_time

import time

time.gmtime(mod_time)

time.asctime(time.gmtime(mod_time))

f'{os.path.getsize("src/part-I/Working-with-Files.html"):,} bytes'

os.path.exists("src/part-I/Working-with-Files.html")

os.path.exists("src/part-I")

os.path.isfile("src/part-I/Working-with-Files.html")

os.path.isfile("src/part-I/Working-with-Flies.html")

os.path.isfile("src/part-I")

os.path.isdir("src/part-I/Working-with-Files.html")

os.path.isdir("src/part-I")

import glob

for html_file in glob.iglob("src/part-I/*.html"):
    html_file = os.path.normcase(html_file)
    print(html_file)

directories = []

for name in glob.iglob("src/**", recursive=True):
    if os.path.isdir(name):
        dir = os.path.normcase(name)
        directories.append(dir)

print(directories)

len(os.listdir("src/part-I"))

input_file = open("src/examples/sonnet-18.txt", "r")
content = input_file.read()
input_file.close()

print(content)

count = 0
for c in content:
    if c == 'a':
        count += 1

count

input_file = open("src/examples/sonnet-18.txt", "r")
content = input_file.readlines()
input_file.close()

print(content)

input_file = open("src/examples/sonnet-18.txt", "r")

line_number = 0
line = input_file.readline()

while line:
    line_number += 1
    print(f"{line_number:>2}  {line.upper()}", end="")
    line = input_file.readline()  # Don't forget this!

input_file.close()

input_file = open("src/examples/sonnet-18.txt", "rb")
content = input_file.read(39)
input_file.close()

content

type(content)

content[0]

bin(content[0])  # binary

hex(content[0])  # hexadecimal

s = "Sîne klâwen æðelen ᚷᛖ ᚻᚹ ᛦᛚ ᚳᚢ ᛗ"

t = s.encode("utf-8")
t

t.decode("utf-8")

s == t

with open("src/examples/sonnet-18.txt", "r") as input_file:
    print(input_file.readline())

guitars = {
    "Fender Stratocaster": 1954,
    "Fender Telecaster": 1950,
    "Gibson Les Paul": 1952,
    "Gibson Flying V": 1958,
    "Ibanez RG": 1987
    }

import pickle

with open("work/pickle_example", "wb") as pickle_file:
    pickle.dump(guitars, pickle_file)

with open("work/pickle_example", "rb") as pickle_file:
    new_guitars = pickle.load(pickle_file)

print(new_guitars)

guitars == new_guitars

from src.code.unipoly import *

t = UniPoly(1, 't', 1)
p = (t**3 - 7)**5
p

with open("work/pickle_example", "wb") as pickle_file:
    pickle.dump(p, pickle_file)

with open("work/pickle_example", "rb") as pickle_file:
    new_p = pickle.load(pickle_file)

p == new_p

import json

with open("src/examples/example.json", 'r') as input_file:
    json_ = json.load(input_file)

type(json_)

json_

json_string = json.dumps(json_, indent=4, sort_keys=True)
print(json_string)

with open("work/new_example.json", 'w') as output_file:
    json.dump(json_, output_file, indent=4, sort_keys=True)


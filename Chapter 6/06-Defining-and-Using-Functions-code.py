for i in range(6):
    if i % 2 == 1:
        print(f"{i} ", end="")

def odd_numbers_less_than(n):
    # this function prints out all odd numbers greater
    # than 0 and less than n
    for i in range(n):
        if i % 2 == 1:
            print(f"{i} ", end="")

odd_numbers_less_than(9)

odd_numbers_less_than(16)

def f():
    pass

import datetime
import time

def print_the_time():
    print(datetime.datetime.now().strftime("%H:%M:%S"))

print_the_time()

time.sleep(2.0)

print_the_time()

def print_the_time(delay_in_seconds):
    # print the current time after waiting delay_in_seconds
    time.sleep(delay_in_seconds)
    print(datetime.datetime.now().strftime("%H:%M:%S"))

print_the_time(0.0)

print_the_time(1.0)

def format_text(text, make_uppercase):
    if make_uppercase:
        print(text.upper())
    else:
        print(text)

format_text("this text is not uppercase", False)

format_text("this text is uppercase", True)

def sort_and_print_5(z1, z2, z3, z4, z5):
    for z in sorted([z1, z2, z3, z4, z5]):
        print(f"{z} ", end="")

sort_and_print_5(4, 2, -9, 0, 3)

def sort_and_print(numbers):
    for z in sorted(numbers):
        print(f"{z} ", end="")

sort_and_print([4, 2, -9, 0, 3])

def sort_and_print(*numbers):
    for z in sorted(numbers):
        print(f"{z} ", end="")

sort_and_print(4, 2, -9, 0, 3)

def sort_and_print(ascending, *numbers):
    if ascending:
        for z in sorted(numbers, reverse=False):
            print(f"{z} ", end="")
    else:
        for z in sorted(numbers, reverse=True):
            print(f"{z} ", end="")

sort_and_print(False, 4, 2, -9, 0, 3)

sort_and_print(True, 4, 2, -9, 0, 3)

def expander3(a, b, c):
    print(f"{a = }  {b = }  {c = }")

numbers = [10, 20, 30]
expander3(*numbers)

text = "can   you see  multiple   spaces?"
text

for _ in range(3):
    text = text.replace("  ", " ")

text

quo, _ = divmod(37, 5)
quo

_, b, _, d = 10, 20, 30, 40
b + d

import_ = "to bring items into a country for sale"

def f():
    pass

type(f())

f() is None

def f():
    return

f() is None

def g(x, y):
    return x + y

g(10, 23)

def bad_g(x, y):
    x + y

bad_g(10, 23) is None

def bad_abs(x):
    if x < 0:
        return -x
    x

bad_abs(-2)**3

bad_abs(5) is None

def h(x, y):
    return x + y, x *y

type(h(10, 15))

sum, product = h(10, 15)

print(f"{sum = }   {product = }")

def f(x):
    return x * x
    return x + x

def isvowel(text):
    # return True if text is empty or composed only of English vowels

    result = True
    for c in text:
        if c not in "aeiouAEIOU":
            result = False
            break
    return result

isvowel("Eeeuuu"), isvowel("Woohoo")

def isvowel(text):
    # return True if text is empty or composed only of English vowels

    for c in text:
        if c not in "aeiouAEIOU":
            return False
    return True

isvowel("Eeeuuu"), isvowel("Woohoo")

import math

def raiser(base, exponent):
    return math.pow(base, exponent)

raiser(2, 3)

raiser(base=2, exponent=3)

raiser(exponent=3, base=2)

raiser(2, exponent=3)

def raiser(*, base, exponent):
    return math.pow(base, exponent)

def pick_an_argument(*args, k):
    return args[k]

pick_an_argument("one", "two", "three", k=1)

def show_keyword_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key = }   {value = }")

show_keyword_args(x=1, y=2, z=3)

def raiser(**kwargs):
    if "base" in kwargs and "exponent" in kwargs:
        return math.pow(kwargs["base"], kwargs["exponent"])
    return "I do not know what you are trying to do"

raiser(exponent=3, base=2)

raiser(sugar=3, flour=2)

print("a string")

print("'a string with quotes'")

print(57.4 / 8)

print('q', 'u', 'a', 'n', 't', 'u', 'm')

print('q', 'u', 'a', 'n', 't', 'u', 'm', sep='_')

for i in range(10, 0, -1):
    print(i, end=' ')
print("launch!")

def display_string(the_string, put_in_uppercase=False):
    if put_in_uppercase:
        print(the_string.upper())
    else:
        print(the_string)

display_string("This is the default behavior")

display_string("This overrides the default behavior", True)

display_string("This is not uppercased", put_in_uppercase=False)

def f(x, y):
    w = 10
    def g(z):
        return z**3 + w
    return  g(x + y)

f(2, 3)

def f(x, y):
    def g():
        def h():
            # if x + y == 10, return all the way out
            # of f with True, otherwise return False to g
            ...

        h()
    g()
    return None

my_variable = "SET AT GLOBAL SCOPE"
print(f"Global: {my_variable}")

def f():
    print(f"Inside f: {my_variable}")

f()

print(f"Global: {my_variable}")

my_variable = "SET AT GLOBAL SCOPE"
print(f"Global: {my_variable}")

def g():
    my_variable = "SET IN g"
    print(f"Inside g: {my_variable}")

g()

print(f"Global: {my_variable}")

my_variable = "SET AT GLOBAL SCOPE"
print(f"Global: {my_variable}")

def g():
    global my_variable
    my_variable = "SET IN g WITH 'global'"
    print(f"Inside g: {my_variable}")

g()

print(f"Global: {my_variable}")

RGB_BLACK = (0x00, 0x00, 0x00)
RGB_WHITE = (0xFF, 0xFF, 0xFF)
RGB_RED   = (0xFF, 0x00, 0x00)
RGB_GREEN = (0x00, 0xFF, 0x00)
RGB_BLUE  = (0x00, 0x00, 0xFF)

my_variable = "SET AT GLOBAL SCOPE"
print(f"Global: {my_variable}")

def h():
    my_variable = "SET IN h"
    print(f"Inside h: {my_variable}")
    def inner_h():
        my_variable = "SET IN inner_h"
        print(f"Inside inner_h: {my_variable}")
    inner_h()
    print(f"Inside h: {my_variable}")

h()

print(f"Global: {my_variable}")

my_variable = "SET AT GLOBAL SCOPE"
print(f"First global: {my_variable}")

def h():
    my_variable = "SET IN h"
    print(f"In h: {my_variable}")
    def inner_h():
        global my_variable
        my_variable = "SET IN inner_h"
        print(f"In inner_h: {my_variable}")
    inner_h()
    print(f"In h: {my_variable}")

h()

print(f"Global: {my_variable}")

my_variable = "SET AT GLOBAL SCOPE"
print(f"Global: {my_variable = }")

def h():
    my_variable = "SET IN h"
    print(f"In h: {my_variable = }")
    def inner_h():
        nonlocal my_variable
        my_variable = "SET IN inner_h"
        print(f"In inner_h: {my_variable = }")
    inner_h()
    print(f"In h: {my_variable = }")

h()

print(f"Global: {my_variable = }")

def f():
    print("I am inside the original definition of 'f'")

f()

g = f
g()

def f():
    print("I am inside the new definition of 'f'")

f()

g()

def adder(x, y): return x + y
def subtracter(x, y): return x - y
def multiplier(x, y): return x * y
def divider(x, y): return x / y

operations = {
    "+": adder,
    "-": subtracter,
    "*": multiplier,
    "/": divider,    # this trailing comma is ok
}

def calculator(digit_op_digit):
    # The left operand is a single digit. Convert it to an int.
    left = int(digit_op_digit[0])

    # Get the operation helper function
    operation = operations[digit_op_digit[1]]

    # The right operand is a single digit.
    right = int(digit_op_digit[2])

    # Apply the retrieved function to the arguments.
    return operation(left, right)

calculator("2+3")

calculator("7-9")

calculator("4*6")

calculator("8/4")

def adder(x, y): return x + y
def subtracter(x, y): return x - y
def multiplier(x, y): return x * y
def divider(x, y): return x / y

operations = {
    "+": adder,
    "-": subtracter,
    "*": multiplier,
    "/": divider
}

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

operations["-"](12.4, 0.4)

# Don't do this even though it works
f = lambda x: x**2

f(100)

from math import sin

# Don't do this even though it works

[(lambda x: sin(x))(y) for y in range(4)]

# This works as-is

[sin(y) for y in range(4)]

from functools import reduce

def caf(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

[(n, caf(n)) for n in range(1, 6)]

def recursive_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Argument must be a non-negative integer.")
    if n < 2:
        return 1
    return n * recursive_factorial(n - 1)

def iterative_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Argument must be a non-negative integer.")

    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

iterative_factorial(12)

iterative_factorial(1000)

def gcd(x, y, step=1):
    print(f"-> {step:>2}: {x = }  {y = }")
    x, y = abs(x), abs(y)

    if x < y:
        x, y = y, x

    if y == 0:
        return x

    # at this point, we know that x and y and positive integers > 1
    # with x >= y > 0

    return gcd(x - y, y, step + 1)

print(f"\ngcd = {gcd(-24, 400)}")

def gcd(x, y, step=1):
    print(f"-> {step:>2}: {x = }  {y = }")
    x, y = abs(x), abs(y)

    if x < y:
        x, y = y, x

    if y == 0:
        return x

    # at this point, we know that x and y and positive integers > 1
    # with x >= y > 0

    return gcd(y, x % y, step + 1)

print(f"\ngcd = {gcd(-24, 400)}")

print(f"\ngcd = {gcd(2**20 * 3**30, 2**30 * 3**20)}")

def gcd(x, y, step=1):
    print(f"-> {step:>2}: {x = }  {y = }")
    x, y = abs(x), abs(y)

    if x < y:
        x, y = y, x

    if y == 0:
        return x

    while y != 0:
        x, y = y, x % y

    return x

print(f"\ngcd = {gcd(-24, 400)}")

def recursive_fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Argument must be a non-negative integer.")

    if n < 2:
        return n

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

for j in range(16):
    print(f"{recursive_fibonacci(j)} ", end="")

def cached_fibonacci(n, cache=None):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Argument must be a non-negative integer.")

    if n < 2:
        return n

    if cache is None:
        cache = {0:0, 1:1}

    # Compute Fibonacci(n - 1) first, thereby calculating all
    # Fibonacci values for values less than n - 1

    if n - 1 in cache:
        fibonacci_n_minus_1 = cache[n - 1]
    else:
        cache[n - 1] = fibonacci_n_minus_1 = cached_fibonacci(n - 1, cache)

    # I know we have computed Fibonacci(n - 2)

    result = cache[n] = fibonacci_n_minus_1 + cache[n - 2]
    return result

for j in range(16):
    print(f"{cached_fibonacci(j)} ", end="")

def iterative_fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Argument must be a non-negative integer.")

    if n < 2:
        return n

    a, b, m = 0, 1, 2

    while m < n:
        a, b, m = b, a + b, m + 1

    return a + b

for j in range(16):
    print(f"{iterative_fibonacci(j)} ", end="")

import time

def time_a_fib(n, fib_function, fib_function_name):
    # time_a_fib computes a fibonacci value for n.
    # fib_function is the function object and
    # fib_function_name is a string with the function's name

    start_time = time.time()
    fib_function(n)
    elapsed_time = round((time.time() - start_time), 9)
    print(f"{fib_function_name}({n}) "
          f"took {elapsed_time} seconds")

time_a_fib(30, recursive_fibonacci, "recursive_fibonacci")
time_a_fib(30, cached_fibonacci, "cached_fibonacci")
time_a_fib(30, iterative_fibonacci, "iterative_fibonacci")

time_a_fib(999, cached_fibonacci, "cached_fibonacci")
time_a_fib(999, iterative_fibonacci, "iterative_fibonacci")

time_a_fib(20000, iterative_fibonacci, "iterative_fibonacci")


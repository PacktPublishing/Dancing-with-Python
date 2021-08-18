import math

math.e

math.factorial(10)

def factorial(n):
    print("Using my factorial")

    if n < 2:
        return 1

    return n * factorial(n - 1)

factorial(5)

math.factorial(5)

import math as maths

maths.cos(maths.pi)

from math import factorial as fac

fac(3)

factorial(3)

from math import factorial

factorial(5)

from math import pi, sin

sin(pi/4)

from math import *

log2(1024)

%reset -f

2**64 - 1

2.0**150

2**150

import math

math.factorial(4)

math.perm(4, 2)

math.comb(4, 4)

for m in (2, 3, 5, 7):
    if 14 % m == 0:
        print(f"14 is divisible by {m}")
    else:
        print(f"14 is not divisible by {m}")

import inspect
import math


def sieve_of_eratosthenes(n):
    # Return a list of the primes less than or equal to n.
    # First check that n is an integer greater than 1.

    if not isinstance(n, int) or not n > 1:
        print(
            "The argument to sieve_of_eratosthenes "
            "must be an integer greater than 1.")
        return []

    # Make a list holding the integers from 0 to n.

    potential_primes = list(range(n + 1))

    # If index is not prime, set potential_primes[index] to 0.
    # We start with 0 and 1

    potential_primes[0] = 0
    potential_primes[1] = 0

    p = 2  # 2 is prime, so start with that.

    while p <= n:
        # If at an index whose value in potential_primes
        # is not 0, it is prime.

        if potential_primes[p]:
            i = 2 * p

            # Mark p+p, p+p+p, etc. as not prime.
            while i <= n:
                if i != p:
                    potential_primes[i] = 0
                i += p
        p += 1

    # The only non-zero integers left in potential_primes
    # are primes. Return a list of those.

    return [prime for prime in potential_primes if prime]


def simple_factor(n):
    # factor the integer n by trial division

    if not isinstance(n, int) or not n > 1:
        print(
            "The argument to simple_factor "
            "must be an integer greater than 1.")
        return []

    primes_to_check = sieve_of_eratosthenes(math.isqrt(n))
    prime_factors = []

    for prime in primes_to_check:
        while n % prime == 0:
            prime_factors.append(prime)
            n = n // prime

    return prime_factors


print(inspect.getsource(sieve_of_eratosthenes))

sieve_of_eratosthenes(35)

import math

math.isqrt(63)

math.isqrt(64)

math.isqrt(65)

print(inspect.getsource(simple_factor))

f10 = math.factorial(10)

print(f"The prime factors of 10! = {f10} are\n"
      f"{simple_factor(f10)}")

math.gcd(12, 15)

12 * 15 // math.gcd(12, 15)

bin(72)

0b1001000

int("-32856")

b = bin(100)
b

int(b, base=2)

for n in range(8):
    m = n + 8
    print(f"{n:01x}   {n:2}   {n:04b}        "
          f"{m:01x}   {m:2}   {m:04b}")

hex(100)

hex(252)

right_arrow = "→"

-3.9005

1.1456e-4

f = -9E100
f

type(f)

1/7

0.10101010101010101010101010101010101

1e1000000000000000000000000

float("inf")

-1e1000000000000000000000000

float("-inf")

float("inf") + 3

2e8383747474847474747 == 9e3838399227273898383

float("inf") + float("inf")

float("inf") - float("inf")

float("inf") / float("inf")

round(8356.92665, 2)

round(8356.92665, -2)

[math.floor(-1.2,), math.ceil(-1.2), math.floor(1.2), math.ceil(1.2)]

math.pi

math.tau

math.degrees(2 * math.pi)

math.radians(270) / math.pi

math.asin(-1.0)

math.tan(1.0)

math.sin(1.0) / math.cos(1.0)

math.cos(math.pi/2)

math.isclose(math.cos(math.pi/2), 0.0, abs_tol=1e-15)

math.e

math.exp(0.0)

math.exp(1.0)

math.exp(4.5)

def compound_continuously(principal, annual_rate, years):
    return principal * math.exp(annual_rate * years)

compound_continuously(100, 0.02, 1)

compound_continuously(100, 0.02, 35)

y = math.pow(8.0, 3.0)
y

math.pow(y, 0.333333333333333)

math.sqrt(105.0)

math.log2(16)

math.log10(10**8)

math.log2(2*2*2*2*2)

def mystery_function(n):
    return math.trunc(math.log2(n))

from fractions import Fraction

Fraction(6, 5)

f = Fraction(20, 30)
f

f.numerator

f.denominator

import math

math.gcd(f.numerator, f.denominator)

Fraction(1, -5)

- Fraction(3, 7)

a = Fraction(2, 3)
b = Fraction(7, 4)

2 * a

a + b

a - b

a * b

1 / b

a / b

a ** 4

a ** -2

f = float(a)
f

Fraction(f)

Fraction(0.125)

Fraction(0.1)

import cmath

cmath.sqrt(-1.0)

z = complex(1.5, -2)
z

z.real

z.imag

3.4 - 8.03j

print(f"{math.sqrt(4)}   {cmath.sqrt(4)}")

print(f"{math.sin(0)}   {cmath.sin(0)}")

type(1j)

isinstance(1j, complex)

(3 + 4j).conjugate()

abs(0.5 - 0.25j)

z = 3 + 4j
w = 2 - 1j

r, phi = cmath.polar(3 + 4j)

z = complex(-5.0 * math.sqrt(2.0) / 4.0,
            -5.0 * math.sqrt(2.0) / 4.0)

r, phi = p = cmath.polar(z)

print(f"{z = }\n{r = }\n{phi = }")

-3 * math.pi / 4

cmath.rect(r, phi)

import sympy as sym

x = sym.Symbol('x')
p = x**3 - 2*x**2 - 5*x + 6
p

sym.factor(p)

p.subs(x, 3)

sym.limit(p, x, 3)

sym.diff(p, x)

sym.integrate(p, x)

import random

[random.randint(1, 10) for i in range(6)]

[random.randint(1, 10) for i in range(6)]

random.seed(10)
[random.randint(1, 10) for i in range(6)]

random.seed(10)
[random.randint(1, 10) for i in range(6)]

[random.random() for i in range(3)]

[random.uniform(0, 2) for i in range(3)]

card_deck = []

for suit in ("C", "D", "H", "S"):
    # create cards with rank 2 through 10
    for rank in range(2, 11):
        card_deck.append(f"{rank}{suit}")

    # create cards for jacks, queens, kings, and aces
    for rank in ("J", "Q", "K", "A"):
        card_deck.append(f"{rank}{suit}")

def print_cards(cards):
    # print the cards with up to 13 cards per row

    for card, n in zip(cards, range(1, len(cards) + 1)):
        print(f"{card:3}", end="  ")
        if n % 13 == 0:
            print()

print_cards(card_deck)

random.shuffle(card_deck)
print_cards(card_deck)

random.sample(card_deck, 5)

random.choice(card_deck)

random.choice(list({1, 2, 3, 4, 5}))

numbers = {0: "zero", 1: "one", 2: "two"}
key = random.choice(list(numbers.keys()))
key

numbers[key]

import qiskit

draw_kwargs = {
    "output": "mpl",         # use matplotlib
    "cregbundle": False,     # separate classical register wires
    "initial_state": True,   # show |0> and 0
    "idle_wires": False,     # don't show unused wires

    "style": {
        "name": "bw",        # black-and-white for book
        "subfontsize": 9,    # font size of subscripts
        "dpi": 600           # image resolution
    }
}

histogram_color = "#82caaf"

circuit = qiskit.QuantumCircuit(2)

circuit.h(0)
circuit.h(1)

circuit.measure_all()

savefig_dpi = 600
file_name = "work/images-to-trim/w-22-quantum-random-002.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

backend = qiskit.Aer.get_backend("aer_simulator")

job_sim = qiskit.execute(circuit, backend, shots=8000)

job_sim.result().get_counts(circuit)


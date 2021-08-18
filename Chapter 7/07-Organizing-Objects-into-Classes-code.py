def p(x):
    return x**3 - 5*x**2 + 7*x + 1

[p(x) for x in range(-2, 4)]

import inspect

class UniPoly:
    # UniPoly creates univariate polynomials with integer coefficients
    # Version 1

    def __init__(self, coefficient, indeterminate, exponent):
        # Create a UniPoly monomial.

        # Validate that the coefficient is an int.
        if not isinstance(coefficient, int):
            raise ValueError(
                "The coefficient for a UniPoly must "
                "be an int.")

        # Validate that the exponent is a non-negative int.
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError(
                "The exponent for a UniPoly must "
                "be a non-negative int.")

        # Validate that the indeterminate is an alphabetic
        # string of length 1.
        if (not isinstance(indeterminate, str) or
                len(indeterminate) != 1 or
                not indeterminate[0].isalpha()):
            raise ValueError(
                "The indeterminate for a UniPoly must "
                "be an alphabetic str of length 1.")

        self.coefficient = coefficient
        self.indeterminate = indeterminate
        self.exponent = exponent

    def __repr__(self):
        # create the object representation of the polynomial
        return f"UniPoly({self.coefficient}, " + \
               f"{repr(self.indeterminate)}, {self.exponent})"

    def __str__(self):
        # create the displayable string form of the polynomial
        return f"{self.coefficient}*" + \
               f"{self.indeterminate}**{self.exponent}"

x = UniPoly(1, 'x', 1)
x

isinstance(x, UniPoly)

str(x)

print(x)

[[1, 2], [7, 1], [1, 0]]

[[4, 3], [-7, 2], [1, 1], [-9, 0]]

[[3, 6], [-5, 4], [1, 1]]

unsorted_terms = [[-5, 4], [1, 1], [3, 6]]
unsorted_terms

sorted(unsorted_terms, key=(lambda term: term[1]), reverse=True)

class UniPoly:
    # UniPoly creates univariate polynomials with integer coefficients
    # Version 2

    def __init__(self, coefficient, indeterminate, exponent):
        # Create a UniPoly monomial.

        # Validate that the coefficient is an int.
        if not isinstance(coefficient, int):
            raise ValueError(
                "The coefficient for a UniPoly must "
                "be an int.")

        # Validate that the exponent is a non-negative int.
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError(
                "The exponent for a UniPoly must "
                "be a non-negative int.")

        # Validate that the indeterminate is an alphabetic
        # string of length 1.
        if (not isinstance(indeterminate, str) or
                len(indeterminate) != 1 or
                not indeterminate[0].isalpha()):
            raise ValueError(
                "The indeterminate for a UniPoly must "
                "be an alphabetic str of length 1.")

        # The 'variable' for the polynomial.
        self.indeterminate = indeterminate

        # The terms in the polynomial. Each key is an int
        # exponent and each value is the int coefficient.

        if coefficient != 0:
            self.terms = {exponent: coefficient}
        else:
            self.terms = dict()


print(inspect.getsource(UniPoly.__init__))

class UniPoly:
    # UniPoly creates univariate polynomials with integer coefficients
    # Version 3

    def __init__(self,
                 coefficient=1,
                 indeterminate='x',
                 exponent=0):

        # Create a UniPoly object from an integer coefficient,
        # string indeterminate, and non-negative integer
        # exponent

        if not isinstance(coefficient, int):
            raise ValueError(
                "The coefficient for a UniPoly must "
                "be an int.")

        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError(
                "The exponent for a UniPoly must "
                "be a non-negative int.")

        if (not isinstance(indeterminate, str) or
            len(indeterminate) != 1 or
                not indeterminate[0].isalpha()):
            raise ValueError(
                "The indeterminate for a UniPoly must "
                "be an alphabetic str of length 1.")

        # The 'variable' for the polynomial
        self.indeterminate = indeterminate

        # The terms in the polynomial. Each key is an int
        # exponent and each value is the int coefficient.

        if coefficient != 0:
            self.terms = {exponent: coefficient}
        else:
            self.terms = dict()

    def __neg__(self):
        # Negate the polynomial term-wise unless it is already 0.
        if not self.terms:
            return self

        new_poly = UniPoly(0, self.indeterminate)
        for exponent in self.terms:
            new_poly.terms[exponent] = -self.terms[exponent]

        return new_poly

    def __repr__(self):
        return str(self)

    def __str__(self):
        # Do a very rough and incomplete conversion to str.

        if not self.terms:
            return '0'

        print_terms = [
            f"{self.terms[exponent]}*{self.indeterminate}**{exponent}"
            for exponent in sorted(self.terms, reverse=True)
        ]

        return " + ".join(print_terms)


p = UniPoly(2, 'z', 5)

p, -p

UniPoly(0), -UniPoly(0)

UniPoly(1, 'a', 1)

-UniPoly(1, 'a', 1)

# same as unipoly03.py but with __bool__ and __eq__ added
class UniPoly:
    # UniPoly creates univariate polynomials with integer coefficients
    # Version 4

    def __init__(self,
                 coefficient=1,
                 indeterminate='x',
                 exponent=0):

        # Create a UniPoly object from an integer coefficient,
        # string indeterminate, and non-negative integer
        # exponent

        if not isinstance(coefficient, int):
            raise ValueError(
                "The coefficient for a UniPoly must "
                "be an int.")

        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError(
                "The exponent for a UniPoly must "
                "be a non-negative int.")

        if (not isinstance(indeterminate, str) or
            len(indeterminate) != 1 or
                not indeterminate[0].isalpha()):
            raise ValueError(
                "The indeterminate for a UniPoly must "
                "be an alphabetic str of length 1.")

        # The 'variable' for the polynomial.
        self.indeterminate = indeterminate

        # The terms in the polynomial. Each key is an int
        # exponent and each value is the int coefficient.

        if coefficient != 0:
            self.terms = {exponent: coefficient}
        else:
            self.terms = dict()

    def __bool__(self):
        # Returns "True" if self is nonzero.

        return bool(self.terms)

    def __eq__(self, other):
        # Tests for equality between a polynomial and an int
        # or between two polynomials.

        if isinstance(other, int):
            # If we have a constant polynomial and the
            # coefficient is the int, return True.

            if not self.terms:
                # self is the zero polynomial.
                return other == 0
            if other == 0:
                # self is not 0 but other is 0.
                return False
            if len(self.terms) > 1:
                return False
            if 0 not in self.terms:
                return False
            # self is a constant polynomial.
            if self.terms[0] == other:
                return True
            return False

        if isinstance(other, UniPoly):
            # Both are polynomials.

            if self.indeterminate != other.indeterminate:
                # The indeterminates are different.
                return False
            if len(self.terms) != len(other.terms):
                # They have different numbers of terms.
                return False

            for exponent in self.terms:
                if exponent not in other.terms:
                    # An exponent in self is missing from other.
                    return False
                if self.terms[exponent] != other.terms[exponent]:
                    # The coefficients of terms of equal exponent
                    # are different.
                    return False

            return True

        return NotImplemented

    def __neg__(self):
        # Negate the polynomial term-wise unless it is already 0.
        if not self.terms:
            return self

        new_poly = UniPoly(0, self.indeterminate)
        for exponent in self.terms:
            new_poly.terms[exponent] = -self.terms[exponent]

        return new_poly

    def __repr__(self):
        return str(self)

    def __str__(self):
        if not self.terms:
            return '0'

        def format_term(coefficient, exponent):
            coefficient = abs(coefficient)

            if exponent == 0:
                return str(coefficient)

            if exponent == 1:
                if coefficient == 1:
                    return self.indeterminate
                return f"{coefficient}*{self.indeterminate}"

            if coefficient == 1:
                return f"{self.indeterminate}**{exponent}"

            return f"{coefficient}*{self.indeterminate}**{exponent}"

        result = ""

        for exponent in sorted(self.terms, reverse=True):
            coefficient = self.terms[exponent]
            term = format_term(coefficient, exponent)

            if result:
                result += f" - {term}" if coefficient < 0 else f" + {term}"
            else:
                result = f"-{term}" if coefficient < 0 else term

        return result


print(inspect.getsource(UniPoly.__bool__))

def __bool__(self):
    # Returns "True" if self is nonzero.
    return True if self.terms else False

def poly_is_zero(p):
    print("not zero" if p else "zero")

poly_is_zero(UniPoly(0, 'x', 1))

poly_is_zero(UniPoly(1, 'x', 1))

print(inspect.getsource(UniPoly.__eq__))

UniPoly(0) == 0, UniPoly(3, 'w', 0) == 3

p = UniPoly(3, 'w', 1)
p

p == 3

UniPoly(3, 'x', 7) == UniPoly(3, 'y', 7)

q = UniPoly(3, 'x', 7)
q == q

q != q

UniPoly(3, 'x', 7) != UniPoly(3, 'y', 7)

-5 == UniPoly(-5, 'w', 0)

p = UniPoly(-3, 'z', 10)

q = p

r = UniPoly(-3, 'z', 10)

p, q, r

p == q, p == r, q == r

p is q, p is r, q is r

p

p.indeterminate = 'M'

p, q, r

"indeterminate" in dir(p)

"terms" in dir(p)

"__init__" in dir(p)

# same as unipoly03.py but with __ before instance variables
class UniPoly:
    # UniPoly creates univariate polynomials with integer coefficients
    # Version 5

    def __init__(self,
                 coefficient=1,
                 indeterminate='x',
                 exponent=0):

        # Create a UniPoly object from an integer coefficient,
        # string indeterminate, and non-negative integer
        # exponent

        if not isinstance(coefficient, int):
            raise ValueError(
                "The coefficient for a UniPoly must "
                "be an int.")

        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError(
                "The exponent for a UniPoly must "
                "be a non-negative int.")

        if (not isinstance(indeterminate, str) or
                len(indeterminate) != 1 or
                not indeterminate[0].isalpha()):
            raise ValueError(
                "The indeterminate for a UniPoly must "
                "be an alphabetic str of length 1.")

        # The 'variable' for the polynomial.
        self.__indeterminate = indeterminate

        # The terms in the polynomial. Each key is an int
        # exponent and each value is the int coefficient.

        if coefficient != 0:
            self.__terms = {exponent: coefficient}
        else:
            self.__terms = dict()

    def __bool__(self):
        # Returns "True" if self is nonzero.

        return bool(self.__terms)

    def __eq__(self, other):
        # Tests for equality between a polynomial and an int
        # or between two polynomials.

        if isinstance(other, int):
            # If we have a constant polynomial and the
            # coefficient is the int, return True.

            if not self.__terms:
                # self is the zero polynomial.
                return other == 0
            if other == 0:
                # self is not 0 but other is 0.
                return False
            if len(self.__terms) > 1:
                return False
            if 0 not in self.__terms:
                return False
            # self is a constant polynomial.
            if self.__terms[0] == other:
                return True
            return False

        if isinstance(other, UniPoly):
            # Both are polynomials.

            if self.__indeterminate != other.__indeterminate:
                # The indeterminates are different.
                return False
            if len(self.__terms) != len(other.__terms):
                # They have different numbers of terms.
                return False

            for exponent in self.__terms:
                if exponent not in other.__terms:
                    # An exponent in self is missing from other.
                    return False
                if self.__terms[exponent] != other.__terms[exponent]:
                    # The coefficients of terms of equal exponent
                    # are different.
                    return False

            return True

        return NotImplemented

    def __neg__(self):
        # Negate the polynomial term-wise unless it is already 0.
        if self:
            return self

        new_poly = UniPoly(0, self.__indeterminate)
        for exponent in self.__terms:
            new_poly.__terms[exponent] = -self.__terms[exponent]

        return new_poly

    def __repr__(self):
        return str(self)

    def __str__(self):
        if not self:
            return '0'

        def format_term(coefficient, exponent):
            coefficient = abs(coefficient)

            if exponent == 0:
                return str(coefficient)

            if exponent == 1:
                if coefficient == 1:
                    return self.__indeterminate
                return f"{coefficient}*{self.__indeterminate}"

            if coefficient == 1:
                return f"{self.__indeterminate}**{exponent}"

            return f"{coefficient}*{self.__indeterminate}**{exponent}"

        result = ""

        for exponent in sorted(self.__terms, reverse=True):
            coefficient = self.__terms[exponent]
            term = format_term(coefficient, exponent)

            if result:
                result += f" - {term}" if coefficient < 0 else f" + {term}"
            else:
                result = f"-{term}" if coefficient < 0 else term

        return result


print(inspect.getsource(UniPoly.__init__))

p = UniPoly(2, 'w', 5)
p

# same as unipoly03.py but with __ before instance variables
class UniPoly:
    # UniPoly creates univariate polynomials with integer coefficients
    # Version 5

    def __init__(self,
                 coefficient=1,
                 indeterminate='x',
                 exponent=0):

        # Create a UniPoly object from an integer coefficient,
        # string indeterminate, and non-negative integer
        # exponent

        if not isinstance(coefficient, int):
            raise ValueError(
                "The coefficient for a UniPoly must "
                "be an int.")

        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError(
                "The exponent for a UniPoly must "
                "be a non-negative int.")

        if (not isinstance(indeterminate, str) or
                len(indeterminate) != 1 or
                not indeterminate[0].isalpha()):
            raise ValueError(
                "The indeterminate for a UniPoly must "
                "be an alphabetic str of length 1.")

        # The 'variable' for the polynomial.
        self.__indeterminate = indeterminate

        # The terms in the polynomial. Each key is an int
        # exponent and each value is the int coefficient.

        if coefficient != 0:
            self.__terms = {exponent: coefficient}
        else:
            self.__terms = dict()

    def __bool__(self):
        # Returns "True" if self is nonzero.

        return bool(self.__terms)

    def __eq__(self, other):
        # Tests for equality between a polynomial and an int
        # or between two polynomials.

        if isinstance(other, int):
            # If we have a constant polynomial and the
            # coefficient is an int, return True.

            if not self.__terms:
                # self is the zero polynomial.
                return other == 0
            if other == 0:
                # self is not 0 but other is 0.
                return False
            if len(self.__terms) > 1:
                return False
            if 0 not in self.__terms:
                return False
            # self is a constant polynomial.
            if self.__terms[0] == other:
                return True
            return False

        if isinstance(other, UniPoly):
            # Both are polynomials.

            if self.__indeterminate != other.__indeterminate:
                # The indeterminates are different.
                return False
            if len(self.__terms) != len(other.__terms):
                # They have different numbers of terms.
                return False

            for exponent in self.__terms:
                if exponent not in other.__terms:
                    # An exponent in self is missing from other.
                    return False
                if self.__terms[exponent] != other.__terms[exponent]:
                    # The coefficients of terms of equal exponent
                    # are different.
                    return False

            return True

        return NotImplemented

    def __neg__(self):
        # Negate the polynomial term-wise unless it is already 0.
        if self:
            return self

        new_poly = UniPoly(0, self.__indeterminate)
        for exponent in self.__terms:
            new_poly.__terms[exponent] = -self.__terms[exponent]

        return new_poly

    def __repr__(self):
        return str(self)

    def __str__(self):
        if not self.__terms:
            return '0'

        def format_term(coefficient, exponent):
            coefficient = abs(coefficient)

            if exponent == 0:
                return str(coefficient)

            if exponent == 1:
                if coefficient == 1:
                    return self.__indeterminate
                return f"{coefficient}*{self.__indeterminate}"

            if coefficient == 1:
                return f"{self.__indeterminate}**{exponent}"

            return f"{coefficient}*{self.__indeterminate}**{exponent}"

        result = ""

        for exponent in sorted(self.__terms, reverse=True):
            coefficient = self.__terms[exponent]
            term = format_term(coefficient, exponent)

            if result:
                result += f" - {term}" if coefficient < 0 else f" + {term}"
            else:
                result = f"-{term}" if coefficient < 0 else term

        return result

    @property
    def indeterminate(self):
        return self.__indeterminate

    @indeterminate.setter
    def indeterminate(self, value):
        if (not isinstance(value, str) or
                len(value) != 1 or
                not value[0].isalpha()):
            raise ValueError(
                "The indeterminate for a UniPoly must "
                "be an alphabetic str of length 1.")
        self.__indeterminate = value


print(inspect.getsource(UniPoly.indeterminate.fget))

p = UniPoly(2, 'w', 5)

p.indeterminate

p.indeterminate = 'y'

print(inspect.getsource(UniPoly.indeterminate.fset))

p.indeterminate = 'y'
p

class_ = "Quantum Computing 101"
class_

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

"""The unipoly module contains the UniPoly class for polynomials.
"""

# The next line is for the spell-checker in Visual Studio Code
# cspell:ignore radd rsub rmul


class UniPoly:
    """Polynomial with one variable and integer coefficients.

    UniPoly creates a univariate polynomial with a single term
    and an integer coefficient. Polynomials may use different
    variables, here called 'indeterminates', but their names
    must each be a single alphabetic character. These polynomials
    are immutable.

    Parameters
    ----------
    coefficient : int, optional
        The coefficient of the term. Default value is 1.
    indeterminate : str, optional
        The "variable." Must be a single alphabetic character.
        Default value is 'x'.
    exponent : int, optional
        The exponent of the term. Default value is 1.

    Raises
    ------
    ValueError
        If the coefficient is not an int.
    ValueError
        If the exponent is not a non-negative int.
    ValueError
        If the indeterminate is not a single
        alphabetic character.
    """

    # -----------------------------------------------------------------
    # Initialization
    # -----------------------------------------------------------------

    def __init__(self,
                 coefficient=1,
                 indeterminate='x',
                 exponent=0):

        # Instance variables
        # ------------------
        # __indeterminate : str
        #     The "variable" of the polynomial.
        # __terms : dict
        #     The terms of the polynomials with the exponents
        #     as keys and values being coefficients.

        if not isinstance(coefficient, int):
            raise ValueError(
                "The coefficient for a UniPoly must "
                "be an int.")

        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError(
                "The exponent for a UniPoly must "
                "be a non-negative int.")

        if (not isinstance(indeterminate, str) or
                len(indeterminate) != 1 or
                not indeterminate[0].isalpha()):
            raise ValueError(
                "The indeterminate for a UniPoly must "
                "be an alphabetic str of length 1.")

        self.__indeterminate = indeterminate

        if coefficient != 0:
            self.__terms = {exponent: coefficient}
        else:
            self.__terms = dict()

    # -----------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------

    def __add__(self, other):
        """Adds a polynomial to a polynomial or an integer.

        Parameters
        ----------
        other : :class:`UniPoly` or int
            A polynomial or integer.

        Notes
        ------
        If the second argument is not a polynomial or integer,
        or if the indeterminates in non-constant polynomials
        are different, returns NotImplemented.

        Returns
        -------
        :class:`UniPoly` or NotImplemented
            The sum of self and other, or NotImplemented.
        """

        if not self.__terms:
            return other

        # if other is an integer, create a constant polynomial
        if isinstance(other, int):
            other = UniPoly(other, self.__indeterminate, 0)

        # both objects are polynomials

        if isinstance(other, UniPoly):
            # if other == 0, return self
            if not other.__terms:
                return self

            if self.__indeterminate != other.__indeterminate:
                if self.is_constant and other.is_constant:
                    return UniPoly(self.constant_coefficient +
                                   other.constant_coefficient,
                                   self.__indeterminate,
                                   0)
                return NotImplemented

            new_poly = UniPoly(0, self.__indeterminate, 0)

            for exponent, coefficient in self.__terms.items():
                if exponent not in other.__terms:
                    new_poly.__terms[exponent] = coefficient
                else:
                    sum = self.__terms[exponent] \
                        + other.__terms[exponent]
                    if sum:
                        new_poly.__terms[exponent] = sum

            for exponent, coefficient in other.__terms.items():
                if exponent not in self.__terms:
                    new_poly.__terms[exponent] = coefficient

            return new_poly

        return NotImplemented

    def __radd__(self, other):
        """Compute other + self.

        Returns
        -------
        :class:`UniPoly`
            The sum of other and self.
        """

        # Addition is commutative, so we call __add__.

        return self.__add__(other)

    def __bool__(self):
        """Returns True if the polynomial is non-zero, False otherwise.

        Returns
        -------
        bool
        """

        return bool(self.__terms)

    def __call__(self, x):
        """Evaluates a polynomial by substituting `x` for the indeterminate.

        Python calls this when it sees a polynomial being used
        in function application. If `p` is a polynomial, then
        `p(3.4)` substitutes 3.4 for the indeterminate and
        does the math as expressed by the polynomial.

        Parameters
        ----------
        x : any object that supports -, +, *, **
            The value to be substituted for the indeterminate.

        Returns
        -------
        Probably `type(x)`
        """
        result = 0

        for exponent, coefficient in self.__terms.items():
            result += coefficient * x**exponent

        return result

    def __copy__(self):
        """Copies a polynomial, returning a new polynomial.

        This creates a deep copy of a polynomial, even if the
        original was zero.

        See Also
        --------
        `deepcopy`

        Returns
        -------
        :class:`UniPoly`
            A complete copy of the polynomial.
        """
        new_poly = UniPoly(0, self.__indeterminate)
        for exponent in self.__terms:
            new_poly.__terms[exponent] = self.__terms[exponent]

        return new_poly

    def __deepcopy__(self, memo):
        """Copies a polynomial, returning a new polynomial.

        This creates a deep copy of a polynomial, even if the
        original was zero.

        See Also
        --------
        `copy`

        Returns
        -------
        :class:`UniPoly`
            A complete copy of the polynomial.
        """
        return self.__copy__()

    def __eq__(self, other):
        """Tests for equality between a polynomial and polynomial or `int`.

        Parameters
        ----------
        other : :class:`UniPoly` or `int`
            The object to be be tested for equality

        Returns
        -------
        bool
            True if the objects are mathematically equal.
        """

        # If other is an `int`, turn it into an polynomial.
        if isinstance(other, int):
            other = UniPoly(other, self.__indeterminate, 0)

        if isinstance(other, UniPoly):
            # Look for a reason why they are not equal.

            # Do they have different indeterminates?
            if self.__indeterminate != other.__indeterminate:
                return False

            # Do they have different numbers of terms?
            if len(self.__terms) != len(other.__terms):
                return False

            # Are there terms of equal exponent and coefficient?
            for exponent in self.__terms:
                if exponent not in other.__terms:
                    # an exponent in self is missing from other
                    return False
                if self.__terms[exponent] != other.__terms[exponent]:
                    # the coefficients of terms of equal exponent
                    # are different
                    return False

            # They must be equal.
            return True

        return NotImplemented

    def __getitem__(self, exponent):
        """Retrieves the coefficient of the term with the exponent.

        Supports square bracket access to coefficients of terms in
        the polynomial. If there is no term with the given exponent,
        returns 0.

        Parameters
        ----------
        exponent : int
            A non-negative integer representing an exponent
            in a polynomial term.

        Returns
        -------
        int or NotImplemented
            The coefficient of the term with the given exponent.

        Raises
        ------
        ValueError
            Raised if the exponent is an integer but less than zero.
        """
        if not isinstance(exponent, int):
            return NotImplemented
        if exponent < 0:
            raise ValueError("polynomial exponents are integers >= 0")

        if not self.__terms:
            return 0
        return self.__terms.get(exponent, 0)

    def __hash__(self):
        """Computes a hash code for a polynomial.

        If p and q are equal polynomials, then their hash codes
        are equal.

        Returns
        -------
        int
            An integer hash code.
        """
        h = hash(self.__indeterminate)
        for exponent_coefficient in self.__terms:
            h += hash(exponent_coefficient)
        return h

    def __int__(self):
        """Returns an `int` if the polynomial is constant.

        Returns
        -------
        int
            The constant term of the constant polynomial.

        Raises
        ------
        ValueError
            Raised if self is not constant.
        """
        if not self.__terms:
            return 0
        if len(self.__terms) == 1 and 0 in self.__terms:
            return self.__terms[0]
        raise ValueError("non-constant polynomial for int()")

    def __iter__(self):
        """Iterator returning exponent-coefficient tuple pairs.

        Notes
        -----
        The order of the pairs is not guaranteed to be sorted.

        Returns
        -------
        tuple:
            (exponent, coefficient) in polynomial.
        """

        return iter(self.__terms.items())

    def __mul__(self, other):
        """Multiplies a polynomial to a polynomial or an integer.

        Parameters
        ----------
        other : :class:`UniPoly` or int
            A polynomial or integer.

        Notes
        ------
        If the second argument is not a polynomial or integer,
        or if the indeterminates in non-constant polynomials
        are different, returns NotImplemented.

        Returns
        -------
        :class:`UniPoly` or NotImplemented
            The product of self and other, or NotImplemented.
        """

        # if self == 0, return it
        if not self.__terms:
            return self

        # if other is an integer, create a constant polynomial
        if isinstance(other, int):
            other = UniPoly(other, self.__indeterminate, 0)

        # both objects are polynomials

        if isinstance(other, UniPoly):
            # if other == 0, return other
            if not other.__terms:
                return other

            # We now have two non-zero polynomials.

            if self.__indeterminate != other.__indeterminate:
                if self.is_constant and other.is_constant:
                    return UniPoly(self.constant_coefficient *
                                   other.constant_coefficient,
                                   self.__indeterminate,
                                   0)
                return NotImplemented

            new_poly = UniPoly(0, self.__indeterminate, 0)

            for exponent_1, coefficient_1 in self.__terms.items():
                for exponent_2, coefficient_2 in other.__terms.items():
                    new_poly += UniPoly(coefficient_1 * coefficient_2,
                                        self.__indeterminate,
                                        exponent_1 + exponent_2)
            return new_poly

        return NotImplemented

    def __rmul__(self, other):
        """Computes other * self.

        Returns
        -------
        :class:`UniPoly`
            The product of other and self.
        """

        # Multiplication is commutative, so we call __mul__.

        return self.__mul__(other)

    def __neg__(self):
        """Negates a polynomial, returning a new polynomial.

        Returns
        -------
        :class:`UniPoly`
            A new polynomial.
        """
        # negate the polynomial term-wise unless it is already 0
        if not self.__terms:
            return self

        new_poly = UniPoly(0, self.__indeterminate)
        for exponent in self.__terms:
            new_poly.__terms[exponent] = -self.__terms[exponent]

        return new_poly

    def __pow__(self, exponent):
        """Raises a polynomial to a non-negative integer exponent.

        `__pow__` used by both `**` and `pow`.

        Parameters
        ----------
        exponent : int
            The non-negative exponent to which self is raised.

        Notes
        -----
        If the exponent is not a non-negative integer, this method
        returns NotImplemented. This allows another class to implement
        quotients of polynomials and expressions like `p**(-1)`.

        Returns
        -------
        :class:`UniPoly` or NotImplemented
            The polynomial `self` raised to `exponent`, or NotImplemented.
        """

        # Validate the exponent.
        if not isinstance(exponent, int) or exponent < 0:
            return NotImplemented

        # Handle the simple cases
        if exponent == 0:
            return UniPoly(1, self.__indeterminate, 0)

        if exponent == 1:
            return self

        if exponent == 2:
            return self * self

        # Compute the exponent by recursive repeated squaring.
        power = self**(exponent // 2)
        power *= power
        if exponent % 2 == 1:
            power *= self

        return power

    def __repr__(self):
        """Returns the human-readable representation of a polynomial.

        Notes
        -----
        For simplicity, we are returning the result of `__str__`. We
        should be returning something like
        UniPoly(2, 'x', 6) + UniPoly(1, 'x', 3) + UniPoly(-1, 'x', 0)

        Returns
        -------
        str
        """
        return str(self)

    def __str__(self):
        """Creates a human-readable string representation.

        This returns forms that look like 2x**6 + x**3 - 1.

        Returns
        -------
        str
            Mathematical human-readable form of the polynomial.
        """
        if not self.__terms:
            return '0'

        def format_term(coefficient, exponent):
            """Format a single term in the polynomial.

            This function formats a term and handles the special
            cases when the coefficient is +/- 1 or the exponent is
            0 or 1.

            Parameters
            ----------
            coefficient : int
                The coefficient of the term.
            exponent : int
                The exponent of the term.

            Returns
            -------
            str
                The human-readable representation of a polynomial term.
            """
            coefficient = abs(coefficient)

            if exponent == 0:
                return str(coefficient)

            if exponent == 1:
                if coefficient == 1:
                    return self.__indeterminate
                return f"{coefficient}*{self.__indeterminate}"

            if coefficient == 1:
                return f"{self.__indeterminate}**{exponent}"

            return f"{coefficient}*{self.__indeterminate}**{exponent}"

        # Collect the formatted and sorted terms in result, taking
        # case to handle leading or middle negative signs.

        result = ""

        for exponent in sorted(self.__terms, reverse=True):
            coefficient = self.__terms[exponent]
            term = format_term(coefficient, exponent)

            if result:
                result += f" - {term}" \
                    if coefficient < 0 else f" + {term}"
            else:
                result = f"-{term}" \
                    if coefficient < 0 else term

        return result

    def __sub__(self, other):
        """Subtracts a polynomial or an integer from a polynomial.

        Parameters
        ----------
        other : :class:`UniPoly` or `int`
            A polynomial or integer.

        Notes
        ------
        If the second argument is not a polynomial or integer,
        or if the indeterminates in non-constant polynomials
        are different, returns NotImplemented.

        Returns
        -------
        :class:`UniPoly` or NotImplemented
            The difference of self and other, or NotImplemented.
        """
        if not self.__terms:
            return -other

        # if other is an integer, create a constant polynomial
        if isinstance(other, int):
            other = UniPoly(other, self.__indeterminate, 0)

        # both objects are polynomials

        if isinstance(other, UniPoly):
            # if other == 0, return self
            if not other.__terms:
                return self

            if self.__indeterminate != other.__indeterminate:
                if self.is_constant and other.is_constant:
                    return UniPoly(self.constant_coefficient -
                                   other.constant_coefficient,
                                   self.__indeterminate,
                                   0)
                return NotImplemented

            new_poly = UniPoly(0, self.__indeterminate, 0)

            for exponent, coefficient in self.__terms.items():
                if exponent not in other.__terms:
                    new_poly.__terms[exponent] = coefficient
                else:
                    sum = self.__terms[exponent] \
                        - other.__terms[exponent]
                    if sum:
                        new_poly.__terms[exponent] = sum

            for exponent, coefficient in other.__terms.items():
                if exponent not in self.__terms:
                    new_poly.__terms[exponent] = -coefficient

            return new_poly

        return NotImplemented

    def __rsub__(self, other):
        """Computes other - self.

        Returns
        -------
        :class:`UniPoly`
            The difference of other and self.
        """

        # other - self == -(self - other)
        # For efficiency, this should be computed like __sub__
        # so we create fewer intermediate polynomials.

        return self.__sub__(other).__neg__()

    # -----------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------

    @property
    def constant_coefficient(self):
        """The coefficient of the term with exponent 0."""
        if self.__terms and 0 in self.__terms:
            return self.__terms[0]
        return 0

    @property
    def degree(self):
        """Returns the largest exponent in the polynomial."""
        if self.__terms:
            max_degree = None
            for exponent in self.__terms:
                if max_degree is None or exponent > max_degree:
                    max_degree = exponent
        else:
            return 0

    @property
    def indeterminate(self):
        """The indeterminate (or variable) in the polynomial."""
        return self.__indeterminate

    @property
    def is_constant(self):
        """True if the polynomial only contains a term of exponent 0."""

        if not self.__terms:
            return True
        if len(self.__terms) != 1:
            return False
        return next(iter(self.__terms)) == 0

    @property
    def minimum_degree(self):
        """The smallest exponent among the non-zero terms, or 0."""
        if self.__terms:
            min_degree = None
            for exponent in self.__terms:
                if min_degree is None or exponent < min_degree:
                    min_degree = exponent
        else:
            # Return 0 for the zero polynomial
            return 0

    # -----------------------------------------------------------------
    # Instance methods
    # -----------------------------------------------------------------

    def derivative(self):
        """Computes the derivative of a polynomial.

        Returns
        -------
        :class:`UniPoly`
            The derivative.
        """

        # Initialize the result to the zero polynomial
        # with the correct indeterminate.
        result = UniPoly(0, self.__indeterminate, 0)

        # Compute the term-by-term derivative, and sum.
        if self.__terms:
            for exponent, coefficient in self.__terms.items():
                if exponent > 0:
                    result += UniPoly(exponent * coefficient,
                                      self.__indeterminate,
                                      exponent - 1)
        return result

# Sample tests for pytest


def test_good_addition():
    """Tests that an addition is correct."""
    x = UniPoly(1, 'x', 1)
    p = x + 1
    q = x - 1
    assert p + q == 2 * x


def test_bad_multiplication():
    """Tests that a multiplication fails."""
    x = UniPoly(1, 'x', 1)
    p = x + 1
    q = x - 1
    assert p * q == x * x + 1


print(inspect.getsource(UniPoly.__bool__))

help(UniPoly.__bool__)

help(UniPoly.__add__)

print(UniPoly.__doc__)

CHOCOLATE_COOKIE = 0
SUGAR_COOKIE = 1
OATMEAL_COOKIE = 2
SHORTBREAD_COOKIE = 3

COOKIE_NAMES = [
    "chocolate",
    "sugar",
    "oatmeal",
    "shortbread"
]

COOKIE_NAMES[SUGAR_COOKIE]

from enum import Enum

class Cookie(Enum):
    CHOCOLATE = "chocolate"
    SUGAR = "sugar"
    OATMEAL = "oatmeal"
    SHORTBREAD = "shortbread"

Cookie.SHORTBREAD

Cookie.SUGAR

cookie = Cookie.OATMEAL
cookie.name

cookie.value

Cookie("sugar")

Cookie["SUGAR"]

from enum import IntEnum

class CatAge(IntEnum):
    GUS = 3
    FERDINAND = 6
    FRANZ = 6
    GEORGIA = 9

CatAge.GUS.name, CatAge.GUS.value

CatAge.FERDINAND >= CatAge.FRANZ

CatAge.GEORGIA < 10

2 * (CatAge.GUS + CatAge.GEORGIA) - 1

print(inspect.getsource(UniPoly.__str__))

UniPoly(-3), UniPoly(-1), UniPoly(0), UniPoly(1), UniPoly(3)

UniPoly(-1, 'z', 1)

UniPoly(3, 'x', 7)

print(inspect.getsource(UniPoly.constant_coefficient.fget))

UniPoly(3, 'x', 0).constant_coefficient

UniPoly(3, 'x', 7).is_constant, UniPoly(2, 'y', 0).is_constant

print(inspect.getsource(UniPoly.__add__))

w = UniPoly(1, 'w', 1)
w, w + w, w + -w

UniPoly(3, 'x', 7) + UniPoly(5, 'x', 3) + 1

UniPoly(3, 'x', 7) + UniPoly(-5, 'x', 3) + 1

UniPoly(3, 'x', 7) + 2

print(inspect.getsource(UniPoly.__radd__))

2 + UniPoly(3, 'x', 7)

w = UniPoly(1, 'w', 1)
w, w - w, w - -w

UniPoly(3, 'x', 7) - UniPoly(5, 'x', 3) + 1

UniPoly(3, 'x', 7) - UniPoly(-5, 'x', 3) + 1

UniPoly(3, 'x', 7) - 2

print(inspect.getsource(UniPoly.__rsub__))

2 - UniPoly(3, 'x', 7)

print(inspect.getsource(UniPoly.__rmul__))

print(inspect.getsource(UniPoly.__mul__))

z = UniPoly(1, 'z', 1)
(z + 1) * (z - 1)

(z + 1) * (z + 1)

(2*z + 1) * (-3*z*z*z + 4)

print(inspect.getsource(UniPoly.__pow__))

(z + 1)**0, (z + 1)**1, (z + 1)**2

(z + 1)**6

(z + 1)**25

print(inspect.getsource(UniPoly.derivative))

p = 3*z**6 - 2*z**5 + 7*z**2 + z - 12
p

p.derivative()

q_prime = UniPoly(4, 'y', 1).derivative()
print(q_prime)
print(type(q_prime))

print(inspect.getsource(UniPoly.__call__))

x = UniPoly(1, 'x', 1)
p = x**3 - 5*x**2 + 7*x + 1

[p(x) for x in range(-2, 4)]

p(2.75)      # float

p(1 + 2j)    # complex

p(x + 1)     # polynomial

small_primes = [2, 3, 5, 7, 11]
small_primes[4]

books = {"math": 4, "cooking": 7, "fishing": 2}
books["fishing"]

print(inspect.getsource(UniPoly.__getitem__))

p = (x**2 - 3)**3
p

p[0]     # the constant term

p[3]     # this exponent does not appear

p[6]     # the exponent of highest degree

print(inspect.getsource(UniPoly.__int__))

int(UniPoly(3, 'x', 0))

class Guitar:
    number_of_guitars = 0

    def __init__(self, brand):
        Guitar.number_of_guitars += 1
        plural = "s" if Guitar.number_of_guitars != 1 else ""
        print(f"We have {Guitar.number_of_guitars} guitar{plural}")
        self.brand = brand

    def __repr__(self):
        return f"Guitar({repr(self.brand)})"

    def __str__(self):
        return self.brand

Guitar("Fender")

Guitar("Taylor")

g = Guitar("Gibson")
g

Guitar.number_of_guitars

g.number_of_guitars

class Guitar:
    number_of_guitars = 0

    def __init__(self, brand):
        Guitar.number_of_guitars += 1
        plural = "s" if Guitar.number_of_guitars != 1 else ""
        print(f"We have {Guitar.number_of_guitars} guitar{plural}")
        self.brand = brand

    def __repr__(self):
        return f"Guitar({repr(self.brand)})"

    def __str__(self):
        return self.brand

    @classmethod
    def get_count_class(cls):
        return cls.number_of_guitars

    @staticmethod
    def get_count_static():
        return Guitar.number_of_guitars


Guitar("Fender")
Guitar("Taylor")
g = Guitar("Gibson")
g

print(inspect.getsource(Guitar.get_count_class))

Guitar.get_count_class(), g.get_count_class()

print(inspect.getsource(Guitar.get_count_static))

Guitar.get_count_class(), g.get_count_static()

class Guitar:
    def __init__(self, brand, model, year_built, strings=6):
        self._brand = brand
        self._model = model
        self._year_built = year_built
        self._strings = strings

    def __str__(self):
        return f"{self._strings}-string " \
            + f"{self._year_built} " \
            + f"{self._brand} {self._model}"


print(Guitar("Fender", "Stratocaster", "2012"))

from src.code.guitar_04 import *

print(inspect.getsource(MusicalInstrument))

print(inspect.getsource(Guitar))

instrument = MusicalInstrument("Gibson", "Les Paul", "1997")
print(instrument)

guitar = Guitar("Fender", "Stratocaster", "2012")
print(guitar)

isinstance(instrument, MusicalInstrument), isinstance(instrument, Guitar)

isinstance(guitar, MusicalInstrument), isinstance(guitar, Guitar)

print(inspect.getsource(Clarinet))

help(Clarinet)

clarinet = Clarinet("Yamaha", "YCL-650", "2021")
print(clarinet)

isinstance(clarinet, MusicalInstrument), isinstance(clarinet, Clarinet)

print(inspect.getsource(Pickup))

print(inspect.getsource(ElectricGuitar))

electric_guitar = ElectricGuitar("Fender", "Stratocaster", "2012")
print(electric_guitar)

electric_guitar.pickup = Pickup.SINGLECOIL
print(electric_guitar)

from abc import ABC, abstractmethod

from src.code.guitar_05 import *

print(inspect.getsource(MusicalInstrument))

print(Guitar("Fender", "Stratocaster", "2012"))

print(inspect.getsource(Wooden))

print(inspect.getsource(AcousticGuitar))

guitar = AcousticGuitar("Taylor", "AD27e", "2021", "mahogany")
print(guitar)

for i in [2, 3, 5]:
    print(i)

the_list = [2, 3, 5]
the_index = 0

while True:
    if the_index < len(the_list):
        print(the_list[the_index])
        the_index += 1
    else:
        break

the_list = [2, 3, 5]
the_index = len(the_list) - 1

while True:
    if the_index >= 0:
        print(the_list[the_index])
        the_index -= 1
    else:
        break

my_iter = iter([2, 3, 5])
print(next(my_iter))

print(next(my_iter))

print(next(my_iter))

numbers = {1: "one", 2: "two", 3: "three"}

next(iter(numbers))

next(iter(numbers.keys()))

next(iter(numbers.values()))

next(iter(numbers.items()))

print(inspect.getsource(UniPoly.__iter__))

s = UniPoly(1, 's', 1)

for exp_coef in (s - 1)**4:
    print(exp_coef)

print(inspect.getsource(UniPoly.is_constant.fget))

def create_odd_number_generator():
    n = 1
    while True:
        yield n
        n += 2

odd_number_generator = create_odd_number_generator()
odd_number_generator

next(odd_number_generator)

next(odd_number_generator)

next(odd_number_generator)

for n in odd_number_generator:
    print(f"{n} ", end="")
    if n > 20:
        break

def create_even_number_generator(maximum_n=None):
    n = 0
    while True:
        if maximum_n is not None and n > maximum_n:
            return
        yield n
        n += 2

even_number_generator = create_even_number_generator(20)
even_number_generator

for n in even_number_generator:
    print(f"{n} ", end="")

polys = [UniPoly(1, 'x', 2), UniPoly(2, 'x', 3), UniPoly(3, 'x', 4)]
polys

polys.reverse()
polys

hash(-0.8367)

hash(735678)

hash("A solitary string")

hash((4, 3, 2, 1))

print(inspect.getsource(UniPoly.__hash__))

hash(UniPoly(10, 'z', 100))

hash(UniPoly(10, 'w', 100))


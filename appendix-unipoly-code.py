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



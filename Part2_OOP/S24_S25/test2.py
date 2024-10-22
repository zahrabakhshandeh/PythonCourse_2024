class Calculator:
    """
    A simple calculator class that can perform basic operations.

    >>> calc = Calculator()
    >>> calc.add(5, 3)
    8
    >>> calc.subtract(10, 4)
    6
    >>> calc.multiply(3, 7)
    21
    >>> calc.divide(8, 2)
    4.0
    >>> calc.divide(5, 0)
    Traceback (most recent call last):
      ...
    ZeroDivisionError: Cannot divide by zero
    """

    def add(self, a: int, b: int) -> int:
        """
        Returns the sum of two numbers.

        :param a: First number to add (integer).
        :param b: Second number to add (integer).
        :return: Sum of a and b (integer).

        >>> Calculator().add(2, 3)
        5
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        Returns the difference between two numbers.

        :param a: First number (integer).
        :param b: Second number to subtract from a (integer).
        :return: Difference between a and b (integer).

        >>> Calculator().subtract(10, 3)
        7
        """
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """
        Returns the product of two numbers.

        :param a: First number to multiply (integer).
        :param b: Second number to multiply (integer).
        :return: Product of a and b (integer).

        >>> Calculator().multiply(4, 5)
        20
        """
        return a * b

    def divide(self, a: int, b: int) -> float:
        """
        Returns the quotient of two numbers.

        :param a: Numerator (integer).
        :param b: Denominator (integer).
        :return: Quotient of a divided by b (float).
        :raises ZeroDivisionError: If b is 0.

        >>> Calculator().divide(8, 2)
        4.0
        >>> Calculator().divide(5, 0)
        Traceback (most recent call last):
          ...
        ZeroDivisionError: Cannot divide by zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    import doctest
    doctest.testmod()

import doctest

class Calculator:
    """
    A simple calcualator
    """
    def add(self, a: int, b: int) -> int:
        """
        Adds two numbers 

        Args:
            a(int): First Number 
            b(int): Second Number 

        Returns:
            int: Sum of a and b 

        Example:
            >>> Calculator().add(2, 3)
            6
        """
        return a + b 
    
    def subtract(self, a: int, b:int) -> int: 
        """
        Subtracts two numbers 

        Args:
            a(int): First Number 
            b(int): Second Number 

        Returns:
            int: Subtracts of a and b 

        Example:
            >>> Calculator().subtract(2, 3)
            -1
        """
        return a - b 
    
    def divide(self, a: int, b: int) -> float:
        """
        Divides two numbers 

        Args:
            a(int): First Number 
            b(int): Second Number 

        Returns:
            float: Subtracts of a and b 
        
        Raises:
            ZeroDivisionError: if b is 0

        Example:
            >>> Calculator().divide(8, 2)
            4.0
            >>> Calculator().divide(2, 0)
            Traceback (most recent call last):
            ... 
            ZeroDivisionError: Cannot divide by zero!
        """
        
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b
    
if __name__ == "__main__":
    doctest.testmod()
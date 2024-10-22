from typing import Iterable, SupportsIndex

class MyList(list):
    """
    A custom list class that only accepts strings and provides additional methods for filtering, joining, and counting.
    """

    def __init__(self, data=[]):
        """
        Initializes a MyList instance with string elements.

        Args:
            data (list): A list of strings.

        Raises:
            ValueError: If any element in data is not a string.

        Example:
            >>> my_list = MyList(["apple", "banana"])
            >>> print(my_list)
            ['apple', 'banana']
            >>> MyList([1, "banana"])
            Traceback (most recent call last):
              ...
            ValueError: Only String!
        """
        if self.all_str(data):
            super().__init__(data)
        else:
            raise ValueError("Only String!")

    @staticmethod
    def all_str(data) -> bool:
        """
        Checks if all elements in the list are strings.

        Args:
            data (list): A list to check.

        Returns:
            bool: True if all elements are strings, False otherwise.

        Example:
            >>> MyList.all_str(["apple", "banana"])
            True
            >>> MyList.all_str(["apple", 2])
            False
        """
        return all(isinstance(item, str) for item in data)

    def append(self, value: str):
        """
        Appends a string to the list.

        Args:
            value (str): The string to append.

        Raises:
            ValueError: If the value is not a string.

        Example:
            >>> my_list = MyList(["apple"])
            >>> my_list.append("banana")
            >>> print(my_list)
            ['apple', 'banana']
            >>> my_list.append(3)
            Traceback (most recent call last):
              ...
            ValueError: Only String!
        """
        if isinstance(value, str):
            super().append(value)
        else:
            raise ValueError("Only String!")

    def insert(self, index: SupportsIndex, value: str):
        """
        Inserts a string at a specified index in the list.

        Args:
            index (SupportsIndex): The index at which to insert the value.
            value (str): The string to insert.

        Raises:
            ValueError: If the value is not a string.

        Example:
            >>> my_list = MyList(["apple", "banana"])
            >>> my_list.insert(1, "orange")
            >>> print(my_list)
            ['apple', 'orange', 'banana']
        """
        if isinstance(value, str):
            super().insert(index, value)
        else:
            raise ValueError("Only String!")

    def extend(self, list_data: Iterable[str]):
        """
        Extends the list with another iterable of strings.

        Args:
            list_data (Iterable[str]): An iterable containing strings to extend the list with.

        Raises:
            ValueError: If any element in list_data is not a string.

        Example:
            >>> my_list = MyList(["apple"])
            >>> my_list.extend(["banana", "orange"])
            >>> print(my_list)
            ['apple', 'banana', 'orange']
            >>> my_list.extend(["kiwi", 3])
            Traceback (most recent call last):
              ...
            ValueError: Only String!
        """
        if self.all_str(list_data):
            super().extend(list_data)
        else:
            raise ValueError("Only String!")

    def __setitem__(self, index: SupportsIndex, value: str):
        """
        Sets the value at a specific index to a string.

        Args:
            index (SupportsIndex): The index to set the value.
            value (str): The new value to set.

        Raises:
            ValueError: If the value is not a string.

        Example:
            >>> my_list = MyList(["apple", "banana"])
            >>> my_list[1] = "orange"
            >>> print(my_list)
            ['apple', 'orange']
            >>> my_list[1] = 5
            Traceback (most recent call last):
              ...
            ValueError: Only String!
        """
        if isinstance(value, str):
            super().__setitem__(index, value)
        else:
            raise ValueError("Only String!")

    def filter_data(self, value: str) -> list:
        """
        Filters the list, returning elements that contain the given substring.

        Args:
            value (str): The substring to filter by.

        Returns:
            list: A list of elements containing the substring.

        Raises:
            ValueError: If the value is not a string.

        Example:
            >>> my_list = MyList(["python", "java", "python3"])
            >>> my_list.filter_data("python")
            ['python', 'python3']
        """
        if not isinstance(value, str):
            raise ValueError("Only String!")
        return [item for item in self if value in item]

    def join_data(self, separator: str = "") -> str:
        """
        Joins the elements of the list into a single string with a specified separator.

        Args:
            separator (str): The string used to separate the elements. Defaults to an empty string.

        Returns:
            str: The joined string.

        Example:
            >>> my_list = MyList(["python", "is", "fun"])
            >>> my_list.join_data(" ")
            'python is fun'
        """
        return separator.join(self)

    def unique(self) -> list:
        """
        Returns a list of unique elements from the original list.

        Returns:
            list: A list of unique elements.

        Example:
            >>> my_list = MyList(["apple", "apple", "banana"])
            >>> my_list.unique()
            ['apple', 'banana']
        """
        return list(set(self))

    def nuique(self) -> int:
        """
        Returns the number of unique elements in the list.

        Returns:
            int: The number of unique elements.

        Example:
            >>> my_list = MyList(["apple", "banana", "apple"])
            >>> my_list.nuique()
            2
        """
        return len(self.unique())

    def count_value(self) -> dict:
        """
        Counts the occurrences of each element in the list.

        Returns:
            dict: A dictionary with elements as keys and their counts as values.

        Example:
            >>> my_list = MyList(["apple", "banana", "apple"])
            >>> my_list.count_value()
            {'apple': 2, 'banana': 1}
        """
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts

from typing import Iterable, SupportsIndex


class MyList(list):
    def __init__(self, data=[]):
        if self.all_str(data):
            super().__init__(data)
        else:
            raise ValueError("Only String!")
    
    @staticmethod
    def all_str(data):
        for item in data:
            if not isinstance(item, str):
                return False 
        return True
    
    def append(self, value):
        if isinstance(value, str):
            super().append(value)
        else:
            raise ValueError("Only String!")
        
    def insert(self, index, value):
        if isinstance(value, str):
            super().insert(index, value)
        else:
            raise ValueError("Only String!")
        
    def extend(self, list_data):
        if self.all_str(list_data):
            super().extend(list_data)
        else:
            raise ValueError("Only String!")
        
    def __setitem__(self, index, value):
        if isinstance(value, str):
            super().__setitem__(index, value)
        else:
            raise ValueError("Only String!")

    def filter_data(self, value): # python 
        # ["python", "python3", "java"] ======> ["python", "python3"]
        if not isinstance(value, str):
            raise ValueError("Only String!")
        filtered_data = []
        for item in self: # python, python3, java
            if value in item: # python in python
                filtered_data.append(item)
        return filtered_data

    def join_data(self, seprator=""):
        result = seprator.join(self)
        return result
    
    def unique(self):
        return list(set(self))
        
    def nuique(self):
        n_unique = len(self.unique())
        return n_unique
    
    def count_value(self):
        counts = {}
        for item in self:
            count_item = counts.get(item, 0) + 1 
            counts[item] = count_item 
        return counts
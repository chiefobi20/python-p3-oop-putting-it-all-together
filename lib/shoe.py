#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand: str, size: int):
        if not isinstance(brand, str):
            raise TypeError("Brand must be a string.")
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be an integer.")

        self.brand = brand
        self.size = size
        self.condition = "New"
        self.is_cobbled = False
    def get_size(self):
        return self.size

    def cobble(self):

        self.is_cobbled = True
        self.condition = "New"
        print("The shoe has been repaired.")

    def is_cobbled_status(self):
        return self.is_cobbled

    def cobble_makes_new(self):
        if self.is_cobbled:
            new_shoe = Shoe(self.brand, self.size)
            new_shoe.condition = "New"
            print(f"A new cobbled version of the {self.brand} shoe (size {self.size}) has been created with condition {new_shoe.condition}.")
            return new_shoe
        else:
            print(f"The {self.brand} shoe (size {self.size}) needs to be cobbled first.")
            return None

    def get_condition(self):
        return self.condition












    # def __init__(self, brand, size):
    #     self.brand = brand
    #     self._size = size

    # def get_size(self):
    #     return self._size

    # def set_size(self, size):
    #      if isinstance(size, int):
    #         self._size = size
    #      else:
    #         raise ValueError("Size must be an integer.")

    # def can_cobble(self):
    #     print("The shoe has been repaired.")
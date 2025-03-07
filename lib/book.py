#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 1

    def get_title(self):
        return self.title

    def get_page_count(self):
        return self.page_count

    def turn_page(self, direction="forward"):
        if direction == "forward":
            self.current_page += 1
            if self.current_page > self.page_count:
                self.current_page = self.page_count
                print("Flipping the page...wow, you read fast!")
        elif direction == "backward":
            self.current_page -= 1
            if self.current_page < 1:
                self.current_page = 1
        else:
            print("Invalid direction. Please use 'forward' or 'backward'.")

    def current_page_number(self):
        return self.current_page




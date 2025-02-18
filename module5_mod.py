#!/usr/bin/python3

class NumberProcessor:
    def __init__(self):
        self.numbers = []
        self.N = 0

    def read_N(self):
        while True:
            self.N = int(input('Enter a positive integer: '))
            if self.N > 0:
                break
            else:
                print("Must use a positive integer. Try again!")

    def read_numbers(self):
        """ Reads N numbers from the user. """
        print(f"Enter {self.N} numbers:")
        for i in range(self.N):
            while True:
                num = int(input(f"Number {i+1}: "))
                self.numbers.append(num)
                break

    def search_number(self, X):
        return self.numbers.index(X) + 1 if X in self.numbers else -1

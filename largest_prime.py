# -*- coding: utf-8 -*-
"""
Get the maximum largest prime of entered number.
"""

class Largest_Prime:
    
    def __init__(self, number):
        self.number = number
    
    def print_largest_prime(self, number):
        if number < 2:
            return -1
        prime = 2
        for i in range(2, number + 1):
            if number % i == 0:
                print(f'Prime factor = {i}')
                number /= i
                prime = i
                i -= 1
        print(f'Largest prime number: {prime}')
        return prime
    

# %%
while True:
    try:
        number = int(input('Enter the number >>> '))
        break
    except:
        print('Enter the integer number.')
        
largest_prime = Largest_Prime(number)
largest_prime.print_largest_prime(number)
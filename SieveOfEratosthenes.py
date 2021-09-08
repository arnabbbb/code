# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:45:30 2021

@author: arnab19
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    
    for divisor in range(2, bound):
        for i in range(divisor + 1 , bound):
            if i % divisor == 0 and i in answer:
                answer.remove(i)
            else:
                continue
    return answer
            
                
print(compute_primes(200))
print(len(compute_primes(200)))
print(len(compute_primes(2000)))
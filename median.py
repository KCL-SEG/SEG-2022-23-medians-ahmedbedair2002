"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from statistics import median


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

def findMedian(numbers):
    numbers.sort()
    if len(numbers)%2:
        median = numbers[(len(numbers)//2)]
        return median
    else:
        median = (numbers[len(numbers)//2]+numbers[(len(numbers)//2)-1])/2
        return median

print(findMedian(numbers))

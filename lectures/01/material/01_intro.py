
from typing import List


# autocomplete a basic function ... 
def calculate_average(a, b):
    """
    Calculates the average of two numbers.
    """
    return (a + b) / 2	

# autocompletion varies according to context (different parameters)
def calculate_average_args(*args):
    """
    Calculates the average of a list of numbers.
    
    """ 
    return sum(args) / len(args)	

# autocomplete a function with a list parameter
def calculate_average_list(numbers):
    """
    Calculates the average of a list of numbers.
    """
    return sum(numbers) / len(numbers)

# with additional information the code generation will adapt
# (type annotations and docstrings)
def calculate_mean_age(ages: List[int]):
    """
    Calculates the mean age of a list of ages.
    If the list is empty, or one of the ages is negative the funtions throws an ReferenceError 
    """
    if len(ages) == 0:
        raise ReferenceError("The list of ages is empty")
    for age in ages:
        if age < 0:
            raise ReferenceError("The list of ages contains negative values")
    return sum(ages) / len(ages)


def main():
    """
    Main program that calls the calculate_average function.
    """
    print(calculate_average_args(1,3))

    


if __name__ == '__main__':
    main()
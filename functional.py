# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''

Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?

We ensure immutability by assigning the array's initial value within the method (function). When this function is invoked with an array as its parameter, Python stores the new object's address in memory.
----------------------------------------------------------------------------------------------------------------------------------------
Is this solution a pure function? Why or why not?

It is a pure function. If you provide the same input, the function will always return the same output, with no side effects.
----------------------------------------------------------------------------------------------------------------------------------------
Is this solution a higher order function? Why or why not?

It is not a higher order function. It does not accept one or more functions as an argument, and it does not return a function.
----------------------------------------------------------------------------------------------------------------------------------------
Would it have been easier to solve this problem using a different programming style?

No, this style is simple, avoids verbosity, and is efficient. the builtin method "sorted" allows you to arrange the iterable in ascending order.
----------------------------------------------------------------------------------------------------------------------------------------
Why in particular is functional programming a helpful paradigm when solving this problem?

As a declarative programming style, its main focus is What to solve, as opposed to an imperative style focusing on How to solve. This solves problems in a very simple, effective way.

'''
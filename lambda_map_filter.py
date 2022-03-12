import functools

lin = [2, 3, 4, 5, 6, 7, 8]

# lambda() is used to create functions that are quickly needed or functions to be used in other functions(Higher Order)
# map performs operations defined in the lambda expression/function on each element of the used/defined list and returns a list/tuple

# this multiplies each element of the list 'lin' by 2
a = map(lambda x: x*2, lin)
print(list(a))
# or    print(tuple(a))

# filter() returns a list/tuple containing elements from the used/defined list that meets the requirements in the lambda expression/function
b = filter(lambda x: x % 4 == 0, lin)
print(list(b))
# or    print(tuple(b))


# reduce() performs whatever is defined in the function/lambda expression on all elements of the list to return a single value
c = functools.reduce(lambda x, y: x+y, lin)
print(c)


# another map example
print("")
yin = [2, 3, 4, 5, 6, 7, 8]
yan = [4, 7, 4, 12, 6, 7, 11]

# returns a list with each element as a result of adding elements of same index from both list yin and yan
egg = map(lambda x, y: x+y, yin, yan)
print(list(egg))

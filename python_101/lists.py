### lists

squares = [1, 4, 9, 16, 25]
squares[0]  # indexing returns the item
squares[-1] #25
squares[-3:]  # slicing returns a new list
# [9, 16, 25]

# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:
squares[:]
# [1, 4, 9, 16, 25]
# A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
# A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

# support concatenation
squares + [36, 49, 64, 81, 100]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

cubes = [1, 8, 27, 65, 125]  # something's wrong here
# >>> 4 ** 3  # the cube of 4 is 64, not 65!
#64
cubes[3] = 64  # replace the wrong value
cubes
#[1, 8, 27, 64, 125]

# appending to end
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes
# [1, 8, 27, 64, 125, 216, 343]

# length:
letters = ['a', 'b', 'c', 'd']
len(letters)
# 4

# nested lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
# [['a', 'b', 'c'], [1, 2, 3]]
x[0]
# ['a', 'b', 'c']
x[0][1]
# 'b'

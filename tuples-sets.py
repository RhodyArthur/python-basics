# Task 6.1: Unpack tuple (3 points)
# Create a tuple of coordinates `(x, y, z)`. Write a function `unpack_coordinates(coords)` that unpacks and returns them as three separate values.

def unpack_coordinates(coords):
    x, y, z = coords
    return x, y, z


# Task 6.2: Get unique elements (3 points)
# Write a function `get_unique(lst)` that returns unique elements from a list using sets.
def get_unique(lst):
    return set(lst)


# Task 6.3: Set intersection (4 points)
# Write a function `set_intersection(set1, set2)` that finds the intersection of two sets.
def set_intersection(set1, set2):
    return set1.intersection(set2)

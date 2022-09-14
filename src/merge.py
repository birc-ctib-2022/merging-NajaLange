"""Code for merging two sorted lists."""


from ast import Break


def merge(x: list[int], y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    i, j = 0, 0
    z = []  # a new list to copy elements into
    # FIXME: fill out the loop so you merge the lists
    # until one of them is empty

    while i < len(x) and j < len(y):
        if x[i] <= y[j]: 
            z.append(x[i])
            i += 1
        if y[j] <= x[i]: 
            z.append(y[j])
            j += 1
        if i < len(x) and j == len(y):
            z.append(x[i])
        if j < len(y) and i == len(x):
            z.append(x[j])
 
        
    # FIXME: you shouldn't just break here
    # At least one of the lists is empty now. Copy the
    # remainder of the other into z.
    return z
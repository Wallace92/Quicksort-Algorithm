x = [7,2,5,4,10,12,5,4,4]

def sort(x):
    less = []
    equal = []
    greater = []

    if len(x) > 1:
        pivot = x[0]
        for i in x:
            if i < pivot:
                less.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                greater.append(i)
        # Don't forget to return something!
        print("less", less, "equal", equal, "greater", greater)
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists

    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return x

q = sort(x)
print (q)

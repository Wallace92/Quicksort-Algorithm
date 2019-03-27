

def sort(list_of_elements):

    less = []
    equal = []
    greater = []
    number_of_elements = len(list_of_elements)

    if number_of_elements > 1:

        pivot = list_of_elements[0]
        print("Number_of_elements=%d and pivot=%d" % (number_of_elements, pivot))
        for i in list_of_elements:
            if i < pivot:
                less.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                greater.append(i)
        print("less", less, "equal", equal, "greater", greater)
        return sort(less) + equal + sort(greater)  #No sort for equal elements!
    else:
        return list_of_elements


x = [7, 2, 5, 4, 10, 12, 5, 4, 4]
q = sort(x)
print(q)

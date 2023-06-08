#write a python program to iterate a given list and count the occurrence of_each element and create a dictionary to show the count of each element

def count_elements(lst):
    element_count = {}
    for element in lst:
        if element not in element_count:
            element_count[element] = 0
        element_count[element] += 1
    return element_count

# Example usage:
my_list = [1, 2, 3, 2, 1, 3, 1, 1, 4, 5, 4]
result = count_elements(my_list)
print(result)
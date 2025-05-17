"""
Binary Search
-Only applies to ordered lists
"""
def binary_search(ordered_list, search_value):
    first = 0
    last = len(ordered_list) - 1

    while first <= last:
        middle = (first + last) // 2
        if search_value == ordered_list[middle]:
            return True
        elif search_value < ordered_list[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False

"""
Complexity: O(log n)
"""

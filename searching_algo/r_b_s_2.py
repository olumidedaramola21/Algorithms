def binary_search_recursive(ordered_list, search_value):
    # define the base case
    if len(ordered_list) == 0:
        return False
    else:
        middle = len(ordered_list) // 2

        # check if middle value is search_value
        if ordered_list[middle] == search_value:
            return True
        elif ordered_list[middle] < search_value:
            return binary_search_recursive(ordered_list[middle:], search_value)
        else:
           return  binary_search_recursive(ordered_list[:middle], search_value)


def binary_search_recursive(arr, target, low=0, high=None):
    """
    Perfom a recursive binary search to find target in a sorted array.

    Args:
        arr: A sorted array (list) of elements
        target: the search value
        low: The lower bound index to search for
        high: The upper bound index to search for
    
    returns:
        The index of the target if found, otherwise -1
    """
    # Init high, if no value is provided
    if high is None:
        high = len(arr) - 1

    # Base case: element not found
    if low > high:
        return -1
    
    # find the middle index
    mid = (high + low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, low, mid + 1)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
        

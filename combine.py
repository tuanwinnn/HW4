def combine_lists(list1, list2):
    # Validate inputs are lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError
    
    # Check all elements are integers
    for item in list1:
        if not isinstance(item, int):
            raise TypeError
    
    for item in list2:
        if not isinstance(item, int):
            raise TypeError
    
    # Merge the two lists
    merged = list1 + list2
    
    # Implement bubble sort to sort the merged list
    n = len(merged)
    for i in range(n):
        for j in range(0, n - i - 1):
            if merged[j] > merged[j + 1]:
                # Swap elements
                merged[j], merged[j + 1] = merged[j + 1], merged[j]
    
    return merged
def combine_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError
    
    for item in list1:
        if not isinstance(item, int):
            raise TypeError
    
    for item in list2:
        if not isinstance(item, int):
            raise TypeError
    
    # Merge and remove duplicates using a set
    merged = list(set(list1 + list2))
    
    # Bubble sort in descending order
    n = len(merged)
    for i in range(n):
        for j in range(0, n - i - 1):
            if merged[j] < merged[j + 1]:
                merged[j], merged[j + 1] = merged[j + 1], merged[j]
    
    return merged
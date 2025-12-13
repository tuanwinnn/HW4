def filter_young(dictionary):
    # Filter people under 30
    result = []
    
    for name, (phone, age) in dictionary.items():
        if age < 30:
            result.append((name, phone))
    
    # Sort alphabetically by name
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j][0] > result[j + 1][0]:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result
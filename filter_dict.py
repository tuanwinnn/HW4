def filter_young(dictionary):
    result = []
    
    # Filter people under 30
    for name, value in dictionary.items():
        phone = value[0]
        age = value[1]
        if age < 30:
            result.append((name, phone))
    
    # Sort alphabetically by name (ascending)
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j][0] > result[j + 1][0]:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result
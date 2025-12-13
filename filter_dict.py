def filter_young(data):
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")
    
    result = []
    
    for name, value in data.items():
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("Each value must be a (phone, age) tuple")
        
        phone, age = value[0], value[1]
        
        if age < 30:
            result.append((name, phone))
    
    # Bubble sort by name (no built-in sort)
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j][0] > result[j + 1][0]:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result
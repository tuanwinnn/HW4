def reverse_sort_dictionary(input_dict):
    # Get list of names (keys)
    names = list(input_dict.keys())
    
    # Sort names in reverse order (without using built-in sort)
    n = len(names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if names[j] < names[j + 1]:
                # Swap elements for reverse order
                names[j], names[j + 1] = names[j + 1], names[j]
    
    # Build result list with (name, phone_number) tuples
    result = []
    for name in names:
        phone_number = input_dict[name][0]  # First element of tuple is phone
        result.append((name, phone_number))
    
    return result
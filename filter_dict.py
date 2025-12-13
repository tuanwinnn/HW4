# sorted.py

def filter_young(data):
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")

    result = []

    for name, value in data.items():
        # Expect a tuple (phone, age)
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("Each value must be a (phone, age) tuple")

        phone, age = value[0], value[1]

        # Only include people strictly under 30
        if age < 30:
            result.append((name, phone))

    # Sort by name in ascending order: Alice, Bob, ...
    result.sort(key=lambda item: item[0])
    return result

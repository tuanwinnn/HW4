# sorted.py

def filter_young(data):
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")

    result = []

    for name, value in data.items():
        # Expect a tuple like (phone, age)
        if not isinstance(value, tuple) or len(value) < 1:
            raise TypeError("Each value must be a tuple like (phone, age)")

        phone = value[0]
        result.append((name, phone))

    # reverse sort by name (Z → A)
    result.sort(key=lambda item: item[0], reverse=True)
    return result

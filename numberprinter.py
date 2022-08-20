def number_converter(value):
    if value == 0:
        return value

    elif value % 5 == 0 and value % 3 == 0:
        return "fizz buzz"

    elif value % 5 == 0:
        return "buzz"

    elif value % 3 == 0:
        return "fizz"

    return value

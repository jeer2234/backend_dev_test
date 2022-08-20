from .numberprinter import number_converter

# from .. import main

multiples_of_3 = [x * 3 for x in range(1, 1001)]

multiples_of_5 = [x * 5 for x in range(1, 1001)]

multiples_of_5_and_3 = list(set(multiples_of_5) & set(multiples_of_3))


def test_first_1000_values():
    for number in range(1001):
        if number in multiples_of_5_and_3:
            assert number_converter(number) == "fizz buzz"

        elif number in multiples_of_5:
            assert number_converter(number) == "buzz"

        elif number in multiples_of_3:
            assert number_converter(number) == "fizz"

        else:
            assert number_converter(number) == number


def test_negative_values():
    assert number_converter(-3) == "fizz"
    assert number_converter(-5) == "buzz"
    assert number_converter(-90) == "fizz buzz"


def test_zero_values():
    assert number_converter(0) == 0

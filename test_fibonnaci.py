from .fibonacci import fibonacci


def test_fibonacci_series():

    fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

    for sequence in range(20):
        assert fibonacci(sequence) == fibonacci_list[sequence]


def test_real_numbers():
    assert fibonacci(2.3) == -1


def test_negative_values():
    assert fibonacci(-5) == -1

def test_zero_values():
    assert fibonacci(0) == 0

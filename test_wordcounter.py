from .wordcounter import word_count


def test_1():

    assert word_count('lincon, michel, and me') == {'lincon': 1, 'michel': 1, 'and': 1, 'me': 1}


def test_2():
    assert word_count("Hi how are things? How are you? Are you a developer? I am also a developer") == {
        "hi": 1, "how": 2, "are": 3, "things": 1, "you": 2, "a": 2, "developer": 2, "i": 1, "am": 1,
        "also": 1}


def test_3():
    assert word_count("Code a program (in python) that displays the numbers from 1 to 100 on the screen,"
                      " substituting the multiples of 3 for the word") == {'code': 1, 'a': 1, 'program': 1, 'in': 1, 'python': 1, 'that': 1, 'displays': 1, 'the': 4, 'numbers': 1,'from': 1, '1': 1, 'to': 1, '100': 1, 'on': 1, 'screen': 1, 'substituting': 1, 'multiples': 1, 'of': 1,'3': 1, 'for': 1, 'word': 1}

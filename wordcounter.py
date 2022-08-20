def word_count(string):
    from re import sub
    from string import punctuation

    word_record = dict()
    words = sub('[' + punctuation + ']', '', string).lower().split()

    for word in words:
        if word in word_record:
            word_record[word] += 1
        else:
            word_record[word] = 1

    return word_record


print(word_count(
    "Code a program (in python) that displays the numbers from 1 to 100 on the screen, substituting the multiples of 3 for the word"))

def get_num_words(data):
    return len(data.split())


def get_letter_count(data):
    data_prc = data.lower()
    letter_count = {}
    for letter in data_prc:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def _sort_on(d):
    return d[list(d.keys())[0]]

def sort_data(letter_count):
    all_letters = []
    for d in letter_count:
        if d.isalpha():
            all_letters.append({d: letter_count[d]})
    all_letters.sort(reverse=True, key=_sort_on)
    return all_letters


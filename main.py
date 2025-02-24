import sys
from stats import get_num_words, get_letter_count, sort_data


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    letters = sort_data(get_letter_count(book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    for letter in letters:
        print(f"{list(letter.keys())[0]}: {letter[list(letter.keys())[0]]}")
    print("============= END ===============")


main()



import sys

def main() -> int:
    try:
        print_book_info_report("books/frankenstein.txt")
    except Exception as err:
        print(f"Error occurred: {err}")
    return 0

def get_book_content(filepath) -> str:
    with open(filepath) as f:
        return f.read()

def get_word_count(text) -> int:
    words = text.split()
    return len(words)

def get_letter_count(text) -> dict:
    counts = {}
    for letter in text:
        letter = letter.lower()

        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    return counts

def print_book_info_report(book_filepath):
        book_content = get_book_content(book_filepath)
        wc = get_word_count(book_content)
        lc = get_letter_count(book_content)
        letters = list(lc)
        letters.sort()
        print(f"--- Begin report of {book_filepath} ---")
        print(f"{wc} words found in the document\n")
        for letter in letters:
            if not letter.isalpha():
                continue
            count = lc[letter]
            print(f"The '{letter}' character was found {count} times")

if __name__ == '__main__':
    sys.exit(main())

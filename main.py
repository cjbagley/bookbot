import sys

def main() -> int:
    try:
        book_filepath = "books/frankenstein.txt"
        book_content = get_book_content(book_filepath)
        wc = get_word_count(book_content)
        print(f"Wordcount for {book_filepath}: {wc}")
        lc = get_letter_count(book_content)
        print("Printing letter counts - get ready...")
        print(lc)
    except:
        print("Error occurred")
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

if __name__ == '__main__':
    sys.exit(main())

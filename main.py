from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    try:
        with open(sys.argv[1]) as f:
        # do something with f (the file) here

            # f is a file object
            file_contents = f.read()

            return file_contents
    except FileNotFoundError:
        print(f"File {sys.argv[1]} not found.")
        sys.exit(1)


def main():
    print("============ BOOKBOT ============\n"
              "Analyzing book found at {sys.argv[1]}...\n"
              "----------- Word Count ----------\n"
              f"Found {get_book_word_count(get_book_text())} total words\n"
              "--------- Character Count -------")
    
    for key,value in get_sorted_dict(get_char_count(get_book_text())).items():
        if key.isalpha():
            print(f"{key}: {value}")

    print("============= END ===============\n")
main()
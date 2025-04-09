def get_book_word_count(book):
    return f"{len(book.split())}"

def get_char_count(book):
    char_dict = dict()
    book = book.lower()
    for i in range(len(book)):
        char_dict[book[i]] = char_dict.get(book[i], 0) + 1
    
    return char_dict
    
def get_sorted_dict(char_dict):
    sorted_dict = dict()
    for i in sorted(char_dict.keys()):
        sorted_dict[i] = char_dict[i]
    
    return sorted_dict
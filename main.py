import sys
from stats import count_words, count_chars, sort_dict

def get_book_text(filepath):
    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        file_contents = f.read()
        return file_contents

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    bookpath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    booktext = get_book_text(bookpath)
    print("----------- Word Count ----------")
    num_words = count_words(booktext)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = count_chars(booktext)
    sorted_list = sort_dict(char_count)
    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")
        
main()

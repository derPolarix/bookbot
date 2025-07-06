from stats import count_words, count_chars, sort_dict

def get_book_text(filepath):
    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    booktext = get_book_text("books/frankenstein.txt")
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

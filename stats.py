def count_words(book_content):
    split_text = book_content.split()
    return len(split_text)

def count_chars(book_content):
    char_dict = {}
    for char in book_content:
        lowercase_char = char.lower()
        if lowercase_char in char_dict:
            char_dict[lowercase_char] += 1
        else:
            char_dict[lowercase_char] = 1

    return char_dict

def sort_dict(input_dict):
    output_list = []

    def sort_on(item):
        return item["num"]

    for entry in input_dict:
        new_entry = {"char": entry, "num": input_dict[entry]}
        output_list.append(new_entry)
        
    output_list.sort(reverse=True, key=sort_on)
    return output_list

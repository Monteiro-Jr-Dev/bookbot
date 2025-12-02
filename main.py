from stats import *
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        text_file = f.read()        
    return text_file

def sort_on(items):
    return items["quant"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print('============ BOOKBOT ============')
    path = sys.argv[1]
    book = get_book_text("./"+path)
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f'Found {get_word_count(book)} total words')
    dic_char = get_char_count(book)
    print("--------- Character Count -------")
    list_char = dict_to_list(dic_char)
    for i in list_char:
        if i["letter"].isalpha():
            print(f'{i["letter"]}: {i["quant"]}')
    print("============= END ===============")
main()
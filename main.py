import sys
from stats import get_num_words, get_char_dict, sort_dict_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    char_dict = get_char_dict(book_text)
    sort_dict_list(char_dict)
    print_results(file_path, num_words, char_dict)

def print_results(file_path, num_words, char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path[2:]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in char_dict.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == "__main__":
    main()

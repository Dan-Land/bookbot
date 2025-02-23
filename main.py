import sys
from stats import get_num_words

def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    num_words = get_num_words(file_contents)
    # print(file_contents)
    print(f"{num_words} words found in the document")
    char_occur = get_char_occur(file_contents)
    get_report(char_occur, num_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_char_occur(book):
    char_occur = {}

    lowered_book = book.lower()
    char_array = list(lowered_book)
    for char in char_array:
        if char in char_occur:
            char_occur[char] += 1
        else:
            char_occur[char] = 1

    return char_occur


def get_report(char_occur, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    temp_list = []
    for char, count in char_occur.items():
        if char.isalpha():
            temp_list.append({"char": char, "count": count})

    temp_list.sort(key=lambda x: x["count"], reverse=True)

    for char_dict in temp_list:
        character = char_dict["char"]
        character_count = char_dict["count"]
        print(f"The '{character}' character was found {character_count} times")

main()
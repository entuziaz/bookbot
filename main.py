import sys
from stats import count_words, count_characters, sort_list

def get_book_text(f): 
    file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
        

    with open(sys.argv[1]) as f:
        book_content = get_book_text(f) 
        word_count = count_words(book_content)
        char_count = count_characters(book_content)
        sorted_list = sort_list(char_count)

        # print(f"{word_count} words found in the document") 
        # print(f"{char_count} characters found in the document") 

        print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
        for char in sorted_list:
            if char['char'].isalpha():
                print(f"{char['char']}: {char['num']}")
        print("============= END ===============")

main()

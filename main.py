
def get_book_text(f): 
    file_contents = f.read()
    return file_contents

def main():
    with open('books/frankenstein.txt') as f:
        book_content = get_book_text(f) 
        word_count = count_words(book_content)
        print(f"{word_count} words found in the document") 

def count_words(text):
    words = text.split()
    return len(words)


main()

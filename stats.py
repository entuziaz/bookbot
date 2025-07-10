def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower_case = text.lower()
    # following could be replaced with collections.Counter
    # such that: return Counter(lower_case)
    counted_chars = {}
    for letter in lower_case:
        if letter in counted_chars:
            counted_chars[letter] += 1
        else:
            counted_chars[letter] = 1
    return counted_chars

def sort_on(items):
    return items["num"]

def sort_list(counted_chars):
    new_list = []
    for item in counted_chars:
        char = item 
        num = counted_chars[item]
        new_list.append({"char": char, "num": num})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
    

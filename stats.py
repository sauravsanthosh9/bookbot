def get_number_of_words(text):
    words_in_docment = text.split()

    return f"Found {len(words_in_docment)} total words"
    
def count_of_characters(text):
    char_count = {}

    for char in text:
        char = char.lower()

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(dict):
    return dict["count"]

def alphabetically_sorted_count_of_characters(char_count):
    chars_list = []
    
    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
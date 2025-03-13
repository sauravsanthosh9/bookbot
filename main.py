import sys
from stats import get_number_of_words, count_of_characters, alphabetically_sorted_count_of_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    
    with open(path) as f:
        file_contents = f.read()
    
    word_count = get_number_of_words(file_contents)
    
    char_count = count_of_characters(file_contents)
    
    sorted_chars = alphabetically_sorted_count_of_characters(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
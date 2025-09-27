from stats import*
import sys

def main():
    if len(sys.argv) == 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    filepath = sys.argv[1]
    words_num = words_in_text(filepath)
    text = get_book_text(filepath)
    sorted_dict = sort_dict(get_character_count(text))
    print(f"============ BOOKBOT ============ \nAnalyzing book found at {filepath}...\n----------- Word Count ---------- \nFound {words_num} total words \n--------- Character Count -------")
    for item in sorted_dict:
        if item.isalpha() ==True:
            print(f'{item}: {sorted_dict[item]}')
    print('============= END ===============')

main()

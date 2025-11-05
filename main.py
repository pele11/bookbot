import sys
from stats import get_num_words,get_chars_dict,chars_dict_to_sorted_list



def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        text = file.read()  
        return text

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)



    file_path = sys.argv[1] 
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    chars_dict = get_chars_dict(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print_report(file_path, word_count, chars_sorted_list)
    
    # for letter, count in sorted(chars_dict.items()):
    #     print(f"{letter}: {count}") 


    # print('Letter counts:')
    # for letter, count in sorted(chars_dict.items()):
    #     print(f"'{letter}': {count}") 
    # print(chars_dict)
    # print(f'Found {word_count} total words')


def print_report(file_path, word_count, chars_sorted_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    i=0
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
        i+=1
        if i>=2:
            break

    print("============= END ===============")
    


if __name__ == "__main__":
    main()


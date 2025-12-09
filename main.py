from pathlib import Path
import sys 
from stats import get_num_words, get_num_characters

def get_book_text(filepath: str) -> str:
    with open(file=filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    BASE_DIR = Path(__file__).resolve().parent

    file_path = BASE_DIR / sys.argv[1]

    content = get_book_text(filepath=file_path)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(content=content)
    print("--------- Character Count -------")
    char_dict = get_num_characters(content=content)
    for key, value in char_dict:
        if str(key).isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
    

main()
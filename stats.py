def get_num_words(content: str):

    print(f"Found {len(content.split())} total words")

def get_num_characters(content: str):

    char_dict = {}

    words_array = content.split()

    for word in words_array:
        for character in word:
            lowered_character = character.lower()
            if char_dict.get(lowered_character):
                char_dict[lowered_character] += 1
            else:
                char_dict[lowered_character] = 1
    
    char_array = list(char_dict.items())
    
    def sort_on(items):
        return items[1]

    char_array.sort(reverse=True, key=sort_on)
    return char_array


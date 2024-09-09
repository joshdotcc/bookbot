def count_words(book):
    all_words = book.split()
    return len(all_words)

def total_chars(book):
    all_words = book.split()
    all_chars = {}
    for word in all_words:
        total = 0
        for character in word:
            lower_character = character.lower()
            if lower_character in all_chars:
                all_chars[lower_character] += 1
            else:
                all_chars[lower_character] = 1
    return all_chars


def sort_on(dict):
    return dict["num"]


def final_output(path, char_counts, word_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in this document \n" )
    for char in char_counts:
        print(f"The {char[0]} character was found {char[1]} times")
    print('--- End report ---')
        
def main():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        the_book = f.read()
        word_count = count_words(the_book)
        all_chars = total_chars(the_book)

    
    char_counts = [(key, value) for key, value in all_chars.items()]
    char_counts.sort(reverse=True, key=lambda x: x[1])
    
    final_output(path, char_counts, word_count)
main()
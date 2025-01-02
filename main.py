def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_counts(text)
    num_letter = dict_letter_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for letter in num_letter: 
        print(f"The '{letter}' character was found {num_letter[letter]} times")
    print("-- End report --")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_counts(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]


def dict_letter_count(text): 
    counts = {}
    lowered_text = text.lower()
    for character in lowered_text: 
        if character.isalpha():
            if character in counts: 
                counts[character] += 1
            else: 
                counts[character] = 1
    for freq in sorted(counts, key=counts.get, reverse=True):
        freq, counts[freq]

    return counts
  
main()
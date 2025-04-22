input_str = "heLLo how Are yOu"

# Function to sort each word by ignoring case but retaining original case
def sort_word_preserve_case(word):
    # Pair each character with its lowercased version
    paired_chars = sorted((char, char.lower()) for char in word)
    print(f"paired_chars::{paired_chars}")
    # Sort based on the lowercased version
    sorted_chars = [char[0] for char in sorted(paired_chars, key=lambda x: x[1])]
    print(f"sorted_chars::{sorted_chars}")
    # Join sorted characters back into a string
    return ''.join(sorted_chars)

# Split the string into words
words = input_str.split()

# Sort each word and retain original case
sorted_words = [sort_word_preserve_case(word) for word in words]

# Join the sorted words back into a sentence
sorted_str = ' '.join(sorted_words)

print(sorted_str)
def count_words(file_path):
    with open(file_path) as f:
        text = f.read()
    s = text.split()
    return len(s)

def frequency_distribution(file_path):
    with open(file_path) as f:
        text = f.read()
    s = text.lower()    
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def print_stats(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    word_count = count_words(file_path)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    freq = frequency_distribution(file_path)
    # Only print alphabetic characters
    sorted_freq = sorted(
        ((char, count) for char, count in freq.items() if char.isalpha()),
        key=lambda x: x[1],
        reverse=True
    )
    for char, count in sorted_freq:
        print(f"{char}: {count}")
    print("============= END ===============")

# Example usage:
# print_stats("books/frankenstein.txt")
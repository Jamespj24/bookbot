import sys
from stats import count_words, frequency_distribution

def main():
    file_path = 'books/frankenstein.txt'
    num_words = count_words(file_path)
    print(f"The book has about {num_words} words.")
    freq_dist = frequency_distribution(file_path)

    print(freq_dist)
    print(sys.argv)


if __name__ == "__main__":
    main()
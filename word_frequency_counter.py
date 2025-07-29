import string

def clean_word(word):
    return word.strip(string.punctuation).lower()

def count_words(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()
        words = [clean_word(word) for word in text.split()]
        freq = {}
        for word in words:
            if word:
                freq[word] = freq.get(word, 0) + 1
        top_five = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        print("Top 5 Frequent Words:")
        for word, count in top_five:
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found.")

# Usage:
# count_words('sample.txt')

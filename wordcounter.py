import sys

def count_word_frequency(filename):
    word_count = {}

    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()

        for word in words:
            word = ''.join(filter(str.isalnum, word)).lower()

            if word:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count

if len(sys.argv) != 2:
    print("Usage: python word_frequency.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
word_count = count_word_frequency(filename)


sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

n = int(input("Enter the value of n: "))

if n <= 0:
    print("n must be a positive number")
else:
    print(f"The {n} most common words in the file {filename} are:")
    for i in range(min(n, len(sorted_word_count))):
        word, count = sorted_word_count[i]
        print(f"{word}: {count} times")

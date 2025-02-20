import requests

link1 = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"
author1 = "Herman Melville"
book1 = "Moby Dick"
link2 = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
author2 = "William Shakespeare"
book2 = "Romeo and Juliet"

def get_unique_words(link):
    """Fetches the book text from the link and counts unique words."""
    result = requests.get(link)
    unique_words = {}
    punctuation = ";,.'!?-=()"

    for line in result.text.splitlines():
        for p in punctuation:
            line = line.replace(p, " ")
        words = line.split()
        for word in words:
            word = word.lower()
            unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words

def compare_books(link1, author1, link2, author2):
    """Compares the unique words used by two different authors."""
    words1 = get_unique_words(link1)
    words2 = get_unique_words(link2)

    unique_count1 = len(words1)
    unique_count2 = len(words2)

    print(f"{author1} used {unique_count1} unique words in {book1}.")
    print(f"{author2} used {unique_count2} unique words in {book2}.")

    if unique_count1 > unique_count2:
        print(f"{author1} used more unique words than {author2} in {book1}.")
    elif unique_count2 > unique_count1:
        print(f"{author2} used more unique words than {author1} in {book2}.")
    else:
        print(f"Both authors used the same number of unique words.")

compare_books(link1, author1, link2, author2)
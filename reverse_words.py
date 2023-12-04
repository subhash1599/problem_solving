def reverse_words(words):
    word_split=words.split()
    reverse_words=word_split[::-1]

    return ' '.join(reverse_words)


if __name__=="__main__":
    print(reverse_words("me creates gaming"))
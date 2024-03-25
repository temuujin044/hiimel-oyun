import nltk

# Download the words corpus from NLTK
nltk.download('words')

# Get the set of English words
english_words = set(nltk.corpus.words.words())

# Write the English words to a text file
with open('english_words.txt', 'w') as f:
    for word in english_words:
        f.write(word + '\n')
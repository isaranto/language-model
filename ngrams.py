from collections import Counter


# remove punctuation from text, convert to lowercase and return word list
# and dictionary with word frequency
def normalize_text(file):
    words = []
    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', " '","' "]
    with open(file, 'r') as f:
        for line in f:
            for word in line.split():
                for i in punctuation:
                    word = word.replace(i,"")
                words.append(word.lower())
    un_frequency = Counter(words).most_common()
    return (words,un_frequency)


# generate bigrams and bigram frequency dictionary
def gen_bigrams(word_list):
    bigrams = []
    for i in range(len(word_list)-1):
        bigrams.append((word_list[i], word_list[i+1]))
    bi_frequency = Counter(bigrams).most_common()
    return (bigrams, bi_frequency)


def gen_trigrams(word_list):
    trigrams = []
    for i in range(len(word_list)-2):
        trigrams.append((word_list[i], word_list[i+1], word_list[i+2]))
    tri_frequency = Counter(trigrams).most_common()
    return (trigrams, tri_frequency)


def create_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])


def laplace_smoothing(word_list, vocabulary, word_frequency):
    pass


if __name__ == '__main__':
    words, un_frequency = normalize_text('./texts/small_training_set')
    bigrams, bi_frequency = gen_bigrams(words)
    trigrams, tri_frequency = gen_trigrams(words)
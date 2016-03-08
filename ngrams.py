from collections import Counter
from operator import itemgetter


# remove punctuation from text, convert to lowercase and return word list
# and dictionary with word frequency
def normalize_text(file):
    words = []
    punctuation = ['(', ')', ':', ';', ',', '/', '"', " '","' "]
    new_sentence= ['.', '!', '?']
    with open(file, 'r') as f:
        for line in f:
            for word in line.split():
                for i in punctuation:
                    word = word.replace(i,"")
                for i in word:
                    if i in new_sentence:
                        word = word.replace(i, " *start*")
                        for new_word in word.split():
                            words.append(new_word)
                        break
                else:
                    words.append(word.lower())
    un_frequency = Counter(words)
    words = [ word if un_frequency[word] > 10 else "*unknown*" for word in words]
    un_frequency = Counter(words)
    return (words,un_frequency)


# generate bigrams and bigram frequency dictionary
def gen_bigrams(word_list):
    bigrams = []
    for i in range(len(word_list)-1):
        bigrams.append((word_list[i], word_list[i+1]))
    bi_frequency = Counter(bigrams)
    return (bigrams, bi_frequency)


def gen_trigrams(word_list):
    trigrams = []
    for i in range(len(word_list)-2):
        trigrams.append((word_list[i], word_list[i+1], word_list[i+2]))
    tri_frequency = Counter(trigrams)
    return (trigrams, tri_frequency)


def create_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])


def laplace_smoothing(word_frequency):
    vocabulary = [key for key in word_frequency]
    laplace = {}
    for word in word_frequency:
        laplace[word] = word_frequency['word'] + 1 / len(vocabulary)


if __name__ == '__main__':
    words, un_frequency = normalize_text('./texts/small_training_set')
    bigrams, bi_frequency = gen_bigrams(words)
    trigrams, tri_frequency = gen_trigrams(words)

    new_d = {k:v for i,(k,v) in enumerate(un_frequency.iteritems())
       }
    items = new_d.items()
    items.sort(key=itemgetter(1),reverse=True)
    print words[:50]
    #print sorted(new_d.iteritems(),key= lambda x: x[1],reverse=True)

from numpy import zeros
# coding=utf-8
basic = raw_input("Insert initial word.\n")
new_word = raw_input("Insert the word you would like to convert to '" + basic + "'\n")


def edit_distance(basic, new_word):
    ed = zeros((len(basic)+1, len(new_word)+1), dtype=int)
    ed[1:,0] = range(1, len(basic)+1)
    ed[0,1:] = range(1, len(new_word)+1)
    for i in range(1, len(basic)+1):
        for j in range(1, len(new_word)+1):
            ed[i,j] = min(1+ed.item(i-1, j),
                        1+ed.item(i, j-1),
                        diff(i, j, basic, new_word) + ed.item(i-1, j-1))
    return (ed, ed.item(len(basic), len(new_word)))


def diff(i, j, word1, word2):
    if word1[i-1] == word2[j-1]:
        return 0
    else:
        return 2 #replace has a cost of 2

def print_matrix(basic, new_word, ed):
    print "  #",
    for i in range(0, len(new_word)):
        print new_word[i],"|",
    print ""
    for i in range(0, len(basic)+1):
        if i == 0:
            print "#",
        else:
            print basic[i-1],
        for j in range(0, len(new_word)+1):
            print ed.item(i, j),"|",
        print ""


def more_than_distance(word, dictionary, min):
    with open(dictionary, 'r') as f:
        for line in f:
           m,i = edit_distance(word,line)
           if i <= min:
               print line

#try to split a line into words
def more_than_this_distance(word, dictionary, min):
    with open(dictionary, 'r') as f:
        for line in f:
            for leksi in line.split():
                m,i = edit_distance(word,leksi)
                if i <= min:
                    print line


if __name__ == '__main__':
    matrix,min_ed = edit_distance(basic, new_word)
    print_matrix(basic,new_word,matrix)
    """more_than_distance(basic,'/usr/share/dict/british-english',2)"""
    """more_than_this_distance(basic,
                            '/home/lias/Downloads/europarl-v7.el-en.en',2)"""
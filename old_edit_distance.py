from numpy import zeros
# coding=utf-8
basic = raw_input("Insert initial word.\n")
new_word = raw_input("Insert the word you would like to convert to '" + basic + "'\n")
"""E(i, j) = min 1 + E(i − 1, j), 1 + E(i, j − 1), diff(i, j) + E(i − 1, j − 1)
edit_distance(i,j)=min( 1+edit_distance(i[:-1],j), 1+edit_distance(i,j[:-1], 1 + edit_distance(i[:-1],j[:-1]))
"""


def edit_distance(basic, new_word):
    ed = zeros((len(basic)+1, len(new_word)+1), dtype=int)
    for i in range(0, len(basic)+1):  #initialize matrix
        ed[i, 0] = i
    for j in range(1,len(new_word)+1):
        ed[0, j] = j
    for i in range(1, len(basic)+1):
        for j in range(1, len(new_word)+1):
            ed[i,j] = min(1+ed.item(i-1, j),
                        1+ed.item(i, j-1),
                        diff(i, j) + ed.item(i-1, j-1))
    return (ed, ed.item(len(basic), len(new_word)))


def diff(i,j):
    if basic[i-1] == new_word[j-1]:
        return 0
    else:
        return 1

def print_matrix(basic, new_word,ed):
    print " #",
    for i in range(0, len(new_word)):
        print new_word[i], " ",
    print ""
    for i in range(0, len(basic)+1):
        if i == 0:
            print '#',
        else:
            print basic[i-1],
        for j in range(0, len(new_word)+1):
            print ed.item(i, j),
        print ""

def more_than_distance(word,dictionary,min):
    with open(dictionary, 'r') as file:
        for line in file:
            m,i = edit_distance(word,line)
            if i <= min:
                print line


if __name__ == '__main__':
    matrix,min_ed = edit_distance(basic, new_word)
    """print_matrix(basic,new_word,matrix)"""
    more_than_distance(basic,'/usr/share/dict/british-english',1)



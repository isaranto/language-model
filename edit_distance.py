import numpy
# coding=utf-8
basic = raw_input("Insert initial word.\n")
new_word = raw_input("Insert the word you would like to convert to '" + basic +"'\n")
"""E(i, j) = min 1 + E(i − 1, j), 1 + E(i, j − 1), diff(i, j) + E(i − 1, j − 1)
edit_distance(i,j)=min( 1+edit_distance(i[:-1],j), 1+edit_distance(i,j[:-1], 1 + edit_distance(i[:-1],j[:-1]))
"""
ed = numpy.zeros((len(basic)+1,len(new_word)+1),dtype=numpy.int8)
ed[0,0]=0
for i in range(0,len(basic),1): #initialize matrix
    ed[i,0]=i
for j in range(0,len(new_word),1):
    ed[0,j]=j
def edit_distance(basic,new_word):
    for i in range(1,len(basic),1):
        for j in range(1,len(new_word),1):
            ed[i,j]=min(1+ed.item(i-1,j), 1+ed.item(i,j-1), diff(i,j) + ed.item(i-1,j-1))
    return ed.item(len(basic),len(new_word))
def diff(i,j):
    if basic[i]==new_word[j]:
        return 0
    else:
        return 1
edit_distance(basic,new_word)
print " #",
for i in range(0,len(new_word),1):
    print new_word[i],
print ""
for i in range(0,len(basic),1):
        print basic[i],
        for j in range(0,len(new_word),1):
            print ed.item(i,j),
        print ""

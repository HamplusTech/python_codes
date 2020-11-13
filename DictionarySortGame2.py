vocab = {"band" : 0, "and" : 1, "ask" : 2, "cat" : 3}
idf = {"band" : 1.7, "and" : 0.98, "ask" : 0.99, "cat" : 1.2}
#new_vocab = {"and" : 0, "ask" : 1, "cat" : 2, "band" : 3}

new_vocab = dict()
vocab_keys = list((vocab.keys()))

final = dict()
word_count = list()
words = (vocab.keys())
##for word in words:
a = list(vocab.keys())
for i in range(len(a)):
    final[a[i]] = len(a[i])
print("final = ", final)
print("vocab = ", vocab)
print("idf = ", idf)
for word in final:
    print (word, "\t", final.get(word),"\t", word, "\t", vocab.get(word))


#alternative and short way
vocab_sort = sorted(vocab.items(), key= lambda x: x[1])
idf_sort = sorted(idf.items(), key= lambda x: len(x[0]))
idf_new = {tup[0]: idf_sort.index(tup) for tup in idf_sort}
print()
print("vocab = ", vocab)
print ("idf = ", idf)
print("new vocab = ", idf_new)


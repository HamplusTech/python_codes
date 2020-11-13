vocab = {"band" : 0, "and" : 1, "ask" : 2, "cat" : 3}
idf = {"band" : 1.7, "and" : 0.98, "ask" : 0.99, "cat" : 1.2}
#new_vocab = {"and" : 0, "ask" : 1, "cat" : 2, "band" : 3}

vocab_keys = vocab.keys()
idf_values = idf.values()
temp_list_keys = list()
temp_list_values = list()
new_vocab = dict()

##a = sorted(vocab)
##print (a)

for key in vocab_keys:
    temp_list_keys.append(key)
temp_list_keys.sort()
for value in idf_values:
    temp_list_values.append(value)
temp_list_values.sort()

print (temp_list_keys)
print (temp_list_values)

for value in range(0,4):
    new_vocab[temp_list_keys[value]] = value

print (new_vocab)

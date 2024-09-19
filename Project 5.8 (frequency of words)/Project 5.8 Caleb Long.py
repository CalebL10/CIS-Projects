file_name = input("Enter the file name: ")
file = open(file_name, "r")
word_freq = {}
for w in file.read().split():
    if w not in word_freq:
        word_freq[w] = 1
    else:
        word_freq[w] += 1
file.close()
for k in sorted(word_freq):
        print("%1s: %1d" % (k, word_freq[k]))
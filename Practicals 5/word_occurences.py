string = input("Please enter a sentence")
strings = string.split()
count_string = {}

for word in strings:
    word_count = count_string.get(word, 0)
    count_string[word] = word_count + 1
    maximum_length = max((len(word) for word in strings))
    print("{:{}} : {}".format(word, maximum_length, count_string[word]))

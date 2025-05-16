# EX_1


words = input("please enter words, separated with commas: ")
separated_words = words.split(",")
sorted_words = sorted(separated_words)
result = ",".join(sorted_words)

print(result)

# EX_2

def long_string(sentence):
    sentence = sentence.split()
    length_of_word = []
    length_of_word.append(sentence[0])
    i = 0
    for word in sentence:
        if len(sentence[i]) > len(length_of_word[0]):
            length_of_word[0] = word

        i += 1

    return length_of_word[0]


print(long_string("Forgetfulness is by all means powerless!"))



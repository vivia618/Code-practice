# Write a function that reverses all the words in a sentence that start with a particular letter.

sentence = input("Which sentence you want to reverse? : ").lower()
letter = input("Which letter you want to reverse? : ").lower()
word_in_sentence = sentence.split(" ")
new_sentence = []


def special_reverse(x, y):
    x = word_in_sentence
    y = letter
    for i in word_in_sentence:
        if i[0] == y:
            i = i[::-1]
            new_sentence.append(i)
        else:
            new_sentence.append(i)
    return ' '.join(new_sentence)


print(special_reverse(sentence, letter))

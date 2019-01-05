# Q1_A
def get_reversed_word(input_word):
    if isinstance(input_word, str):
        return input_word[::-1]

# Q1_B
def get_reversed_sentence(input_sentence):
    word_list = input_sentence.split()
    reversed_word_list = list()

    for word in word_list:
        reversed_word_list.append(get_reversed_word(word))

    reversed_sentence = ' '.join(reversed_word_list)

    return reversed_sentence

if __name__ == "__main__":
    # Q1_A
    test_str = "junyiacademy"
    ans_str = get_reversed_word(test_str)
    # Expected True.
    print(ans_str == "ymedacaiynuj")

    # Q1_B
    test_sentence = "flipped class room is important"
    ans_sentence = get_reversed_sentence(test_sentence)
    # Expected True.
    print(ans_sentence == "deppilf ssalc moor si tnatropmi")

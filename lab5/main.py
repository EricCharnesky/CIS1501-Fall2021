def scramble(word, skip):
    #sanity check
    if skip <= 1:
        return word

    scrambled_word = ""
    for start_index in range(0, skip):
        for index in range(start_index, len(word), skip):
            scrambled_word += word[index]
    return scrambled_word


for skip in range(2, 12):
    print(scramble("Beef potpie", skip))
def main():
    input_word = input("Input: ")
    print(shorten(input_word))


def shorten(word):
    for letter in word:
        if letter == 'a' or letter == 'A':
            word = word.replace(letter, '')
        if letter == 'e' or letter == 'E':
            word = word.replace(letter, '')
        if letter == 'i' or letter == 'I':
            word = word.replace(letter, '')
        if letter == 'o' or letter == 'O':
            word = word.replace(letter, '')
        if letter == 'u' or letter == 'U':
            word = word.replace(letter, '')
    return word

if __name__ == "__main__":
    main()
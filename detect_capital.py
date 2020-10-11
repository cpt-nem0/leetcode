def detectCapitalUse(word: str) -> bool:
    count = 0
    for c in word:
        if c.isupper():
            count += 1
    return count == 0 or count == len(word) or (count == 1 and word[0].isupper())

if __name__ == "__main__":
    word = input('> ')
    print(detectCapitalUse(word))
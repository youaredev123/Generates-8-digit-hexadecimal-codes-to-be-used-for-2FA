import re

def main():
    ## min length of hexword. we can control it. 
    minlen = 4
    ## The table of substitutions can be adjusted to broaden the list even further.
    subs = [
        ('l', '1'),
        ('o', '0'),
        ('s', '5'),
        ('t', '7')
    ]

    reHexWord = re.compile("[a-f0-9]*")
    ## open and read english dictionary text file
    fWords = open('words.txt', 'r')
    ## create hexwords list file
    fHexwords = open('hexspeakwords.txt', 'a')
    for w in fWords.readlines():
        w = w.strip()
        for old, new in subs:
            w = w.replace(old, new)
        if len(w) >= minlen:
            match = reHexWord.search(w)
            if match and match.group() == w:
                ## write hexwords to hexspeakwords.txt file
                fHexwords.write(w + '\n')
    fHexwords.close()
    print("########### hexspeak words list created successfully. ###########")
if __name__ == '__main__':
    main()

    
import re

def main():
    ## min length of hexword. we can control it. 
    minlen = 4
    ## The table of substitutions can be adjusted to broaden the list even further.
    subs = [
        ('L', '1'),
        ('O', '0'),
        ('S', '5'),
        ('T', '7')
    ]

    reHexWord = re.compile("[A-F0-9]*")

    ## open and read english dictionary text file
    with open('words.txt', 'r') as fWords:
        
        ## create hexwords list file
        with open('hexspeakwords.txt', 'a') as fHexwords:
            for w in fWords.readlines():
                w = w.strip().upper()
                for old, new in subs:
                    w = w.replace(old, new)
                if len(w) >= minlen:
                    match = reHexWord.search(w)
                    if match and match.group() == w:
                        ## write hexwords to hexspeakwords.txt file
                        fHexwords.write(w + '\n')
    print("########### hexspeak words list created successfully. ###########")
if __name__ == '__main__':
    main()

    
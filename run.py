from asyncio.windows_events import NULL
import secrets
def main():
    while True:

        ## Generates 8-digit hexadecimal code
        randomHex = secrets.token_hex(4)

        ## odd-looking hex code list. we can update these odd-looking list
        odd_looking_words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'ab', 'bc', 'cd', 'de', 'ef', '00', '11', '22', '33', '44', '55', '66', '77', '88', '99', '01', '12', '23', '34', '45', '56', '67', '78', '89']

        ## validate random hex code if it contains any odd-looking hex code
        if any(odd in randomHex for odd in odd_looking_words):
            continue

        ## open and read hexwords
        with open('hexspeakwords.txt', 'r') as fHexwords:
            ## validate random hex code if it contains any hexword(hexspeak words)
            if any(hexword in randomHex for hexword in fHexwords.readlines()):
                continue
        with open('oldHexs.txt', 'a+') as foldHexs:
            ## validate random hex code's repetition
            if any(randomHex in oldHex for oldHex in foldHexs.readlines()):
                continue
            foldHexs.write(randomHex + '\n')
        print('########### This is 8-digit hexadecimal code: 0x' + randomHex + ' ###########')
        break

if __name__ == '__main__':
    main()
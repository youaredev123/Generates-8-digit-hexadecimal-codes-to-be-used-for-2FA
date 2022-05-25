from asyncio.windows_events import NULL
import secrets
def main():
    while True:
        ## Generates 8-digit hexadecimal code
        randomHex = secrets.token_hex(4)
        ## odd-looking hex code list
        odd_looking_words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', '01', '12', '23', '34', '45', '56', '67', '78', '89', '90']
        ## open and read hexwords
        fHexwords = open('hexspeakwords.txt', 'r')
        ## validate random hex code if it contains any odd-looking hex code
        for odd in odd_looking_words:
            if odd in randomHex:
                randomHex = NULL
                break
        if randomHex == NULL:
            continue
        ## validate random hex code if it contains any hexword(hexspeak words)
        for hexword in fHexwords.readlines():
            if hexword.strip() in randomHex:
                randomHex = NULL
                break
        if randomHex == NULL:
            continue
        print('########### This is 8-digit hexadecimal code: 0x' + randomHex + ' ###########')
        break

if __name__ == '__main__':
    main()
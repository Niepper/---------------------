from cyphers.globals import DICT, REV_DICT


def vigenere(word: str, key: str, decode=False):
    t = 0
    word = word.lower()
    key = key.lower()

    while len(word) > len(key):
        key += key[t]
        t += 1

    temp = []
    for index, i in enumerate(word):
        if decode:
            if i == " ":
                temp.append(" ")
            elif DICT[i] - DICT[key[index]] < 1:
                temp.append((DICT[i] - DICT[key[index]] + 32))
            else:
                temp.append(DICT[i] - DICT[key[index]])
        else:
            if i == " ":
                temp.append(" ")
            elif (DICT[i] + DICT[key[index]]) > 32:
                temp.append(((DICT[i] + DICT[key[index]]) % 33) + 1)
            else:
                temp.append(DICT[i] + DICT[key[index]])

    encoded = ""
    for i in temp:
        if i == " ":
            encoded += " "
        else:
            encoded += REV_DICT[i - 1]

    print(encoded)


vigenere("cęsśohdmsńą", "podatki", True)

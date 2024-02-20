from cyphers.globals import DICT, REV_DICT


def cesar(word:str, shift: int = 0, decode=False):
    temp = []
    for i in word.lower():
        if decode:
            if i == " ":
                temp.append(" ")
            elif DICT[i] - shift < 1:
                temp.append((DICT[i] - shift + 32))
            else:
                temp.append(DICT[i] - shift)
        else:
            if i == " ":
                temp.append(" ")
            elif DICT[i] + shift > 32:
                temp.append(((DICT[i] + shift) % 33) + 1)
            else:
                temp.append(DICT[i] + shift)

    encoded = ""
    for i in temp:
        if i == " ":
            encoded+=" "
        else:
            encoded += REV_DICT[i - 1]

    return encoded

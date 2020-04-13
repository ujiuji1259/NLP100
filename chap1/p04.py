import re
def create_elementmap(text, pos_list):
    words = [re.sub(r"[,\.]", "", t) for t in text.split()]
    res = {}
    for i, w in enumerate(words):
        if i + 1 in pos_list:
            res[w[0]] = i+1
        else:
            res[w[:2]] = i+1

    return res



if __name__ == "__main__":
    t = """Hi He Lied Because Boron Could Not Oxidize Fluorine.\
             New Nations Might Also Sign Peace Security Clause.\
             Arthur King Can."""

    l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    print(create_elementmap(t, l))

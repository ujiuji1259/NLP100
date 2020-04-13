import re
def create_ngram(text, n, fmt):
    if fmt == "char":
        words = [list(t) for t in re.sub(r"[,\.]", "", text).split()]
    else:
        words = [[t for t in re.sub(r"[,\.]", "", text).split()]]
    res = [w[i:i+n] for w in words for i in range(len(w)-n+1)]

    return res

if __name__ == "__main__":
    t = "I am an NLPer"
    print(create_ngram(t, 2, "word"))
    print(create_ngram(t, 3, "char"))

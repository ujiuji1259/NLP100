import random

def shuffle_words(text):
    words = text.split()
    res = []
    for w in words:
        if len(w) <= 4:
            res.append(w)
        else:
            shuffled_str = w[0]
            mid_str = w[1:-1]
            shuffled_str += "".join(random.sample(mid_str, len(mid_str)))
            shuffled_str += w[-1]
            res.append(shuffled_str)

    return " ".join(res)

if __name__ == "__main__":
    t = """I couldn't believe that I could actually understand what I was reading : \
            the phenomenal power of the human mind ."""
    print(shuffle_words(t))




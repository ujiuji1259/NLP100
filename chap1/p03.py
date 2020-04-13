import re
def count_word_lengths(text):
    words = [re.sub(r"[,\.]", "", t) for t in text.split()]
    return [len(w) for w in words]

if __name__ == "__main__":
    t = """Now I need a drink, alcoholic of course, after the heavy \
            lectures involving quantum mechanics."""
    print(count_word_lengths(t))

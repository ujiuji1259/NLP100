def mix_texts(text1, text2):
    return "".join([t1 + t2 for t1, t2 in zip(text1, text2)])

if __name__ == "__main__":
    print(mix_texts("パトカー", "タクシー"))

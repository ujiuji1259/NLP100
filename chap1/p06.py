from p05 import create_ngram

if __name__ == "__main__":
    t1 = "paraparaparadise"
    t2 = "paragraph"
    bi1 = {"".join(t) for t in create_ngram(t1, 2, "char")}
    bi2 = {"".join(t) for t in create_ngram(t2, 2, "char")}

    print("和集合：", bi1 | bi2)
    print("積集合：", bi1 & bi2)
    print("差集合：", bi1 - bi2)
    print("'se' in X: ", 'se' in bi1)
    print("'se' in Y: ", 'se' in bi2)

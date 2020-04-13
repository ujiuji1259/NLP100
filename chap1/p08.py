def cipher(text):
    res = [chr(219 - ord(c)) if "a" <= c <= "z" else c for c in text]
    return "".join(res)

if __name__ == "__main__":
    print(cipher("I Am An Engineer"))
    print(cipher(cipher("I Am An Engineer")))

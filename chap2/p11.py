# python p11.py popular-names.txt
# tr '\t' '' < popular-names.txt
import sys

def replace_tab(file_name):
    res = []
    with open(file_name, "r") as f:
        for line in f:
            res.append(line.replace("\t", " "))
    return "".join(res)


if __name__ == "__main__":
    fn = sys.argv[1]
    print(replace_tab(fn))

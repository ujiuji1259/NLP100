# python p13.py col1.txt col2.txt
# paste col1.txt col2.txt
import sys

def merge_two_file(f1, f2):
    col1, col2 = [], []
    with open(f1, 'r') as f:
        col1 = [line for line in f.read().split("\n") if line != '']
    with open(f2, 'r') as f:
        col2 = [line for line in f.read().split("\n") if line != '']

    res = ["\t".join([c1, c2]) for c1, c2 in zip(col1, col2)]
    return res

if __name__ == "__main__":
    f1, f2 = sys.argv[1], sys.argv[2]
    output = merge_two_file(f1, f2)
    with open("res_p13.txt", "w") as f:
        f.write("\n".join(output))

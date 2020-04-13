# python p12.py popular-names.txt
# cut -f 1 popular-names.txt
# cut -f 2 popular-names.txt
import sys

def save_eachcol(file_name):
    col1, col2 = [], []
    with open(file_name, "r") as f:
        for line in f:
            if line != '':
                line = line.replace("\n", "").split("\t")
                col1.append(line[0])
                col2.append(line[1])

    with open("col1.txt", "w") as f:
        f.write("\n".join(col1))
    with open("col2.txt", "w") as f:
        f.write("\n".join(col2))


if __name__ == "__main__":
    fn = sys.argv[1]
    print(save_eachcol(fn))

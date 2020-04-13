# python p14.py popular-names.txt 10
# head -n 10 popular-names.txt
import sys

def head(fn, n):
    output = []
    with open(fn, 'r') as f:
        for i, line in enumerate(f):
            if i == n:
                break
            output.append(line.replace('\n', ''))

    return output

if __name__ == "__main__":
    fn, n = sys.argv[1], int(sys.argv[2])
    print("\n".join(head(fn, n)))

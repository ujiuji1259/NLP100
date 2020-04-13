# python p15.py popular-names.txt 10
# tail -n 10 popular-names.txt
import sys

def tail(fn, n):
    with open(fn, 'r') as f:
        res = [line for line in f.read().split('\n') if line != ''][-n:]

    return res


if __name__ == "__main__":
    fn, n = sys.argv[1], int(sys.argv[2])
    print("\n".join(tail(fn, n)))

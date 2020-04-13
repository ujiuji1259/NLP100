# python p10.py popular-names.txt
# wc -l popular-names.txt
import sys

def count_row(file_name):
    with open(file_name, "r") as f:
        return len(f.readlines())

if __name__ == "__main__":
    fn = sys.argv[1]
    print(count_row(fn))

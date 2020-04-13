if __name__ == '__main__':
    with open('wiki_england.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if line != '']

    res = [line for line in lines if line[:10] == '[[Category']
    print('\n'.join(res))

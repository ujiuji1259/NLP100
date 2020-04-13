import json

if __name__ == "__main__":
    with open("jawiki-country.json", 'r') as f:
        for line in f:
            article = json.loads(line)
            if article['title'] == 'イギリス':
                print(article['text'])

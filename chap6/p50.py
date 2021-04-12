import csv
import random

def load_dataset(path, publishers=["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]):
    datasets = []
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row[3] in publishers:
                datasets.append(row)

    random.shuffle(datasets)
    fold_size = len(datasets) // 10
    train_data = datasets[:fold_size*8]
    validation_data = datasets[fold_size*8:fold_size*9]
    test_data = datasets[fold_size*9:]

    return train_data, validation_data, test_data

def save_dataset(data, path):
    with open(path, 'w') as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(data)

train_data, validation_data, test_data = load_dataset("NewsAggregatorDataset/newsCorpora.csv")
save_dataset(train_data, "NewsAggregatorDataset/train.txt")
save_dataset(validation_data, "NewsAggregatorDataset/valid.txt")
save_dataset(test_data, "NewsAggregatorDataset/test.txt")
from sklearn.feature_extraction.text import CountVectorizer
import csv
import numpy as np

def load_dataset(path):
    datasets = []
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            datasets.append(row)

    return datasets

def preprocess(data):
    x = [d[1] for d in data]
    y = [d[4] for d in data]

    x = [d.lower() for d in x]
    return x, y

train_data = load_dataset("NewsAggregatorDataset/train.txt")
valid_data = load_dataset("NewsAggregatorDataset/valid.txt")
test_data = load_dataset("NewsAggregatorDataset/test.txt")
train_x, train_y = preprocess(train_data)
valid_x, valid_y = preprocess(valid_data)
test_x, test_y = preprocess(test_data)

model = CountVectorizer()
train_x = model.fit_transform(train_x)
valid_x = model.transform(valid_x)
test_x = model.transform(test_x)
print(train_x)

np.savetxt("NewsAggregatorDataset/train.feature.txt", train_x.toarray())
np.savetxt("NewsAggregatorDataset/valid.feature.txt", valid_x.toarray())
np.savetxt("NewsAggregatorDataset/test.feature.txt", test_x.toarray())
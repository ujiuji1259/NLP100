from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import csv
import numpy as np
import matplotlib.pyplot as plt

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


Cs = [1e-1, 1, 1e1, 2e1, 3e1, 5e1]
train_acc = []
valid_acc = []
test_acc = []
for c in Cs:
    clf = LogisticRegression(random_state=0, C=c).fit(train_x, train_y)
    preds = clf.predict(train_x)
    train_acc.append(accuracy_score(train_y, preds))

    preds = clf.predict(valid_x)
    valid_acc.append(accuracy_score(valid_y, preds))

    preds = clf.predict(test_x)
    test_acc.append(accuracy_score(test_y, preds))

plt.plot(Cs, train_acc)
plt.plot(Cs, valid_acc)
plt.plot(Cs, test_acc)
plt.show()

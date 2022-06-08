from sklearn import preprocessing, svm, model_selection

# 이거 공부. 수정본.

def read_leaf(file):
    x, labels = [], []
    with open(file, 'r', encoding='utf-8') as f:
        f.readline()

        for line in f:
            items = line.strip().split(',')

            x.append([float(v) for v in items[2:]])
            labels.append(items[1])

    f.close()
    return x, labels


x, labels = read_leaf('leaf-classification/train.csv')

bin = preprocessing.LabelEncoder()
y = bin.fit_transform(labels)

data = model_selection.train_test_split(x, y, train_size=0.8)
x_train, x_test, y_train, y_test = data

clf = svm.SVC()
clf.fit(X=x_train, y=y_train)
print('acc :', clf.score(x_test, y_test))

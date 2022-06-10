from sklearn import preprocessing, svm, model_selection
import numpy as np

x = [[1, -1, -3],
     [2, 0, 1],
     [0, 1, 7]]


# 퀴즈
# x에 대해 표준화 스케일링 적용하기
def scl(x):
    scaler = preprocessing.StandardScaler()
    scaler.fit(x)

    return scaler.transform(x)


# # x에 대해 표준화 스케일링 직접 적용하기
# y = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
# print(x)


# 퀴즈
# x에 대해 정규화 스케일링 적용
def mm(x):
    mms = preprocessing.MinMaxScaler()
    mms.fit(x)

    return mms.transform(x)


# # 퀴즈
# # x에 대해 정규화 직접 적용하기
# print((x - np.min(x, axis=0)) / (np.max(x, axis=0) - np.min(x, axis=0)))


# 퀴즈
# 스케일링 한것과 안한것 비교 + 표준화 정규화
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


x, labels = read_leaf('data/train.csv')

bin = preprocessing.LabelEncoder()
y = bin.fit_transform(labels)

x_compare = [x, scl(x), mm(x)]
for num, i in enumerate(x_compare):
    data = model_selection.train_test_split(i, y, train_size=0.8)
    x_train, x_test, y_train, y_test = data

    clf = svm.SVC()
    clf.fit(X=x_train, y=y_train)
    print('acc {}:'.format(num), clf.score(x_test, y_test))

# 스케일링은 하되, 어떤게 좋은지 그때그때 다르므로 둘 다 해봐야한다.
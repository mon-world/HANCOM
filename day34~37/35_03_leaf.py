# 35_03_leaf.py
import numpy as np
from sklearn import preprocessing, model_selection, svm

# 퀴즈
# leaf-classification에 train.csv 읽고 8 : 2로 학습 정확도 구하기(svm)

def read_leaf(file):
    x = []
    with open(file, 'r', encoding='utf-8') as f:
        f.readline()        # 1: 삭제 가능
        for line in f:
            x.append(line.strip().split(','))

    f.close()
    return np.array(x)          # 여기 쓰는게 좋다

# 바로 x,y 구하는게 좋다.

rows = read_leaf('data/train.csv')

# leaf = rows[1:,2:]  # (990, 192)
leaf = rows[:, :2]
leaf_name = rows[:, 1]


bin1 = preprocessing.LabelEncoder()
bin1.fit(leaf_name)
leaf_name = bin1.transform(leaf_name)

clf = svm.SVC()

data = model_selection.train_test_split(leaf, leaf_name, train_size=0.8)
x_train, x_test, y_train, y_test = data

clf.fit(X=x_train, y=y_train)
score = clf.score(x_test, y_test)
print(score)        # 0.8383838383838383

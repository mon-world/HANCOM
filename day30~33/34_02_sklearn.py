# 34_02_sklearn.py
import pandas as pd
import sklearn.utils
from sklearn import datasets, svm, neighbors
import matplotlib.pyplot as plt
import numpy as np

# 퀴즈
# 사이킷런에 있는 iris에 8대2로 나눠서 학습 테스트

digits = datasets.load_iris()
clf = svm.SVC()

digits.data, digits.target = sklearn.utils.shuffle(digits.data, digits.target)

test = int(len(digits.data)*0.7)
print(len(digits.data))
clf.fit(X=digits.data[:test], y=digits.target[:test])
p = clf.predict(X=digits.data[test:])

print('acc : ', np.sum(p == digits.target[test:]) / len(p))

print(digits.target)
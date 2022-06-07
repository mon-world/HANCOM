# 35_01_sklearn.py
from sklearn import datasets, svm, neighbors, utils, model_selection
import matplotlib.pyplot as plt
import numpy as np

# 하이퍼파라미터 : 모델에서 직접 결정해야 하는 값

# 나에게 해야하는 질문을 이웃에게 물어봐서 특성을 아는 것. 최근접 이웃
nav_1 = neighbors.KNeighborsClassifier(n_neighbors=2)

# 퀴즈
# KN 클래스에 대해서 이웃 숫자를 2개에서 10개까지 바꾸면서 iris 데이터에 정확도를 구하고
# 해당 정확도를 그래프로 그리기

iris = datasets.load_iris()

# digits.data, digits.target = utils.shuffle(digits.data, digits.target)
# train = int(len(digits.data)*0.8)
#
# nav.fit(X=digits.data[:train], y=digits.target[:train])

# 위를 대체
data = model_selection.train_test_split(iris.data, iris.target, train_size=0.8)

x_train, x_test, y_train, y_test = data

scores = []
for i in range(2, 11):
    nav = neighbors.KNeighborsClassifier(n_neighbors=i)
    nav.fit(x_train, y_train)
    score = nav.score(x_test, y_test)

    scores.append(score)

plt.bar(range(len(scores)), scores)
plt.xticks(range(len(scores)), range(2, 11))
plt.show()
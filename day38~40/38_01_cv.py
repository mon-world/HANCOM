# 38_01_cv.py
import numpy as np
from sklearn import datasets, linear_model, model_selection
import matplotlib.pyplot as plt


# 퀴즈
# make_blobs 함수가 반환한 데이터를 시각화하세요
def show_blobs():
    x, y = datasets.make_blobs(random_state=23, centers=7, n_samples=100, n_features=5)
    print(x.shape, y.shape)     # 1. 데이터를 보고 판단 -> x와 y를 직접 정하기
    print(x[:3])
    print(y[:10])               
    print(min(y), max(y))      

    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.show()


# 퀴즈
# linear_model에 속한 LogisticRegression 모델을 사용해서
# blob 데이터에 대해 80%로 학습하고 20%에 대해 정확도를 구하세요
def cv_1():
    x, y = datasets.make_blobs(random_state=23, centers=31, n_samples=1000, n_features=4)

    data = model_selection.train_test_split(x, y, train_size=0.8)
    x_train, x_test, y_train, y_test = data

    # 1번(모델 생성) 2번(학습) 3번(예측/변환)
    # {'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'}
    reg = linear_model.LogisticRegression(solver='liblinear')
    reg.fit(x_train, y_train)
    print('acc :', reg.score(x_test, y_test))


# 퀴즈
# 로지스틱 리그레션 모델을 동일 데이터에 10회 검증하세요
# 문제점 : 같은 데이터가 쓰이지 않는다. 따라서 model_selection.train_test_split을 사용하기 힘들다.(랜덤이므로)
def cv_2():
    x, y = datasets.make_blobs(random_state=23, centers=31, n_samples=1000, n_features=4)

    total = 0
    for i in range(10):
        data = model_selection.train_test_split(x, y, train_size=0.8)
        x_train, x_test, y_train, y_test = data

        reg = linear_model.LogisticRegression(solver='liblinear')
        reg.fit(x_train, y_train)

        acc = reg.score(x_test, y_test)
        total += acc
        print('{} : {}'.format(i, acc))

    print('-' * 30)
    print('mean :', total / 10)




# show_blobs()

# cv_1()
# cv_2()
cv_3()

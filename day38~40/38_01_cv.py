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
    reg = linear_model.LogisticRegression(solver='liblinear')
    reg.fit(x_train, y_train)
    print('acc :', reg.score(x_test, y_test))


# 퀴즈
# 로지스틱 리그레션 모델을 동일 데이터에 10회 검증하세요
# 문제점 : 같은 데이터가 쓰이지 않는다. 따라서 model_selection.train_test_split을 사용하기 힘들다.(랜덤이므로)
# 10번 돌리면 모든 데이터가 사용되는게 같아야 함.
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


# 데이터 100개를 선택해서 test 데이터로 만들고, 나머지 데이터를 학습데이터로 사용한다.
def cv_3():
    x, y = datasets.make_blobs(random_state=23, centers=31, n_samples=1000, n_features=4)

    total = 0
    for i in range(10):
        # 데이터 100개씩 분할
        s = i * 100
        e = s + 100
        # print(s, e)

        x_test = x[s:e]
        y_test = y[s:e]

        # test 데이터의 범위가 200에서 300일 때
        # train 데이터의 범위는 (0 ~ 200) + (300 ~ 1000)
        x_train = np.vstack([x[:s], x[e:]])
        y_train = np.concatenate([y[:s], y[e:]])

        # print(x_train.shape, x_test.shape)          # (900, 4) (100, 4)
        # print(y_train.shape, y_test.shape)          # (900,) (100,)

        reg = linear_model.LogisticRegression(solver='liblinear')
        reg.fit(x_train, y_train)

        acc = reg.score(x_test, y_test)
        total += acc
        print('{} : {}'.format(i, acc))

    print('-' * 30)
    print('mean :', total / 10)             # 평균 정확도


# 퀴즈
# cv_3코드를 StratifiedShuffleSplit 클래스를 사용하는 코드로 수정
# 35_05_leaf에서 사용했었음
def cv_4():
    x, y = datasets.make_blobs(random_state=23, centers=31, n_samples=1000, n_features=4)

    data = model_selection.StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=23)

    total = 0
    for i, (train_index, test_index) in enumerate(data.split(x, y)):
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]

        reg = linear_model.LogisticRegression(solver='liblinear')
        reg.fit(x_train, y_train)

        acc = reg.score(x_test, y_test)
        total += acc
        print('{} : {}'.format(i, acc))

    print('-' * 30)
    print('mean :', total / 10)


# 지금 코드를 한 줄로 줄이기
def cv_5():
    x, y = datasets.make_blobs(random_state=23, centers=31, n_samples=1000, n_features=4)

    reg = linear_model.LogisticRegression(solver='liblinear')       # 바깥에 두는게 좋다

    # 반복 사용 안해도 이렇게 해줌
    scores = model_selection.cross_val_score(reg, x, y)
    print(scores)

    scores = model_selection.cross_val_score(reg, x, y, cv=10)
    print(scores)


# show_blobs()

# cv_1()
# cv_2()
# cv_3()
# cv_4()
cv_5()

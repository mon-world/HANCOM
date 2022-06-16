# 39_01_grid_search.py
import numpy as np
import pandas as pd
from sklearn import datasets, model_selection, svm


def svm_basic():

    # iris 데이터 셋을 x,y로 바로 분리
    x, y = datasets.load_iris(return_X_y=True)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, train_size=0.8)

    clf = svm.SVC()
    clf.fit(x_train, y_train)
    print('acc :', clf.score(x_test, y_test))


# hp: hyper parameter
# 퀴즈
# SVC 클래스에 전달하는 C와 gamma 옵션에 대해 최적의 값을 찾으세요
# C와 gamma의 값은 (0.001, 0.01, 0.1, 1, 10, 100) 중에서 선택합니다
def search_hp_1(x_train, x_test, y_train, y_test):
    best_score, best_param = 0.0, {}

    params = [0.001, 0.01, 0.1, 1, 10, 100]
    for C in params:
        for gamma in params:
            clf = svm.SVC(C=C, gamma=gamma)
            clf.fit(x_train, y_train)
            score = clf.score(x_test, y_test)

            if best_score < score:
                best_score = score
                best_param['C'] = C
                best_param['gamma'] = gamma


    print('best score :', best_score)       
    print('best param :', best_param)       

    clf = svm.SVC(C=best_param['C'], gamma=best_param['gamma'])
    clf.fit(x_train, y_train)
    print('acc :', clf.score(x_test, y_test))


# 퀴즈
# 기존 데이터를 분할해서 validation 데이터를 만들어서 사용하고
# 최종 결과는 test 데이터에 대해 검사하세요
def search_hp_2(x_total, x_test, y_total, y_test):
    # train을 다시 train과 validation으로 나눈다.
    x_train, x_valid, y_train, y_valid = model_selection.train_test_split(x_total, y_total, train_size=0.7)

    best_score, best_param = 0.0, {}

    params = [0.001, 0.01, 0.1, 1, 10, 100]
    for C in params:
        for gamma in params:
            clf = svm.SVC(C=C, gamma=gamma)
            clf.fit(x_train, y_train)
            score = clf.score(x_valid, y_valid)

            if best_score < score:
                best_score = score
                best_param['C'] = C
                best_param['gamma'] = gamma

    print('best score :', best_score)
    print('best param :', best_param)

    clf = svm.SVC(C=best_param['C'], gamma=best_param['gamma'])
    clf.fit(x_total, y_total)
    print('acc :', clf.score(x_test, y_test))


# svm_basic()

x, y = datasets.load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, train_size=0.7)

# search_hp_1(x_train, x_test, y_train, y_test)
search_hp_2(x_train, x_test, y_train, y_test)


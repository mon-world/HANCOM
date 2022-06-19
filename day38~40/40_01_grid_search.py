# 40_01_grid_search.py
import numpy as np
import pandas as pd
from sklearn import datasets, model_selection, svm


# 퀴즈
# 단순 모델을 적용하는 코드를 교차검증(cross validation) 모델 적용하는 코드로 수정하세요
def search_hp_3(x_train, x_test, y_train, y_test):
    best_score, best_param = 0.0, {}
    list_a = [0.001, 0.01, 0.1, 1, 10, 100]
    for C in list_a:
        for gamma in list_a:
            clf = svm.SVC(C=C, gamma=gamma)
            scores = model_selection.cross_val_score(clf, x_train, y_train, cv=5)
            avg_score = np.mean(scores)

            if best_score < avg_score:
                best_score = avg_score
                best_param['C'] = C
                best_param['gamma'] = gamma

    print('best score :', best_score)
    print('best param :', best_param)

    # clf = svm.SVC(C=best_param['C'], gamma=best_param['gamma'])
    clf = svm.SVC(**best_param)
    clf.fit(x_train, y_train)
    print('acc :', clf.score(x_test, y_test))
# 33_03_sklearn.py
import pandas as pd
from sklearn import datasets, svm, neighbors
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


def sklearn_1():
    iris = datasets.load_iris()

    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    print(df)

    # scatter_matrix(df)
    # scatter_matrix(df, c=iris.target)
    # scatter_matrix(df, c=iris.target, hist_kwds={'bins': 20})
    scatter_matrix(df, c=iris.target, hist_kwds={'bins': 20}, cmap='jet')
    plt.show()


# 퀴즈
# load_digits 함수가 반환한 데이터에 대해 살펴보세요
def sklearn_2():
    digits = datasets.load_digits()
    print(digits.keys())
    # dict_keys(['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR'])

    print(digits.DESCR, end='\n\n')

    print(digits.feature_names)             # ['pixel_0_0', 'pixel_0_1', ... 'pixel_7_7']
    print(digits.target_names, end='\n\n')  # [0 1 2 3 4 5 6 7 8 9]

    print(digits.images.shape)              # (1797, 8, 8)
    print(digits.data.shape)                # (1797, 64)
    print(digits.target.shape, end='\n\n')  # (1797,)

    print(digits.target[0])
    print(digits.images[0], end='\n\n')


def sklearn_3():
    digits = datasets.load_digits()

    clf = svm.SVC()
    print(clf)

    clf.fit(X=digits.data, y=digits.target)
    p = clf.predict(X=digits.data)

    print(p)


# sklearn_1()
# sklearn_2()
sklearn_3()
























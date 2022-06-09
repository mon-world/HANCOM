# 36_01_leaf.py
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedShuffleSplit

from sklearn.metrics import accuracy_score, log_loss
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis

# 모르는 것 과감히 삭제하
def encode(df_train, df_test):
    le = LabelEncoder()
    y_train = le.fit_transform(df_train.species)

    x_train = df_train.drop(['species', 'id'], axis=1).values
    x_test = df_test.drop(['id'], axis=1).values

    return x_train, y_train, x_test, df_test.id.values, le.classes_


df_train = pd.read_csv('leaf-classification/train.csv')
df_test = pd.read_csv('leaf-classification/test.csv')

x_total, y_total, x_test, test_ids, classes = encode(df_train, df_test)
print(x_total.shape, x_test.shape)      # (990, 192) (594, 192)
print(y_total.shape)                    # (990,)

sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=23)

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="rbf", C=0.025, probability=True),
    NuSVC(probability=True),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    AdaBoostClassifier(),
    # GradientBoostingClassifier(),
    GaussianNB(),
    LinearDiscriminantAnalysis(),
    QuadraticDiscriminantAnalysis(),
]

accuracies, losses = {}, {}
for clf in classifiers:
    accuracies[clf.__class__.__name__] = 0.0
    losses[clf.__class__.__name__] = 0.0

for train_index, test_index in sss.split(x_total, y_total):
    x_train, x_valid = x_total[train_index], x_total[test_index]
    y_train, y_valid = y_total[train_index], y_total[test_index]

    # print(train_index.shape)
    # print(test_index.shape)
    # total = np.concatenate([train_index, test_index])
    # print(total.shape)
    # print(len(set(total)))
    # print(sorted(total))

    for clf in classifiers:
        clf.fit(x_train, y_train)

        # print(clf.__class__.__name__)

        train_predictions = clf.predict(x_valid)
        acc = accuracy_score(y_valid, train_predictions)
        accuracies[clf.__class__.__name__] += acc
        # print("acc : {:.4%}".format(acc))

        train_predictions = clf.predict_proba(x_valid)
        ll = log_loss(y_valid, train_predictions)
        losses[clf.__class__.__name__] += ll
        # print("loss: {}".format(ll))
        # print()

    print("=" * 50)

for clf in classifiers:
    accuracies[clf.__class__.__name__] /= 10
    losses[clf.__class__.__name__] /= 10

for clf in classifiers:
    name = clf.__class__.__name__
    print('{:>30} : {:.3f} {:.3f}'.format(name, accuracies[name], losses[name]))

favorite_clf = LinearDiscriminantAnalysis()
favorite_clf.fit(x_total, y_total)
test_predictions = favorite_clf.predict_proba(x_test)       # 192개 피처 -> 99개 정답
# print(test_predictions[0])

# submission = pd.DataFrame(test_predictions, columns=classes)
# submission.insert(0, 'id', test_ids)
# submission.reset_index()
#
# submission.to_csv('leaf-classification/submission.csv', index=False)

f = open('leaf-classification/submission.csv', 'w', encoding='utf-8')

f.write('id,' + ','.join(classes) + '\n')

for leaf_id, values in zip(test_ids, test_predictions):
    f.write('{},{}\n'.format(leaf_id, ','.join([str(v) for v in values])))

f.close()




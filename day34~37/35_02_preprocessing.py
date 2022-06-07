from sklearn import preprocessing, impute
import numpy as np


x = [[1, 2],
     [np.nan, 4],
     [7, 9]]

imp = impute.SimpleImputer()          # 결측치를 적절한 값으로 채우는 알고리즘
imp.fit(x)
print(imp.transform(x))

# 퀴즈
# 아래 데이터를 온전한 데이터로 바꾸기 imp.transform 사용
# z = [np.nan, np.nan]                  # 2차원이 아니라 에러
# z = [[np.nan], [np.nan]]              # 1피쳐라 에러
z = [[np.nan, np.nan]]                  # [[4. 5.]]

print(imp.transform(z))
from sklearn.feature_selection import chi2, SelectFdr, SelectFpr, SelectKBest, SelectFwe,mutual_info_classif
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import accuracy_score

x,y = load_diabetes(return_X_y=True)

x_train, y_train, x_test, y_test = train_test_split(x,y)

model = DecisionTreeRegressor()

train = model.fit(x_train,x_test)


test = model.predict(y_train)


print(test)
print(y_test)

accuracy = accuracy_score(test,y_test)

print(F"Accuracy of model is {accuracy}")
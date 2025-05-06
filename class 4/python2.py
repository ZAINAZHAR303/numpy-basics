from sklearn.feature_selection import SelectKBest, chi2, SelectPercentile, SelectFdr, SelectFpr, SelectFromModel, SelectFwe, mutual_info_classif
from sklearn.datasets import load_iris, load_breast_cancer  
from sklearn.feature_selection import GenericUnivariateSelect

X,y = load_breast_cancer(return_X_y=True)
inputs = load_breast_cancer()
a,b = inputs.data,inputs.target
fname = inputs.feature_names
print(fname)   
# print(inputs.shape)

bestk = SelectKBest(mutual_info_classif, k=5).fit(a,b)
# print(bestk.get_support())
k_trans= bestk.transform(a)
sleected = fname[bestk.get_support()]
print("feture after mutual classif",fname[bestk.get_support()])

# // we have to calculate the false positive rate

gen = GenericUnivariateSelect(chi2, mode="percentile", param=50).fit_transform(a,b)
print(gen.shape)
print("feture after chi2 in generic",fname[gen.get_support()])
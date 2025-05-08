from sklearn.feature_selection import SelectKBest,chi2,SelectPercentile,SelectFdr,SelectFpr,SelectFromModel,SelectFwe, mutual_info_classif

from sklearn.datasets import load_iris, load_breast_cancer


# x,y = load_breast_cancer(return_X_y=True)
inputs = load_breast_cancer()
x,y = inputs.data,inputs.target



result = inputs.feature_names

print(result)
# k_chi=SelectKBest(chi2,k=5).fit_transform(x,y)
# print(k_chi.shape)

# per_chi = SelectPercentile(chi2,percentile=5).fit_transform(x,y)
# print(per_chi.shape)

# per_mu = SelectPercentile(mutual_info_classif,percentile=5).fit(x,y)
# trans_mu = per_mu.transform(x)
# print(result[per_mu.get_support()])


# fdr_chi = SelectFdr(chi2,alpha=0.01).fit_transform(x,y)
# print(fdr_chi.shape)





# selector = SelectFpr(mutual_info_classif, alpha=0.01)  
# f_chi = selector.fit_transform(x, y)
# print("Actual Features")
# print("original shape:", x.shape)
# print(f_chi.shape)
# print("Selected Featur es of SelectFpr")
# print(result[selector.get_support()])  


# fdr_mi = SelectFdr(chi2, alpha=0.05)
# X_mi_selected = fdr_mi.fit_transform(x, y)
# print(X_mi_selected.shape)
# print("Selected Features of SelectFdr")
# print(result[fdr_mi.get_support()])  # Use Selector instead of selector
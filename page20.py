from sklearn.datasets import load_breast_cancer
import pandas as pd

breast_cancer = load_breast_cancer()
breast_cancer_df = pd.DataFrame(data=breast_cancer.data,
                               columns=breast_cancer.feature_names)
breast_cancer_df['target'] = breast_cancer.target
breast_cancer_df = breast_cancer_df.dropna()
print(breast_cancer_df.head())

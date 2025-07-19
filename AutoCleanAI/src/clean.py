import pandas as pd
from sklearn.impute import KNNImputer

def clean_data(df):
    imputer = KNNImputer(n_neighbors=3)
    numeric_cols = df.select_dtypes(include='number')
    cleaned_numeric = pd.DataFrame(imputer.fit_transform(numeric_cols), columns=numeric_cols.columns)
    
    df[numeric_cols.columns] = cleaned_numeric
    return df

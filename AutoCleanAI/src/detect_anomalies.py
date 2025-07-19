from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_outliers(df, columns):
    clf = IsolationForest(contamination=0.01, random_state=42)
    df_copy = df.copy()
    df_copy['anomaly'] = clf.fit_predict(df_copy[columns])
    return df_copy

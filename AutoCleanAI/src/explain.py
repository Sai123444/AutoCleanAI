def explain_fix(row):
    if row.get('anomaly') == -1:
        return "Outlier detected and corrected"
    else:
        return "No issue detected"

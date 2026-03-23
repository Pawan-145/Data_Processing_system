import pandas as pd

def validate_data(df):
    errors = []

    # Check for missing values (including -1)
    missing_count = df.replace([-1, -1.0, "", " "], pd.NA).isna().sum().sum()
    
    if missing_count > 0:
        errors.append(f"Missing values found: {missing_count}")

    # Check duplicates
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        errors.append(f"Duplicate rows found: {duplicate_count}")

    # Check negative values (important for agri data)
    negative_values = (df.select_dtypes(include=['float64', 'int64']) < 0).sum().sum()
    if negative_values > 0:
        errors.append(f"Negative values found: {negative_values}")

    return errors
import pandas as pd

def clean_data(df):
    df.replace([-1, -1.0, "", " "], pd.NA, inplace=True)
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna("N/A")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


    return df
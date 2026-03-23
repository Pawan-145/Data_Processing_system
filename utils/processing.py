import pandas as pd
from utils.data_cleaning import clean_data
from utils.validation import validate_data

def process_file(filepath):
    df = pd.read_csv(filepath)

    original_shape = df.shape

    errors = validate_data(df)

    df = clean_data(df)

    processed_shape = df.shape
    print("Errors detected:", errors)
    summary = {
    "original_rows": original_shape[0],
    "processed_rows": processed_shape[0],
    "columns": list(df.columns),
    "errors": errors,
    "status": "Cleaned Successfully" if not errors else "Issues Detected"
}

    return df, summary

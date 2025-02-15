import pandas as pd
from typing import Tuple, List
import datacompy

def load_file(uploaded_file) -> pd.DataFrame:
    """Load CSV or Excel file into a pandas DataFrame."""
    if uploaded_file.name.endswith('.csv'):
        return pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(('.xls', '.xlsx')):
        return pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload CSV or Excel files only.")

def create_synthetic_key(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Create a synthetic key by concatenating multiple columns."""
    df = df.copy()
    df['synthetic_key'] = df[columns].astype(str).agg('_'.join, axis=1)
    return df

def compare_dataframes(df1: pd.DataFrame, df2: pd.DataFrame, 
                      compare_cols: List[str], join_columns: List[str],
                      df1_name: str, df2_name: str) -> Tuple[str, float]:
    """Compare two dataframes using datacompy and return the comparison report."""
    comparison = datacompy.Compare(
        df1,
        df2,
        join_columns=join_columns,
        df1_name=df1_name,
        df2_name=df2_name
    )
    
    return comparison.report(), comparison.match_score 
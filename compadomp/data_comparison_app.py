 import streamlit as st
import pandas as pd
import datacompy
import io
from typing import Tuple, List

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
                      compare_cols: List[str], join_columns: List[str]) -> Tuple[str, float]:
    """Compare two dataframes using datacompy and return the comparison report."""
    comparison = datacompy.Compare(
        df1,
        df2,
        join_columns=join_columns,
        df1_name='Dataset 1',
        df2_name='Dataset 2'
    )
    
    return comparison.report(), comparison.match_score

def main():
    st.title("Dataset Comparison Tool")
    st.write("Upload two CSV or Excel files to compare their contents")

    # File uploaders
    file1 = st.file_uploader("Upload first dataset", type=['csv', 'xlsx', 'xls'])
    file2 = st.file_uploader("Upload second dataset", type=['csv', 'xlsx', 'xls'])

    if file1 and file2:
        try:
            df1 = load_file(file1)
            df2 = load_file(file2)

            # Get common columns between the two datasets
            common_columns = list(set(df1.columns) & set(df2.columns))
            
            # Column selection
            st.subheader("Select columns for comparison")
            selected_columns = st.multiselect(
                "Choose columns to compare",
                common_columns,
                default=common_columns
            )

            if selected_columns:
                # Create synthetic key if multiple columns are selected
                if len(selected_columns) > 1:
                    st.info("Creating synthetic key from selected columns")
                    df1 = create_synthetic_key(df1, selected_columns)
                    df2 = create_synthetic_key(df2, selected_columns)
                    join_columns = ['synthetic_key']
                else:
                    join_columns = selected_columns

                if st.button("Compare Datasets"):
                    report, match_score = compare_dataframes(
                        df1, df2, selected_columns, join_columns
                    )

                    # Display match score
                    st.subheader("Match Score")
                    st.write(f"The datasets are {match_score:.2%} similar")

                    # Display report
                    st.subheader("Comparison Report")
                    st.text(report)

                    # Download report
                    report_bytes = report.encode()
                    st.download_button(
                        label="Download Report",
                        data=report_bytes,
                        file_name="comparison_report.txt",
                        mime="text/plain"
                    )

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 
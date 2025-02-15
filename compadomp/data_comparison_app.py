import streamlit as st
import pandas as pd
from typing import List
from .utils import load_file, create_synthetic_key, compare_dataframes

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
            
            # Get file names without extension for labeling
            df1_name = file1.name.rsplit('.', 1)[0]
            df2_name = file2.name.rsplit('.', 1)[0]

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
                        df1, df2, selected_columns, join_columns,
                        df1_name=df1_name, df2_name=df2_name
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
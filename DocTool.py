import streamlit as st
import pandas as pd

def main():
    st.title("Excel Spreadsheet Uploader")

    # Allow users to upload an Excel file
    uploaded_file = st.file_uploader("Upload Excel file", type=["xls", "xlsx"])

    if uploaded_file is not None:
        try:
            # Read the Excel file into a DataFrame
            df = pd.read_excel(uploaded_file)
            
            # Display the DataFrame
            st.write("Preview of the uploaded Excel file:")
            st.dataframe(df.head())

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


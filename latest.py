import streamlit as st
import pandas as pd

# Streamlit UI
st.title("CSV Duplicate Checker")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding="latin-1")

    st.write("### Original Data Preview:")
    st.dataframe(df.head())  # Show the first few rows of the uploaded data

    # Duplicate Detection
    duplicate_columns = st.multiselect("Select columns to check for duplicates", df.columns)

    if duplicate_columns:
        df["Duplicate"] = df.duplicated(subset=duplicate_columns, keep="first")

        # Mark duplicates explicitly for visibility
        df["Delete"] = df["Duplicate"].map({True: "Delete", False: ""})

        # Save the modified file
        output_filename = "duplicates-file-odc.csv"
        df.to_csv(output_filename, index=False)

        st.write("### Processed Data Preview:")
        st.dataframe(df.head())  # Show preview after marking duplicates

        # Provide download button
        st.download_button(
            label="Download Processed CSV",
            data=df.to_csv(index=False),
            file_name=output_filename,
            mime="text/csv"
        )
    else:
        st.warning("Please select at least one column for duplicate checking.")

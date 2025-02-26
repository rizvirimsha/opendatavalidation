import streamlit as st
import pandas as pd

# Streamlit UI
st.title("CSV Duplicate Checker")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded file
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding="latin-1")

    # Mark duplicates: keep only the first occurrence
    df["Delete"] = df.duplicated(keep="first").map({True: "Delete", False: ""})

    # Save the modified file
    output_filename = "duplicates-file-odc.csv"
    df.to_csv(output_filename, index=False)

    # Show preview of processed data
    st.write("### Processed Data Preview:")
    st.dataframe(df.head())

    # Provide download button
    st.download_button(
        label="Download Processed CSV",
        data=df.to_csv(index=False),
        file_name=output_filename,
        mime="text/csv"
    )

    st.success("Duplicates marked and saved in duplicates-file-odc.csv")

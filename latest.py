import streamlit as st
import pandas as pd

# Streamlit UI for file upload
st.title("CSV Duplicate Checker")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding="latin-1")

    # Mark duplicates
    df["Delete"] = df.duplicated(keep="first").map({True: "Delete", False: ""})

    # Save the modified file
    output_filename = "duplicates-file-odc.csv"
    df.to_csv(output_filename, index=False)

    st.write("Duplicates marked. Preview below:")
    st.dataframe(df.head())  # Show a preview of the data

    # Provide a download link
    st.download_button(
        label="Download Processed CSV",
        data=df.to_csv(index=False),
        file_name=output_filename,
        mime="text/csv"
    )

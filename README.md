# opendatavalidation
A simple Python script that scans your dataset for duplicate rows and flags them for deletion. Upload your file, and the script will generate a new version with an additional column indicating duplicates.
import pandas as pd
from google.colab import files

uploaded = files.upload()
file_name = list(uploaded.keys())[0]

try:
    df = pd.read_csv(file_name, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_name, encoding='latin-1')

df['Delete'] = df.duplicated(keep='first').map({True: 'Delete', False: ''})
df.to_csv('duplicates-file-odc.csv', index=False)

files.download('duplicates-file-odc.csv')
print("Duplicates marked and saved in duplicates-file-odc.csv")

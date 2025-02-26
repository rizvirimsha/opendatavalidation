import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# Create an upload widget
upload_widget = widgets.FileUpload(accept='.csv', multiple=False)
display(upload_widget)

def load_data(upload_widget):
    if upload_widget.value:
        uploaded_file = list(upload_widget.value.values())[0]
        file_name = uploaded_file['metadata']['name']
        content = uploaded_file['content']

        # Read CSV into a pandas DataFrame
        try:
            df = pd.read_csv(content, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(content, encoding='latin-1')

        # Mark duplicates
        df['Delete'] = df.duplicated(keep='first').map({True: 'Delete', False: ''})

        # Save the modified file
        df.to_csv('duplicates-file-odc.csv', index=False)
        print("Duplicates marked and saved in duplicates-file-odc.csv")

# Button to trigger file processing
process_button = widgets.Button(description="Process File")
process_button.on_click(lambda x: load_data(upload_widget))
display(process_button)



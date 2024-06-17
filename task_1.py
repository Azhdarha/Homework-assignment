import pandas as pd


file_names = ['file.xlsx', 'file3.xlsx', 'file2.xlsx']


for file_name in file_names:
    print(f"Contents of file '{file_name}':\n")

    # Reading multiple sheets from an Excel file
    sheets_dict = pd.read_excel(file_name, engine="openpyxl", sheet_name=None)

    # Accessing individual sheets and displaying their contents
    for sheet_name, df in sheets_dict.items():
        print(f"Sheet '{sheet_name}':\n{df}\n")

    print("\n")
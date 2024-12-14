# Import data using pandas
import pandas as pd

# Import Excel file (Block 4, 7, 9)
def import_excel_file(file_path):
    """
    Imports data from an Excel file into a pandas DataFrame.

    Parameters:
        file_path (str): The path to the Excel file to be imported.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the specified Excel file.
    """
    data = pd.read_excel(file_path)
    return data

# Import CSV file (Block 4)
def import_csv_file(file_path):
    """
    Imports data from a CSV file into a pandas DataFrame.

    Parameters:
        file_path (str): The path to the CSV file to be imported.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the specified CSV file.
    """
    data = pd.read_csv(file_path)
    return data

# Import and merge Excel files from a folder (Block 9)
import os

def import_and_merge_excel_files(folder_path):
    """
    Imports and merges data from multiple Excel files in a specified folder into a single pandas DataFrame.

    Parameters:
        folder_path (str): The path to the folder containing the Excel files to be imported.

    Returns:
        pd.DataFrame: A DataFrame containing the combined data from all Excel files in the specified folder.

    Process:
        - Iterates through all files in the folder.
        - Imports each file as a pandas DataFrame using `import_excel_file`.
        - Appends each DataFrame to a list.
        - Concatenates all DataFrames into a single DataFrame and returns it.
    """
    all_data = []  # List to store the DataFrames of the Excel files

    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        # Path to the Excel file
        file_path = os.path.join(folder_path, file_name)

        # Import the Excel file
        data = import_excel_file(file_path)

        # Append the DataFrame to the list of DataFrames
        all_data.append(data)

    # Merge all DataFrames
    combined_data = pd.concat(all_data, ignore_index=True)

    return combined_data
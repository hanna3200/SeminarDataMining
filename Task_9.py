import data_import
import pandas as pd


# Function to import December production data (Day 1 and without Day 1)
def load_december_data():
    """
    This function performs the following tasks:
    1. Loads the production data for December, specifically for Day 1.
    2. Loads the production data for December excluding Day 1.
    3. Corrects any erroneous entries in the 'Prüfresultat' column (replaces value 11 with 1).
    4. Merges the two datasets (Day 1 and excluding Day 1 data) into one combined DataFrame.

    Returns:
    - production_data_december (pd.DataFrame): The combined DataFrame containing both Day 1 and excluding Day 1 December production data.
    """
    # Import December Day 1 production data
    excel_file_path = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/01_Block5_Produktionstag 1/Dezember_Produktionstag1.xlsx"
    december_day1 = data_import.import_excel_file(excel_file_path)

    # Import December production data excluding Day 1
    excel_file_path = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/02_Block9_Zusammenführung/Dezember_ohne_Tag1.xlsx"
    december_without_day1 = data_import.import_excel_file(excel_file_path)

    # Manual correction for "December_without_Day1"
    december_without_day1['Prüfresultat'] = december_without_day1['Prüfresultat'].replace(11, 1)

    # Merge December datasets
    production_data_december = pd.concat([december_day1, december_without_day1], ignore_index=True)

    return production_data_december


# Function to load January production data
def load_january_data():
    """
    This function imports the production data for January from a specified Excel file.

    Returns:
    - production_data_january (pd.DataFrame): A DataFrame containing the January production data.
    """
    excel_file_path = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/02_Block9_Zusammenführung/Januar.xlsx"
    production_data_january = data_import.import_excel_file(excel_file_path)

    return production_data_january


# Function to load and merge February production data (first parts)
def load_february_data_first_parts():
    """
    This function imports all Excel files from the specified folder that contain the first parts of the February production data.
    The files are then merged into a single DataFrame.

    Returns:
    - combined_data_february_first_parts (pd.DataFrame): A DataFrame containing the merged February first parts data.
    """
    folder_path = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/02_Block9_Zusammenführung/Februar/erste_Teile"
    combined_data_february_first_parts = data_import.import_and_merge_excel_files(folder_path)

    return combined_data_february_first_parts


# Function to load and correct February production data (remaining data)
def load_february_data_rest():
    """
    This function performs the following tasks:
    1. Imports the remaining February production data from an Excel file.
    2. Combines the 'Datumsstempel' (date) and 'Uhrzeit' (time) columns into a single 'Zeitstempel' (timestamp) column.
    3. Drops the original 'Datumsstempel' and 'Uhrzeit' columns to maintain only the 'Zeitstempel' column.

    Returns:
    - production_data_february_rest (pd.DataFrame): A DataFrame containing the corrected February production data.
    """
    excel_file_path = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/02_Block9_Zusammenführung/Februar/Februar_Rest.xlsx"
    production_data_february_rest = data_import.import_excel_file(excel_file_path)

    # Combine 'Datumsstempel' and 'Uhrzeit' into 'Zeitstempel'
    production_data_february_rest['Zeitstempel'] = production_data_february_rest['Datumsstempel'].astype(str) + ' ' + \
                                                   production_data_february_rest['Uhrzeit'].astype(str)

    # Drop the original columns
    production_data_february_rest.drop(['Datumsstempel', 'Uhrzeit'], axis=1, inplace=True)

    return production_data_february_rest


# Function to merge all production data (December, January, and February)
def merge_all_production_data():
    """
    This function combines the production data from three months: December, January, and February.
    It first loads the data from each month, then merges the February data (first and remaining parts),
    and finally combines all three months into one DataFrame.

    Returns:
    - production_data_overall (pd.DataFrame): A DataFrame containing the combined production data for December, January, and February.
    """
    # Load data
    production_data_december = load_december_data()
    production_data_january = load_january_data()
    combined_data_february_first_parts = load_february_data_first_parts()
    production_data_february_rest = load_february_data_rest()

    # Merge February datasets
    production_data_february = pd.concat([combined_data_february_first_parts, production_data_february_rest],
                                         ignore_index=True)

    # Merge all datasets
    production_data_overall = pd.concat([production_data_december, production_data_february, production_data_january],
                                        ignore_index=True)

    return production_data_overall


# Main function to execute the entire data processing
def main():
    """
    Main function to execute the entire data processing pipeline.

    This function calls the 'merge_all_production_data' function to load and merge the production data from December,
    January, and February. The merged data is then displayed.

    Returns:
    - None
    """
    # Merge all production data
    production_data_overall = merge_all_production_data()

    # Display result (should have 284,789 rows)
    print("Overall Production Data:")
    print(production_data_overall)


if __name__ == "__main__":
    main()
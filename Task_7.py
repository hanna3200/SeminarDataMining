import data_import
import pandas as pd
import matplotlib.pyplot as plt


# Function 1.1: Overall Statistics of Test Results
def task_1_1(production_day1):
    """
    Calculates the defect rate of test results and creates a pie chart.

    Parameters:
    - production_day1: The DataFrame with the production data.

    Returns:
    - None
    """
    test_results = production_day1['Prüfresultat']

    # Count defects and non-defects
    defect_count = test_results[test_results == 2].count()
    total_count = len(test_results)

    # Calculate defect rate
    defect_rate = defect_count / total_count
    no_defect_rate = 1 - defect_rate

    # Create a pie chart
    labels = ['Defects (Test Result is 2)', 'No Defects (Test Result is 1)']
    sizes = [defect_rate, no_defect_rate]
    colors = ['red', 'green']
    explode = (0.1, 0)  # Highlight the "Defects" section slightly

    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%.2f%%', startangle=140)
    plt.title('Defect Rate of Test Results - Day 1')
    plt.axis('equal')  # Ensure the pie chart is circular
    plt.show()


# Function 1.2: Test Bench Statistics
def task_1_2(production_day1):
    """
    Calculates the statistics for each test bench and outputs them as a DataFrame.

    Parameters:
    - production_day1: The DataFrame with the production data.

    Returns:
    - summary: A DataFrame containing the statistics for each test bench.
    """
    groups = production_day1.groupby('Prüfstand')

    # Initialize lists for the results
    test_bench_list = []
    tested_parts_count = []
    defect_counts = []
    defect_rates = []

    # Calculate statistics for each test bench
    for test_bench, group in groups:
        total = len(group)  # Number of tested parts
        defects = group[group['Prüfresultat'] == 2].shape[0]  # Number of defects
        defect_rate = defects / total if total > 0 else 0  # Defect rate

        # Store the results
        test_bench_list.append(test_bench)
        tested_parts_count.append(total)
        defect_counts.append(defects)
        defect_rates.append(defect_rate)

    # Create the DataFrame with the results
    summary = pd.DataFrame({
        'Test Bench': test_bench_list,
        'Number of Tested Parts': tested_parts_count,
        'Number of Defects': defect_counts,
        'Defect Rate (%)': [round(rate * 100, 2) for rate in defect_rates]  # Defect rate in percentage
    })

    # Print the summary table
    print(summary)


# Function 1.3: Frequency of Defect Codes
def task_1_3(production_day1):
    """
    Calculates the frequency of defect codes and creates a pie chart.

    Parameters:
    - production_day1: The DataFrame with the production data.

    Returns:
    - None
    """
    defect_codes = production_day1['Fehlercode']

    # Filter out entries with "0", as this is not a valid defect code
    defect_codes = defect_codes[defect_codes != 0]

    # Count the occurrences of defect codes
    defect_code_counts = defect_codes.value_counts()

    # Calculate the percentage frequencies
    defect_code_percent = defect_code_counts / defect_code_counts.sum() * 100

    # Prepare data for the pie chart
    labels = [f"{code}" for code in defect_code_counts.index]  # Only the defect code
    sizes = defect_code_counts
    colors = plt.cm.tab10.colors  # Colors from a predefined color palette

    # Function to create labels with count and percentage
    def make_label(count, percent):
        return f'{count} ({percent:.2f}%)'

    # Create the pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct=lambda p: make_label(int(p * sum(sizes) / 100), p),
            startangle=140)
    plt.title('Frequency Distribution of Defect Codes')
    plt.axis('equal')  # Ensure the pie chart is circular
    plt.show()


# Main function: Orchestrates the entire process
def main():
    # Path to the Excel file
    excel_file_path = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/01_Block5_Produktionstag 1/Dezember_Produktionstag1.xlsx"

    # Load the production data
    production_day1 = data_import.import_excel_file(excel_file_path)

    # Task 1.1: Overall statistics of test results
    task_1_1(production_day1)

    # Task 1.2: Test bench statistics
    task_1_2(production_day1)

    # Task 1.3: Frequency of defect codes
    task_1_3(production_day1)


if __name__ == "__main__":
    main()
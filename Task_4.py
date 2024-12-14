import data_import
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Part 1: Importing, adjusting column names, and combining tables
def process_and_combine_tables():
    """
    The function performs the following steps:
    1. Imports data from an Excel file and a CSV file.
    2. Renames a specific column in the first table to match a required format.
    3. Combines the two tables vertically into a single table.
    4. Renames the column names to English.

    Parameters:
    None

    Returns:
    pd.DataFrame: A single DataFrame containing the combined and processed data from both the Excel and CSV files.
    """
    # Part 1.1: Import data from Excel and CSV
    # Import Excel file
    excel_file_path = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/00_Block4_Iris Flower DataSet/Iris_01.xlsx"
    table1 = data_import.import_excel_file(excel_file_path)

    # Import CSV file
    csv_file_path = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/00_Block4_Iris Flower DataSet/Iris_02.csv"
    table2 = data_import.import_csv_file(csv_file_path)

    # Display the imported data
    print("Part 1.1 Table 1")
    print(table1)
    print("Part 1.1 Table 2")
    print(table2)


    # Part 1.2: Align column names
    table1.rename(columns={'Sepal Länge': 'sepal length'}, inplace=True)

    # Display updated tables
    print("Part 1.2 Table 1 (After Renaming)")
    print(table1)
    print("Part 1.2 Table 2")
    print(table2)


    # Part 1.3: Combine tables (stack them vertically)
    combined_table = pd.concat([table1, table2], ignore_index=True)

    # Display combined table
    print("Part 1.3 Combined Table")
    print(combined_table)


    # Part 1.4: Rename all column names to English
    combined_table.rename(columns={'Art': 'species'}, inplace=True)

    # Display final combined table
    print("Part 1.4 Combined Table (After Renaming Columns to English)")
    print(combined_table)

    # Return the final combined table
    return combined_table



# Part 2: Visualizing the classification of Iris flowers
def visualize_data(combined_table):
    """
    The function performs the following steps:
    1. Creates a 2D scatter plot comparing sepal length and sepal width.
    2. Creates a 2D scatter plot comparing petal length and petal width.
    3. Generates a scatter matrix to display all pairwise relationships between features.
    4. Creates a 3D scatter plot to visualize the relationships between sepal length, sepal width, and petal length.

    Parameters:
    combined_table (pd.DataFrame): A DataFrame containing the combined data of the iris flowers.

    Returns:
    None
    """
    # Part 2.1: Create scatter plot for sepal length and width, colored by "species"
    plt.figure(figsize=(10, 6))  # Set the size of the plot
    sns.scatterplot(
        data=combined_table,
        x='sepal length',  # X-axis: Sepal Length
        y='sepal width',  # Y-axis: Sepal Width
        hue='species',  # Color differentiation by species
        style='species',  # Point style for each species
        palette={'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'},  # Colors for each category
    )

    # Add title and axis labels
    plt.title('Sepal Length vs. Sepal Width by Species')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')

    # Show plot
    plt.show()


    # Part 2.2: Create scatter plot for petal length and width, colored by "species"
    plt.figure(figsize=(10, 6))  # Set the size of the plot
    sns.scatterplot(
        data=combined_table,
        x='petal length',  # X-axis: Petal Length
        y='petal width',  # Y-axis: Petal Width
        hue='species',  # Color differentiation by species
        style='species',  # Point style for each species
        palette={'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'},  # Colors for each category
    )

    # Add title and axis labels
    plt.title("Petal Length vs. Petal Width by Species")
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")

    # Show plot
    plt.show()


    # Part 2.3: Scatter matrix with all possible scatter plots
    scatter_matrix = sns.pairplot(
        combined_table,  # The combined table
        hue='species',  # Color differentiation by "species"
        palette={'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'},  # Colors for each category
        diag_kind="auto",  # Scatter plots on the diagonal
        markers=["o", "s", "D"],  # Point markers for each category
        plot_kws={'s': 50}  # Adjust point size in scatter plot
    )

    # Add title
    scatter_matrix.fig.suptitle("Scatter Matrix: Pairwise Feature Representation", y=1.02)

    # Adjust plot size if needed
    scatter_matrix.fig.set_size_inches(12, 7)  # Set width and height in inches

    # Show plot
    plt.show()


    # Part 2.4: 3D scatter plot with sepal length, sepal width, and petal length
    # Prepare data for 3D plot
    color_mapping = {'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'}
    x = combined_table['sepal length']  # X-axis
    y = combined_table['sepal width']  # Y-axis
    z = combined_table['petal length']  # Z-axis
    category = combined_table['species']  # Categorical variable
    colors = category.map(color_mapping)

    # Prepare 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Create 3D scatter plot
    scatter = ax.scatter(x, y, z, c=colors, s=50)  # 'c=colors' applies color coding

    # Add axis labels
    ax.set_xlabel('Sepal Length')
    ax.set_ylabel('Sepal Width')
    ax.set_zlabel('Petal Length')

    # Add title
    plt.title('3D Scatter Plot with Categorical Coloring')

    # Add legend
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label)
               for label, color in color_mapping.items()]
    ax.legend(handles=handles, title='species', loc='upper left')

    # Show plot
    plt.show()


# Main function to execute the entire process
def main():
    """
    Main function that orchestrates the data processing and visualization.

    It first processes and combines the data tables by calling the `process_and_combine_tables`
    function. Then it visualizes the processed data using the `visualize_data` function.

    Parameters:
    None

    Returns:
    None
    """
    # Part 1: Process and combine tables
    combined_table = process_and_combine_tables()

    # Part 2: Visualize the data
    visualize_data(combined_table)


if __name__ == "__main__":
    main()
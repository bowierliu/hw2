import pandas as pd

def clean_stats_csv(file_path):
    """
    Reads a CSV file, removes rows with missing values, removes duplicate rows,
    and outputs summary statistics of all numeric columns.

    Parameters:
    - file_path (str): The file path to the CSV file.

    Returns:
    - DataFrame: A DataFrame containing the summary statistics (count, mean, std, min,
      25%, 50%, 75%, max) of each numeric column.
    """

    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Remove rows with missing values
    df.dropna(inplace=True)
    
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Compute and return summary statistics of numeric columns
    summary_stats = df.describe()
    
    return summary_stats


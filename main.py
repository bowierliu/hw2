from clean_stats_csv import clean_stats_csv


if __name__ == '__main__':

    # Allow users to dynamically enter the path to their CSV file when they run the script
    file_path = input('Please paste the path to your CSV file here: ')

    # Use the imported function fron clean_stats_csv to retrive summary stats for CSV file
    stats = clean_stats_csv(file_path)

    # Print the summary stats for users
    print(stats)
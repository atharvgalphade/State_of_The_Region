import pandas as pd
import glob

# Define file paths
unemployment_files = glob.glob('Unemployment/*.csv')
population_files = glob.glob('Population/*.csv')

def read_and_process_files(file_list, value_col, date_col, rename_col):
    dfs = []
    for file in file_list:
        county = file.split('\\')[-1].split('_')[0]
        df = pd.read_csv(file)
        df[date_col] = pd.to_datetime(df[date_col]).dt.date
        df = df.rename(columns={value_col: rename_col})
        df['county'] = county
        dfs.append(df)
    return pd.concat(dfs, axis=0)

# Read and process unemployment data
unemployment_df = read_and_process_files(unemployment_files, 'value', 'date', 'unemployment_rate')

# Read and process population data
population_df = read_and_process_files(population_files, 'value', 'date', 'population')

# Merge unemployment and population data
merged_df = pd.merge(unemployment_df, population_df, on=['date', 'county'], how='left')

# Debug: Print column names and a sample of the DataFrame
print("Columns in merged DataFrame:", merged_df.columns)
print("Sample data from merged DataFrame:", merged_df.head())

# Ensure the 'unemployment_rate' column is present for pivoting
if 'unemployment_rate' not in merged_df.columns:
    print("Error: 'unemployment_rate' column is missing.")
else:
    # Pivot table to get the desired format
    pivot_df = merged_df.pivot_table(index='date', columns='county', values='unemployment_rate')

    # Save to Excel
    pivot_df.to_excel('tampa_bay_unemployment_data_1990_2023.xlsx', sheet_name='County Data')
    print('Excel file with monthly county unemployment rates generated successfully.')

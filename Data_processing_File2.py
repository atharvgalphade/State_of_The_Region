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
        df[date_col] = pd.to_datetime(df[date_col]).dt.date  # Ensure only date is kept
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

# Convert 'date' to datetime and extract year
merged_df['date'] = pd.to_datetime(merged_df['date'])
merged_df['year'] = merged_df['date'].dt.year

# Calculate weighted unemployment rate
def weighted_unemployment_rate(group):
    numerator = (group['unemployment_rate'] * group['population']).sum()
    denominator = group['population'].sum()
    return numerator / denominator if denominator != 0 else float('nan')

# Group by year and calculate weighted unemployment rate
yearly_unemployment_df = merged_df.groupby('year').apply(weighted_unemployment_rate).reset_index(name='Tampa Bay Region Unemployment Rate')

# Rename the year column to the required date format
yearly_unemployment_df['date'] = pd.to_datetime(yearly_unemployment_df['year'].astype(str) + '-01-01').dt.date
yearly_unemployment_df = yearly_unemployment_df[['date', 'Tampa Bay Region Unemployment Rate']]

# Save to Excel
# yearly_unemployment_df.to_excel('tampa_bay_unemployment_data_1990_2023.xlsx', sheet_name='Tampa Bay Region Data', index=False)
# print('Excel file with yearly weighted unemployment rates for the Tampa Bay region generated successfully.')
file_path='tampa_bay_unemployment_data_1990_2023.xlsx'
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='new') as writer:
    yearly_unemployment_df.to_excel(writer, sheet_name='Tampa Bay Region Data', index=False)

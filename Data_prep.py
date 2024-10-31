import requests
import pandas as pd

# API Key
API_KEY = 'd184d62af80a78adef57b56488ce649c'

# FRED base URL
base_url = "https://api.stlouisfed.org/fred/series/observations"

# Function to get data from FRED API
def get_fred_data(series_id, api_key, start_date="1990-01-01", end_date="2023-12-31"):
    params = {
        'series_id': series_id,
        'api_key': api_key,
        'file_type': 'json',
        
        'observation_start': start_date,
        'observation_end': end_date,
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()['observations']
        df = pd.DataFrame(data)
        return df[['date', 'value']]  # Return only date and value columns
    else:
        print(f"Error fetching data for series: {series_id}")
        return None

# Example: Pull unemployment rate and population data for all counties.
series_id_Hillsborough_unemployment = "FLHILL7URN"
series_id_Hillsborough_population = "FLHILL7POP"
series_id_Pinellas_unemployment="FLPINE5URN"
series_id_Pinellas_population="FLPINE5POP"
series_id_Pasco_unemployment="FLPASC5URN"
series_id_Pasco_population="FLPASC5POP"
series_id_Hernando_unemployment="FLHERN3URN"
series_id_Hernando_population="FLHERN3POP"
series_id_Manatee_unemployment="FLMANA1URN"
series_id_Manatee_population="FLMANA1POP"
series_id_Sarasota_unemployment="FLSARA5URN"
series_id_Sarasota_population="FLSARA5POP"
series_id_Polk_unemployment="FLPOLK5URN"
series_id_Polk_population="FLPOLK5POP"
series_id_Citrus_unemployment="FLCITR5URN"
series_id_Citrus_population="FLCITR5POP"

# Get unemployment data
Hillsborough_unemployment_df = get_fred_data(series_id_Hillsborough_unemployment, API_KEY)
Pinellas_unemployment_df=get_fred_data(series_id_Pinellas_unemployment, API_KEY)
Pasco_unemployment_df = get_fred_data(series_id_Pasco_unemployment, API_KEY)
Hernando_unemployment_df = get_fred_data(series_id_Hernando_unemployment, API_KEY)
Manatee_unemployment_df = get_fred_data(series_id_Manatee_unemployment, API_KEY)
Sarasota_unemployment_df = get_fred_data(series_id_Sarasota_unemployment, API_KEY)
Polk_unemployment_df = get_fred_data(series_id_Polk_unemployment, API_KEY)
Citrus_unemployment_df = get_fred_data(series_id_Citrus_unemployment, API_KEY)

# Get population data
Hillsborough_population_df = get_fred_data(series_id_Hillsborough_population, API_KEY)
Pinellas_population_df = get_fred_data(series_id_Pinellas_population, API_KEY)
Pasco_population_df = get_fred_data(series_id_Pasco_population, API_KEY)
Hernando_population_df = get_fred_data(series_id_Hernando_population, API_KEY)
Manatee_population_df = get_fred_data(series_id_Manatee_population, API_KEY)
Sarasota_population_df = get_fred_data(series_id_Sarasota_population, API_KEY)
Polk_population_df = get_fred_data(series_id_Polk_population, API_KEY)
Citrus_population_df = get_fred_data(series_id_Citrus_population, API_KEY)

# Save to CSV (you can extend this for other counties)
Hillsborough_unemployment_df.to_csv('Hillsborough_unemployment_data.csv', index=False)
Pinellas_unemployment_df.to_csv('Pinellas_unemployment_data.csv', index=False)
Pasco_unemployment_df.to_csv('Pasco_unemployment_data.csv', index=False)
Hernando_unemployment_df.to_csv('Hernando_unemployment_data.csv', index=False)
Manatee_unemployment_df.to_csv('Manatee_unemployment_data.csv', index=False)
Sarasota_unemployment_df.to_csv('Sarasota_unemployment_data.csv', index=False)
Polk_unemployment_df.to_csv('Polk_unemployment_data.csv', index=False)
Citrus_unemployment_df.to_csv('Citrus_unemployment_data.csv', index=False)

Hillsborough_population_df.to_csv('Hillsborough_population_data.csv', index=False)
Pinellas_population_df.to_csv('Pinellas_population_data.csv', index=False)
Pasco_population_df.to_csv('Pasco_population_data.csv', index=False)
Hernando_population_df.to_csv('Hernando_population_data.csv', index=False)
Manatee_population_df.to_csv('Manatee_population_data.csv', index=False)
Sarasota_population_df.to_csv('Sarasota_population_data.csv', index=False)
Polk_population_df.to_csv('Polk_population_data.csv', index=False)
Citrus_population_df.to_csv('Citrus_population_data.csv', index=False)

print("Data has been successfully pulled and saved.")
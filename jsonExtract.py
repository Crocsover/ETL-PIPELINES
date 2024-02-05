import pandas as pd
import json

def extract_id_and_domains(json_string):
    try:
        parsed_data = json.loads(json_string)
        id_value = parsed_data.get('id')
        domains_value = parsed_data.get('domains')
        return id_value, domains_value
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None, None

# Load the Excel file into a DataFrame
excel_file_path = r'C:\Users\Public\jsonfile.xlsx'
df = pd.read_excel(excel_file_path)

# Create new columns for 'ID' and 'Domains'
df['ID'] = None
df['Domains'] = None

# Iterate through each row and extract 'id' and 'domains'
for index, row in df.iterrows():
    json_string = row['json_data']  # Change 'json_data' to the correct column name
    id_value, domains_value = extract_id_and_domains(json_string)
    df.at[index, 'ID'] = id_value
    df.at[index, 'Domains'] = domains_value

# Print the updated DataFrame
print(df[['ID', 'Domains']])

# etl/etl_pipeline.py
import pandas as pd

# Extract
data = pd.read_csv('data/source_data.csv')

# Transform
data['new_column'] = data['existing_column'] * 2

# Filter rows where 'existing_column' > 50
filtered_data = data[data['existing_column'] > 50]

# Load
filtered_data.to_csv('data/transformed_data.csv', index=False)

print("ETL Pipeline executed successfully")

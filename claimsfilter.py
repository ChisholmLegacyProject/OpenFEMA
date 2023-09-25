import csv
import pandas as pd

# Read in data 
data = pd.read_csv('YOURFEMADATA.csv')

# Filter out NULL values
data = data[data['amountPaidOnBuildingClaim'] != 'NULL'] 
data = data[data['amountPaidOnContentsClaim'] != 'NULL']

# Calculate totals
data['total_paid'] = data['amountPaidOnBuildingClaim'].astype(float) + data['amountPaidOnContentsClaim'].astype(float)

# Groupby and sum totals
aggregated = data.groupby('reportedZipCode')['total_paid'].sum().reset_index()

# Export aggregated data
aggregated.to_csv('aggregated.csv', index=False)

print('Aggregated data exported to aggregated.csv')

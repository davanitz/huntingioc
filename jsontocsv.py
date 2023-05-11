# Convert a JSON String to CSV Using Python
import pandas as pd
df = pd.read_json (r'assets.json', lines=True)
df.to_csv (r'file.csv', index = None)
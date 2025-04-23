import pandas as pd
from pathlib import Path

# base_dir = Path("options-data/banknifty_data/banknifty_options/2023")  # replace with your actual root path
base_dir = Path("options-data/banknifty_data/banknifty_spot/2023")  # replace with your actual root path
all_csvs = list(base_dir.rglob("banknifty_spot*.csv"))

df = pd.concat([pd.read_csv(f) for f in all_csvs], ignore_index=True)
print("Done0")
df.to_csv('full-nifty-spot.csv', index=False)
print("Done1")
import glob
import os

import pandas as pd

path = r'usedcsv'
all_files = glob.glob(os.path.join(path, "diemthi_*.csv"))
print(all_files)
all_lines = (pd.read_csv(link) for link in all_files)

# merge_df = pd.read_csv('merged.csv')
merge_df = pd.concat(all_lines, ignore_index=True)
print(merge_df)
# pd.concat()

merge_df.to_csv(r'csv\merged.csv', index=False)

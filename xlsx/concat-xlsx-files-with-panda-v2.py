# Need to install:
# pip install pandas
# pip install openpyxl
# pip install xlrd

# Ref: https://stackoverflow.com/questions/15793349/how-to-concatenate-three-excels-files-xlsx-using-python

import pandas as pd
# import numpy as np
import glob

all_data = pd.DataFrame()
for f in glob.glob('*.xlsx'):
   df = pd.read_excel(f)
   all_data = all_data.append(df, ignore_index=True)

writer = pd.ExcelWriter('mycollected_data.xlsx')
# writer = pd.ExcelWriter('mycollected_data.xlsx', engine='xlsxwriter')
all_data.to_excel(writer, sheet_name='Sheet1')
writer.save()


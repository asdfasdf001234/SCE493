import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

input_file_path = 'clinical.sampleMap_STAD_clinicalMatrix'  
output_file_path = 'binary_label.csv'  

df = pd.read_csv(input_file_path, sep='\t')
df.fillna('')

new_df = pd.DataFrame()
new_df['sampleID'] = df['sampleID'].copy()
new_df['MSS'] = 0
new_df['MSI'] = 0

for i in range(df.shape[0]): 
    row = df.iloc[i]
    #print(row['CDE_ID_3226963'])
    
    if row['CDE_ID_3226963'] == 'MSS':
        print(i)
        new_df.loc[i, 'MSS'] = 1
        
    elif row['CDE_ID_3226963'] == 'MSI-L':
        new_df.loc[i, 'MSI'] = 1
    elif row['CDE_ID_3226963'] == 'MSI-H':
        new_df.loc[i, 'MSI'] = 1     
    else:
        print(i)
        new_df.loc[i, 'MSI'] = np.NaN 

new_df = new_df.dropna(axis = 0, how='any')

print(new_df)
        
new_df.to_csv(output_file_path, index=False)



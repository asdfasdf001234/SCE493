import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

input_file_path = 'new_mapping_STAD.csv' 
output_file_path = 'mapping.csv'  

df = pd.read_csv(input_file_path, sep=',')
df.fillna(0.0)

all_genes = set(gene for genes in df['gene'] if genes != '.' for gene in genes.split(','))


matrix = np.zeros((len(df), len(all_genes)), dtype='int8')
    
ID_to_gene = {ID: df.iloc[idx]['gene'] for idx, ID in enumerate(df['#id'])}
for ID, gene in ID_to_gene.items():
    gene_list = gene.split(',')
    ID_to_gene[ID] = gene_list

i = 0
for ID, gene_list in ID_to_gene.items():
    j = 0
    for element in all_genes:
        if element in gene_list:
            matrix[i][j] = 1.0
        j += 1
    i += 1
    if i == j:
        print(i, j)

sparse_matrix = csr_matrix(matrix)
print("sparse_matrix done")

new_df = pd.DataFrame.sparse.from_spmatrix(
    sparse_matrix,
    index=df['#id'],  
    columns=all_genes
)
print("dataframe generated")

new_df.to_csv(output_file_path, index=True)

print("csv file saved")

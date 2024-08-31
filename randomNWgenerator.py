import csv
import random

# mapping.csv 파일 읽기
with open('mapping.csv', mode='r') as file:
    reader = csv.reader(file)
    
    genes = next(reader)[1:]  
    samples = []
    for row in reader:
        samples.append(row[0])  

num_columns = len(genes)
num_rows = len(samples)
print("num_col: "+str(num_columns))
print("num_row: "+str(num_rows))

matrix = [[0] * num_columns for _ in range(num_rows)]

for i in range(num_rows):
    column_index = random.randint(0, num_columns - 1)
    matrix[i][column_index] = 1

output_file = 'random_adjacent_matrix.csv'
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow([""] + genes)  
    
    for sample, row in zip(samples, matrix):
        writer.writerow([sample] + row)

print("randomNW generated")

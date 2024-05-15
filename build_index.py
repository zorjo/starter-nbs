import pandas
import itertools
# Step 1: Read the main sales csv file
df=pandas.read_csv("~/Downloads/ms.csv" )
#df.rename(columns={df.columns[4]:'asin'})
columns = ['category', 'asin']
# Step 2: Get unique values for the columns
unique_values = {}
for column in columns:
    unique_values[column] = df[column].unique()

# Step 3: Generate all possible combinations of the unique values and create the index dataframe
combinations = list(itertools.product(*unique_values.values()))
comboname = pandas.DataFrame(columns= ["file_name"]+columns)

# Step 4: Apply each combination as a filter and write to separate CSV files
j = 0
for combination in combinations:
    filtered_df = df
    for i, column in enumerate(columns):
        filtered_df = filtered_df[filtered_df[column] == combination[i]]
    if not filtered_df.empty:
        output_file = f'output_{j}.csv'
        filtered_df.to_csv(output_file, index=False, quotechar="'")
        filters = {column: combination[i] for i, column in enumerate(columns)}
        new_row = pandas.Series({**filters, 'file_name': output_file})
        comboname.loc[len(comboname)] = new_row
        print(f'{output_file} created with {len(filtered_df)} rows.')
        j += 1
j+=1
for value1 in unique_values[columns[0]]:
    filtered_df = df[(df[columns[0]] == value1)]
    if not filtered_df.empty:
        output_file = f'output_{j}.csv'
        filtered_df.to_csv(output_file, index=False, quotechar="'")
        new_row2=pandas.Series({columns[0]:f'{value1}','file_name':output_file})
        comboname.loc[len(comboname)] = new_row2
        print(f'{output_file} created with {len(filtered_df)} rows.')
        j += 1
# Step 5: Write the index file
output_file = 'index.csv'
comboname.to_csv(output_file, index=False,quotechar="'")

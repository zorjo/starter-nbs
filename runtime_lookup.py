import pandas
values={}
indexdf = pandas.read_csv('index.csv',quotechar="'")
cols=indexdf.columns[1:]

for x in cols:
    values[x]=input(f"Enter the {x}:")
for x,y in values.items():
    if(not y==""):
        indexdf=indexdf[indexdf[x]==y]

if(len(indexdf)>0):
    required_name=indexdf['file_name'].values[-1]
    x=" ".join(list(values.values()))
    print(f"The required filename for key '{x}' is: {required_name}")
else:
    print(f"No value found for key '{x}'.")

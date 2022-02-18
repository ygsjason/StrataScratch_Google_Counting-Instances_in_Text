# Import your libraries
import pandas as pd

# Start writing code
df1 = google_file_store.drop_duplicates()

# Creat a new col: bull
df1['bull'] = df1.contents.str.count('bull')
df1['bear'] = df1.contents.str.count('bear')

df2 = df1[['bull', 'bear']]

# sum of the each colum and append the new row to the botton of df
df2.loc[3] = df2[['bull', 'bear']].sum()

# Subset the row with the last index 
df2.loc[len(df2)-1:len(df2)]
df2[-1:]
df3 = df2[len(df2)-1:len(df2)]

# Gather columns into rows
df3.melt(var_name = 'word', value_name = 'occur')

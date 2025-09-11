import pandas as pd 
df = pd.read_csv('ticket_data.csv',encoding='latin-1') 
df = df.drop_duplicates() 
df = df.fillna(value=0) 
df1 = df.where(df['Ticket price'] == 0.0).dropna() 
print(df1.to_string())

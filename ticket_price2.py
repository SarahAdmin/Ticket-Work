import pandas as pd 
df = pd.read_csv('ticket_data.csv',encoding='latin-1') 
df = df.drop_duplicates() 
df = df.fillna(value=0) 
df2 = df.where(df['Ticket price'] == 20.0).dropna() 
print(df2.to_string())

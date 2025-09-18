import pandas as pd 
df = pd.read_csv('ticket_data.csv',encoding='latin-1') 
newDF = df.to_json('ticket_data_1.json')

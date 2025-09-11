import pandas as pd 
df = pd.read_csv('ticket_data.csv',encoding='latin-1') 
df1 = df.drop_duplicates() 
columnsToRemove = ['Order ID','Order date','COUNTIF','Phone number','Purchaser city','Purchaser state',
                  'Purchaser country','Event name','Event ID','Event start date',	'Event start time', 'Event timezone','Event location','Ticket tier','Buyer first name','Buyer last name','Buyer email','Ticket type','Currency']
newDF = df1.drop(columnsToRemove,axis=1) 
print(newDF.to_string())
                   

import pandas as pd 
df = pd.read_csv('ticket_data.csv',encoding='latin-1') 
df = df.drop_duplicates()
columnsToRemove = ['Order ID','Order date','COUNTIF','Phone number','Purchaser city','Purchaser state',
                  'Purchaser country','Event name','Event ID','Event start date',	'Event start time', 'Event timezone','Event location','Ticket tier','Buyer first name','Buyer last name','Buyer email','Ticket type','Currency','Attendee email']
df = df.drop(columnsToRemove,axis=1) 
finalDF = df.to_json('ticket_data_1.json')

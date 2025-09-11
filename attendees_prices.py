import pandas as pd 
df = pd.read_csv('ticket_data.csv',encoding='latin-1') 
df2 = df.drop_duplicates() 
columnsToRemove = ['Order ID','Order date','COUNTIF','Phone number','Purchaser city','Purchaser state',
                  'Purchaser country','Event name','Event ID','Event start date',	'Event start time', 'Event timezone','Event location','Ticket tier','Buyer first name','Buyer last name','Buyer email','Ticket type','Currency','Attendee email']
newDF = df2.drop(columnsToRemove,axis=1) 
priceTwo = newDF.where(df2['Ticket price'] == 20.0).dropna()
print(priceTwo.to_string())
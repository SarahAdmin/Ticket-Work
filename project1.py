import pandas as pd
def read_ticket_data(file_path):
  try: 
    df = pd.read_csv('ticket_data.csv',encoding='latin-1) 
    print(f'Successfully read {len(df)} rows from the file.') 
    return df 
  except FileNotFoundError: 
       print(f'Error: File is not found at path: {file_path}') 
       return None 
  except Exception as e:
    print(f'Error occurred while the reading the CSV {e}') 
    return None 
    
      
  

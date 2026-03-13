import pandas as pd
from sqlalchemy import create_engine

# CSV load karo
df = pd.read_csv('data/raw/creditcard.csv')

# Database engine create karo
engine = create_engine('sqlite:///database/fraud_data.db')

# DataFrame ko SQL table mein save karo
df.to_sql('transactions', engine, if_exists='replace', index=False)
print("Database setup successful!")
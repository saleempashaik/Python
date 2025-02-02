import pandas
import requests
import sqlalchemy

url = 'http://api.coincap.io/v2/assets'
#url = 'https://api.finra.org/data/group/registration/name/compositeindividualmock?individualCrdNumber=12345'
header={"Content-Type":"appliction/json",
        "Accept_Encoding":"deflate"}


response = requests.get(url,headers=header)
print(response)

responseData = response.json()
print(responseData)

df= pandas.json_normalize(responseData,'data')
#print(df)

engine = sqlalchemy.create_engine('mssql+pyodbc://SSP\SSP/Test?driver=SQL+Server+Native+Client+11.0')
df.to_sql(name='FactCrypto',con=engine,index=False,if_exists='fail')


import pandas as pd
import requests as req
# end_point='https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
# key_val='fd298239-ec99-44f2-8d0d-40f26a3a9d1c'
# end_point+=key_val
# print(end_point)
# response=req.get(end_point) #respons status
# data=pd.DataFrame(response.json()['data'])[['id','cmc_rank','circulating_supply']]
# print(data)
response=req.get('https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=fd298239-ec99-44f2-8d0d-40f26a3a9d1c')
temp_df=pd.DataFrame(response.json()['data'])[['id','cmc_rank','circulating_supply']]
print(temp_df)

df=temp_df.append(temp_df,ignore_index=True)
df.to_csv('currency.csv')

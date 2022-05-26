import pandas as pd
import json
from pandas import json_normalize

data = json.loads(open('user.json').read())
df = json_normalize(data) 
df = pd.DataFrame(df)
all_message = df.groupby(df.columns.tolist(),as_index=False).size()
all_message = all_message.sort_values(by=['size'],ascending=False)
all_message.to_csv('all_message.csv', index=False, sep=';')
print(all_message)

# all messages of the user who sent the same message at most
height_message_user = all_message.iloc[0:1,:]
height_message_username = height_message_user.iloc[0,0]
max_message_user = df.loc[df.username == height_message_username]
max_message_user.to_csv('max_message_user.csv', index=False, sep=';')
print(max_message_user)
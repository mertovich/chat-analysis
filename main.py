import pandas as pd
import json
from pandas import json_normalize

data = json.loads(open('user.json').read())
df = json_normalize(data) 
df = pd.DataFrame(df, columns= ['message'])
all_message = df.groupby(df.columns.tolist(),as_index=False).size()
all_message = all_message.sort_values(by=['size'],ascending=False)
all_message.to_csv('all_message.csv', index=False, sep=';')
print(all_message)
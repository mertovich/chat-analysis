from email import message
import pandas as pd
import json
from pandas import json_normalize


data = json.loads(open('user.json').read())
df = json_normalize(data) 
df = pd.DataFrame(df, columns= ['message'])
all_message = df.groupby(df.columns.tolist(),as_index=False).size()
print(all_message['message'].sort_index(ascending=False))

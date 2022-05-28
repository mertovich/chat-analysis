import pandas as pd
import json
from pandas import json_normalize
from textblob import TextBlob
import matplotlib.pyplot as plt

data = json.loads(open('user.json').read())
df = json_normalize(data) 
df = pd.DataFrame(df)

# sentiment
blob = []
with open('sentiment.txt') as f:
    blob = f.readlines()
    if len(blob) == 0:
        for text in df['message']:
            TmpBlob = TextBlob(text)
            try:
                blob_eng = TmpBlob.translate(from_lang='tr', to='en')
                print(blob_eng)
                with open('sentiment.txt', 'a+') as f:
                    f.write('{}\n'.format(blob_eng))
            except:
                pass
    else:
        pass

tmpBlob = []
for i in blob:
    tmp = i.replace('\n', '')
    tmpBlob.append(tmp)

blob = tmpBlob
print(blob)

positive = []
negative = []
neutral = []

for text in blob:
    tmp = TextBlob(text)
    tmp = tmp.sentiment.polarity
    if tmp > 0:
        positive.append(tmp)
    if tmp < 0:
        negative.append(tmp)
    else:
        neutral.append(tmp)


print(positive)
print(negative)
print(neutral)

# graph positive and negative
plt.hist([positive, negative], stacked=True, color=['g', 'r'], label=['positive', 'negative'])
plt.xlabel('Sentiment')
plt.ylabel('Number of messages')
plt.legend()
plt.show()

all_message = df.groupby(df.columns.tolist(),as_index=False).size()
all_message = all_message.sort_values(by=['size'],ascending=False)
all_message.to_csv('all_message.csv', index=False, sep=';')

# all messages of the user who sent the same message at most
height_message_user = all_message.iloc[0:1,:]
height_message_username = height_message_user.iloc[0,0]
max_message_user = df.loc[df.username == height_message_username]
max_message_user.to_csv('max_message_user.csv', index=False, sep=';')

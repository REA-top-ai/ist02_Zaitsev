from client.api_methods import get_everything
import json
from pprint import pprint

resp = get_everything('0de5f8492c0d4ddea5f736788d4c5944', q = 'apple', sortBy = 'publishedAt')
print(resp)
ctr = 0
for art in resp['articles']:
    if art['title']!=None and len(art['description'])>=50 and art['url']!= None and ctr<50:
        ctr+=1
        res = {
            'title': art['title'],
            'source': art['source'],
            'publishedAt': art['publishedAt'],
            'author': art['author']

        }
        pprint(json.dumps(res))
    if ctr>=50:
        break
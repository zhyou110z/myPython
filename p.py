import requests 
import json

data2 = {"data":{"head":{"deviceId":"1fd597ce","osType":1,"deviceRule":"2","apiVersion":"1.0.3","viewSize":"720x1280","utoken":"159.1496371085-fa8a559fa292559707439536cd62597c","channel":"Beta"}}}

encode_json = json.dumps(data2)
print (type(encode_json), encode_json)

decode_json = json.loads(encode_json)
print (type(decode_json))
print (decode_json['data'])
print (decode_json)

url2 = "http://b2b-newapi.beta1.fn/getEnv"

html = requests.post(url2,params=json.dumps(data2.get("data")))

print (html.json())
'''
count = 0
while (True):
   print ('The count is:', count)
   count = count + 1
 
'''
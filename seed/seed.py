import csv
import requests
with open('seed.csv','r') as f:
  rows = csv.reader(f)
  for row in rows:
    data = {
      "req_msg": row[0],
      "res_msg": row[1],
      "mode": 1
    }
    r = requests.post('https://hannaeae.herokuapp.com/add',json=data)
    print (r.status_code, row[0],r.text)


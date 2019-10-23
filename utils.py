import requests
import json
def get_auth():
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"
    appid = "wx9e3235b5af07f2ec"
    secret = "d19c4b897a5e83d85d1d667879ed4576"
    res = requests.get(url % (appid, secret))
    d = json.loads(res.content)
    auth = d['access_token']
    
get_auth()
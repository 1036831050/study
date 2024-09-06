import requests
from pprint import pprint

headers = {
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'Referer': 'https://www.cool18.com/bbs4/index.php?app=forum&act=threadview&tid=14408111',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.cool18.com/pub/jquery-1.11.1.min.js', headers=headers)
pprint(response.json())
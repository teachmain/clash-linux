import requests as req

bookingurl = input("input url:")
HEADER = {
        'Accept': 'application/json, text/plain, */*',
        'pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'User-Agent': 'Clash'}
original = req.get(url=bookingurl, headers=HEADER)
print(original.text)

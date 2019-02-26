import requests
import json


def main():
    same()


def same():
    r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like '
                                                                       'Mac OS X) AppleWebKit'}, timeout=9)
    print(r.status_code)
    print(r.encoding)


def callTuLing(info):
	appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
	url = ("http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info))
	req = requests.get(url)
	content = req.text
	data = json.loads(content)
	answer = data['text']
	return answer

if __name__ == '__main__':
	# main()
	print(callTuLing("真的吗"))

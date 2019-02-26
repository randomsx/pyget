import chardet
import itchat
import random
import json
import requests

'''
1. 发送二十条消息后询问是否召唤主人
2. 询问是否开启对话模式
3. 询问是否想看你自己
'''

xId = '@ee9e2d8d20d9ea4a9865a0fd2a64f56aa68d7bd28acb35512bd79872480df523'
apikey = 'b6a58939dedb48838ec6852e61756929'
msg_count = 0
CLAA_ME_NUMBER = 5
callmeFlag = False
close_flag = False
open_tuling = False
ziji='<?xml version="1.0"?>\n<msg>\n\t<appmsg appid="" sdkver="0">\n\t\t<title />\n\t\t<des />\n\t\t<action />\n\t\t<type>8</type>\n\t\t<showtype>0</showtype>\n\t\t<soundtype>0</soundtype>\n\t\t<mediatagname />\n\t\t<messageext />\n\t\t<messageaction />\n\t\t<content />\n\t\t<contentattr>0</contentattr>\n\t\t<url />\n\t\t<lowurl />\n\t\t<dataurl />\n\t\t<lowdataurl />\n\t\t<appattach>\n\t\t\t<totallen>215714</totallen>\n\t\t\t<attachid>0:0:25b08cf23ebaa033e8900123142e9ffc</attachid>\n\t\t\t<emoticonmd5>25b08cf23ebaa033e8900123142e9ffc</emoticonmd5>\n\t\t\t<fileext>pic</fileext>\n\t\t\t<cdnthumbaeskey>7968636c657479726d6a736677797569</cdnthumbaeskey>\n\t\t\t<aeskey />\n\t\t\t<cdnthumburl>3064020100045d305b02010002044f04d66902033d11fd0204b3e2e26502045c61702a0436313533333035323833385f313734333438363437365f31313831383232633831323733376234643532636261663864303830346362380204010400030201000400</cdnthumburl>\n\t\t\t<cdnthumblength>14288</cdnthumblength>\n\t\t\t<cdnthumbwidth>300</cdnthumbwidth>\n\t\t\t<cdnthumbheight>300</cdnthumbheight>\n\t\t\t<cdnthumbmd5>1181822c812737b4d52cbaf8d0804cb8</cdnthumbmd5>\n\t\t</appattach>\n\t\t<extinfo />\n\t\t<sourceusername />\n\t\t<sourcedisplayname />\n\t\t<thumburl />\n\t\t<md5 />\n\t\t<statextstr />\n\t</appmsg>\n\t<fromusername></fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>1</version>\n\t\t<appname></appname>\n\t</appinfo>\n\t<commenturl></commenturl>\n</msg>\n'


def callMe():
	global close_flag
	itchat.send(u'正在召唤主人,请稍后...')
	close_flag = True

def callTuLing(info):
	global open_tuling
	if info == '关闭闲聊模式':
		open_tuling = False
		return

	appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
	url = ("http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info))
	req = requests.get(url)
	content = req.text
	data = json.loads(content)
	answer = data['text']
	return answer

def main():
    j = chardet.detect(b'Hello, X_X')
    print(j)

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
	global msg_count
	global open_tuling
	global callmeFlag
	global close_flag

	if msg['FromUserName'] == xId:
		if close_flag:
			return

		msg_count = msg_count + 1
		talk = msg['Text']
		print('仙儿发来了一条消息： ' + talk)

		if msg_count == 1:
			itchat.send(u'你可以选择开启闲聊模式,或者什么都不做[捂脸]', xId)
			return

		if open_tuling:
			itchat.send(callTuLing(talk), xId)
			return

		if callmeFlag == True:
			if not(talk.find("不")==-1 or talk.find("否")==-1):
				callMe()
				return
			callmeFlag = False

		if talk == '晚安':
			itchat.send(u'晚安哦~', msg['FromUserName'])

		if talk == '😂':
			itchat.send(u'[捂脸]', msg['FromUserName'])

		if talk == '看灰机':
			# todo: print huiji
			itchat.send(u'哼! 不给你看', msg['FromUserName'])

		if talk == '看自己':
			# TODO: print gif
			itchat.send(u'哼! 不给你看', msg['FromUserName'])

		if talk == '哈哈哈':
			itchat.send(u'哈哈哈哈',msg['FromUserName'])

		if talk == '召唤主人':
			callMe()
			return

		if talk == '开启闲聊模式':
			open_tuling = True
			return

		if talk == '召唤小助手':
			itchat.send(u'小助手已经上线了哦',msg['FromUserName'])


		if msg_count >= CLAA_ME_NUMBER:
			itchat.send(u'尊敬的小仙仙,如果累感到无聊,在这里可以召唤主人哦[调皮]')
			callmeFlag = True
		# itchat.send(u'我是邪恶的小助手,请来掠我吧~~', msg['FromUserName'])
	else:
		print("其他人发来了一条消息：")
		print('fron' + msg['FromUserName'])
		print(msg['Text'])
		itchat.send(msg['Text'], 'filehelper')
		itchat.send('😂', 'filehelper')

	print(msg) 

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def print_pic(msg):
	print('GET PIC')
	# print(msg)
	# itchat.send(ziji, 'filehelper')
	# itchat.send()
	# author = itchat.search_friends(name='仙儿')[0]
	# print('+++++++++++++++')
	# print(author['UserName'])
	# itchat.send(u'test', author['UserName'])
	# itchat.send('😂', 'filehelper')
	
	itchat.send(u'仙儿,你发送的消息类型太高级啦[捂脸]', xId)

	num = random.randint(1,3)
	if num == 1:
		itchat.send(u'告诉你个秘密,开启闲聊模式可以获取更多哦[奸笑]', xId)
	elif num == 2:
		itchat.send(u'告诉你个秘密,输入看灰机有惊喜哦[奸笑]', xId)
	else:
		itchat.send(u'告诉你个秘密,输入看自己有惊喜哦[奸笑]', xId)
	
	# print(msg)

def print_start():
	print('start!')
	itchat.send(u'可爱的小仙仙,过来玩你的定制游戏吧[愉快]', 'filehelper')

if __name__ == '__main__':
    # main()
    # itchat.auto_login()
	itchat.auto_login(hotReload=True)
	itchat.run()
import itchat
import requests

itchat.auto_login(hotReload=True)
friendList = itchat.get_friends(update=True)
for friend in friendList:
    if friend['NickName'] in ['Sawyer']:
        msg = auto_chat_tuling('讲个笑话')
        itchat.send(msg= msg,toUserName=friend['UserName'])


def auto_chat_tuling(msg):
    apiKey = 'b2e008b19d5e4acb93c87a4588e967f3'
    # apiKey = '1107d5601866433dba9599fac1bc0083'
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': apiKey,  # 如果这个Tuling Key不能用，那就换一个
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

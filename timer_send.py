import itchat
from app import text_reply
itchat.auto_login(hotReload=True)
friendList = itchat.get_friends(update=True)
for friend in friendList:
    if friend['NickName'] in ['Sawyer']:
        text_reply('早上好')


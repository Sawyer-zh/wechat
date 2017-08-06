import itchat

itchat.auto_login(hotReload=True)
friendList = itchat.get_friends(update=True)
for friend in friendList:
    print (friend['NickName'], friend['UserName'])
    print(friend)
    break
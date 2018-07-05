#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cd project
# python3 -m venv venv
# . venv/bin/activate
# pip install itchat
import codecs
import itchat
from itchat.content import *

# 群名称
chat_room_name = u'Taro 开发交流 2⃣️ 群'


# 添加好友并邀请进群
@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    print('userid: ', msg['RecommendInfo']['UserName'], msg['Text'])
    nick_name = msg['Text']['autoUpdate']['NickName']
    log_user(nick_name)
    itchat.add_member_into_chatroom(
        get_group_id(chat_room_name),
        [{'UserName': msg['RecommendInfo']['UserName']}],
        useInvitation=False
    )
    itchat.send_msg(u'感谢关注Taro，正在火速拉你入群！', msg['FromUserName'])


# 回复消息加群，则发送邀请进群
@itchat.msg_register([TEXT])
def on_reply_invite(msg):
    text = msg['Content']
    if text.strip().lower() == u'taro':
        print('userid: ', msg['FromUserName'], msg)
        itchat.add_member_into_chatroom(
            get_group_id(chat_room_name),
            [{'UserName': msg['FromUserName']}],
            useInvitation=False
        )
        itchat.send_msg(u'感谢关注Taro，正在火速拉你入群！', msg['FromUserName'])
        # itchat.send_raw_msg(49, chat_room_name, msg['FromUserName'])


# 获取群聊ID
def get_group_id(group_name):
    group_list = itchat.search_chatrooms(name=group_name)
    print('chatroomid: ', group_list[0]['UserName'])
    return group_list[0]['UserName']
    # return itchat.update_chatroom()


def log_user(user_name):
    filename = 'user.txt'
    open(filename, 'a')
    with codecs.open(filename, 'r', 'utf8') as original:
        data = original.read()
    with codecs.open(filename, 'w', 'utf8') as modified:
        modified.write(user_name + "\n" + data)


#itchat.auto_login(hotReload=True, enableCmdQR=True)
itchat.auto_login(hotReload=True)

itchat.run(True)

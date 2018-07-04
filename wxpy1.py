from wxpy import *
bot = Bot()


chat_room_name = 'Taro 开发交流 2⃣️ 群'

# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

'''
验证信息
'''
def valid_msg(msg):
    return '运维密码' in msg.text.lower()

'''
定义邀请用户的方法
'''
def invite(user):
    group = bot.groups().search(chat_room_name)
    group[0].add_members(user, use_invitation=True)

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')

@bot.register(msg_types=TEXT)
def just_print(msg):
    # 打印消息
    print(msg)

embed()
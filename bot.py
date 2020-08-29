from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.application.message.elements.internal import Plain
from graia.application.friend import Friend
from graia.application.group import Group, Member

from NMSLClass import NMSL
import logging

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:9223",  # 填入 httpapi 服务运行的地址
        authKey="authKey",  # 填入 authKey
        account=QQ,  # 你的机器人的 qq 号
        websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)

ZC = NMSL()


@bcc.receiver("TempMessage")
async def temp_message_handler(app: GraiaMiraiApplication, message: MessageChain, group: Group, member: Member):
    if message.asDisplay().startswith("nmsl"):
        await
        app.sendTempMessage(group, member, MessageChain(__root__=[
            Plain(ZC.get())
        ]))


@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, message: MessageChain, friend: Friend):
    if message.asDisplay().startswith("nmsl"):
        await
        app.sendFriendMessage(friend, MessageChain(__root__=[
            Plain(ZC.get())
        ]))


app.launch_blocking()

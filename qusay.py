import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

# -

qusay1.start()
qusay2.start()
qusay3.start()
qusay4.start()
qusay5.start()


c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@Gt_BoT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5864082310]


async def join_channel():
    try:
        await qusay(JoinChannelRequest("@f_c_a"))
    except BaseException:
        pass


@qusay1.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay1(JoinChannelRequest("@d3boot_7"))
    except BaseException:
        pass
        
        
@qusay1.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay1(JoinChannelRequest("@DzDDDD"))
    except BaseException:
        pass
        
@qusay1.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay1(JoinChannelRequest("@G_3_I"))
    except BaseException:
        pass
        
@qusay1.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay1(JoinChannelRequest("@d6dd60"))
    except BaseException:
        pass
        
@qusay1.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay1(JoinChannelRequest("@F_C_A"))
    except BaseException:
        pass
        
@qusay1.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay1(JoinChannelRequest("@botbillion"))
    except BaseException:
        pass
        
        
@qusay1.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay1(JoinChannelRequest("@fvvvv"))
    except BaseException:
        pass

@qusay2.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay2(JoinChannelRequest("@d3boot_7"))
    except BaseException:
        pass

    
@qusay2.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay2(JoinChannelRequest("@DzDDDD"))
    except BaseException:
        pass

        

@qusay2.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay2(JoinChannelRequest("@botbillion"))
    except BaseException:
        pass

        

        

@qusay2.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay2(JoinChannelRequest("@fvvvv"))
    except BaseException:
        pass
        
@qusay2.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay2(JoinChannelRequest("@G_3_I"))
    except BaseException:
        pass
        
@qusay2.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay2(JoinChannelRequest("@d6dd60"))
    except BaseException:
        pass
        
@qusay2.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay2(JoinChannelRequest("@F_C_A"))
    except BaseException:
        pass
        
@qusay3.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay3(JoinChannelRequest("@d3boot_7"))
    except BaseException:
        pass
        
        
@qusay3.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay3(JoinChannelRequest("@DzDDDD"))
    except BaseException:
        pass
        
@qusay3.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay3(JoinChannelRequest("@botbillion"))
    except BaseException:
        pass
        
        
@qusay3.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay3(JoinChannelRequest("@fvvvv"))
    except BaseException:
        pass
        
@qusay3.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay3(JoinChannelRequest("@G_3_I"))
    except BaseException:
        pass
        
@qusay3.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay3(JoinChannelRequest("@d6dd60"))
    except BaseException:
        pass
        
@qusay3.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay3(JoinChannelRequest("@F_C_A"))
    except BaseException:
        pass


@qusay4.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay4(JoinChannelRequest("@d3boot_7"))
    except BaseException:
        pass

        

        

@qusay4.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay4(JoinChannelRequest("@DzDDDD"))
    except BaseException:
        pass

        

@qusay4.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay4(JoinChannelRequest("@botbillion"))
    except BaseException:
        pass

        

        

@qusay4.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay4(JoinChannelRequest("@fvvvv"))
    except BaseException:
        pass
        
@qusay4.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay4(JoinChannelRequest("@G_3_I"))
    except BaseException:
        pass
        
@qusay4.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay4(JoinChannelRequest("@d6dd60"))
    except BaseException:
        pass
        
@qusay4.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay4(JoinChannelRequest("@F_C_A"))
    except BaseException:
        pass
        
@qusay5.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay5(JoinChannelRequest("@d3boot_7"))
    except BaseException:
        pass

        

        

@qusay5.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay5(JoinChannelRequest("@DzDDDD"))
    except BaseException:
        pass

        

@qusay5.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay5(JoinChannelRequest("@botbillion"))
    except BaseException:
        pass

        

        

@qusay5.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay5(JoinChannelRequest("@fvvvv"))
    except BaseException:
        pass
        
@qusay5.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay5(JoinChannelRequest("@G_3_I"))
    except BaseException:
        pass
        
@qusay5.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay5(JoinChannelRequest("@d6dd60"))
    except BaseException:
        pass
        
@qusay5.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay5(JoinChannelRequest("@F_C_A"))
    except BaseException:
        pass
        
        
@qusay1.on(events.NewMessage(outgoing=False, pattern='/QUSAY'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سورس قــصــي يعمل سيدي 🔥📎**')

@qusay2.on(events.NewMessage(outgoing=False, pattern='/QUSAY'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سورس قــصــي يعمل سيدي 🔥📎**')


@qusay3.on(events.NewMessage(outgoing=False, pattern='/QUSAY'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سورس قــصــي يعمل سيدي 🔥📎**')


@qusay4.on(events.NewMessage(outgoing=False, pattern='/QUSAY'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سورس قــصــي يعمل سيدي 🔥📎**')

@qusay5.on(events.NewMessage(outgoing=False, pattern='/QUSAY'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سورس قــصــي يعمل سيدي 🔥📎**')
        
@qusay1.on(events.NewMessage(outgoing=False, pattern='قــصــي'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**احـتـرامـﮯ ٱيـهـا آلـرئـيـس 🙋‍**')

@qusay2.on(events.NewMessage(outgoing=False, pattern='قــصــي'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**احـتـرامـﮯ ٱيـهـا آلـرئـيـس 🙋‍**')


@qusay3.on(events.NewMessage(outgoing=False, pattern='قــصــي'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**احـتـرامـﮯ ٱيـهـا آلـرئـيـس 🙋‍**')


@qusay4.on(events.NewMessage(outgoing=False, pattern='قــصــي'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**احـتـرامـﮯ ٱيـهـا آلـرئـيـس 🙋‍**')

@qusay5.on(events.NewMessage(outgoing=False, pattern='قــصــي'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**احـتـرامـﮯ ٱيـهـا آلـرئـيـس 🙋‍**')

@qusay1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")

@qusay2.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")

@qusay3.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")


@qusay4.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")

@qusay5.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")





@qusay1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")


@qusay2.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")


@qusay3.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")

@qusay4.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")


@qusay5.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**❀ اوامر التجميع الجماعي 👑

• قم بعمل كروب خاص وقم بإضافة جميع الارقام واضافة حساب المطور وخلي ملكية الكروب لحساب المطور وشوف هاي الاوامر
• @ZMMBOT - `/billion`
• @GT_BoT - `/bareq`
• @MARKTEBOT - `/oqab`
• @XNSEX21BOT - `/arab`
• SEND - `/QUSAY`


❀ اوامر التجميع الفردي 👍

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل البرق - `.تجميع البرق`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")

@qusay1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝚀𝚄𝚂𝙰𝚈⌯──╮

※ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 -  𝙵_𝙲_𝙰    ※

※ 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 - 𝟭.𝟬 - 𝚁𝙴𝚅𝙸𝚂𝙴𝙳   ※

※ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 - 𝚀𝚄𝚂𝙰𝚈.𝚆𝙰  ※

╰───⌯𝚀𝚄𝚂𝙰𝚈 𝙿𝙾𝙸𝙽𝚃⌯───╯
''')

@qusay1.on(events.NewMessage(outgoing=False, pattern='/billion'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay1.get_entity(bot_username)
        await qusay1.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay1.get_entity(bot_username)
        await qusay1.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay1.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay1.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay1(ImportChatInviteRequest(bott))
                msg2 = await qusay1.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay1.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@qusay1.on(events.NewMessage(outgoing=False, pattern='/bareq'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay1.get_entity(bot_usernamee)
        await qusay1.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay1.get_entity(bot_usernamee)
        await qusay1.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay1.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay1.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay1(ImportChatInviteRequest(bott))
                msg2 = await qusay1.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay1.send_message(event.chat_id, "تم الانتهاء من التجميع !")
      
  
@qusay1.on(events.NewMessage(outgoing=False, pattern='/oqab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay1.get_entity(bot_usernameee)
        await qusay1.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay1.get_entity(bot_usernameee)
        await qusay1.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay1.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay1.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay1(ImportChatInviteRequest(bott))
                msg2 = await qusay1.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay1.on(events.NewMessage(outgoing=False, pattern='/arab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay1.get_entity(bot_usernameeee)
        await qusay1.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay1.get_entity(bot_usernameeee)
        await qusay1.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay1.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay1.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay1(ImportChatInviteRequest(bott))
                msg2 = await qusay1.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay1.get_entity(bot_username)
        await qusay1.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay1.get_entity(bot_username)
        await qusay1.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay1.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay1.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay1(ImportChatInviteRequest(bott))
                msg2 = await qusay1.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع البرق"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay1.get_entity(bot_usernamee)
        await qusay1.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay1.get_entity(bot_usernamee)
        await qusay1.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay1.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay1.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay1(ImportChatInviteRequest(bott))
                msg2 = await qusay1.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay1.get_entity(bot_usernameeee)
        await qusay1.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay1.get_entity(bot_usernameeee)
        await qusay1.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay1.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay1.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay1(ImportChatInviteRequest(bott))
                msg2 = await qusay1.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay1.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@qusay1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay1.get_entity(bot_usernameee)
        await qusay1.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay1.get_entity(bot_usernameee)
        await qusay1.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay1.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay1.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay1(ImportChatInviteRequest(bott))
                msg2 = await qusay1.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay1.send_message(event.chat_id, "تم الانتهاء من التجميع !")



##########################################

@qusay2.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝚀𝚄𝚂𝙰𝚈⌯──╮

※ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 -  𝙵_𝙲_𝙰    ※

※ 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 - 𝟭.𝟬 - 𝚁𝙴𝚅𝙸𝚂𝙴𝙳   ※

※ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 - 𝚀𝚄𝚂𝙰𝚈.𝚆𝙰  ※

╰───⌯𝚀𝚄𝚂𝙰𝚈 𝙿𝙾𝙸𝙽𝚃⌯───╯
''')

@qusay2.on(events.NewMessage(outgoing=False, pattern='/billion'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay2.get_entity(bot_username)
        await qusay2.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay2.get_entity(bot_username)
        await qusay2.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay2.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay2.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay2(ImportChatInviteRequest(bott))
                msg2 = await qusay2.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay2.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@qusay2.on(events.NewMessage(outgoing=False, pattern='/bareq'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay2.get_entity(bot_usernamee)
        await qusay2.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay2.get_entity(bot_usernamee)
        await qusay2.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay2.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay2.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay2(ImportChatInviteRequest(bott))
                msg2 = await qusay2.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay2.send_message(event.chat_id, "تم الانتهاء من التجميع !")
      
  
@qusay2.on(events.NewMessage(outgoing=False, pattern='/oqab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay2.get_entity(bot_usernameee)
        await qusay2.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay2.get_entity(bot_usernamee)
        await qusay2.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay2.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay2.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay2(ImportChatInviteRequest(bott))
                msg2 = await qusay2.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay2.on(events.NewMessage(outgoing=False, pattern='/arab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay2.get_entity(bot_usernameeee)
        await qusay2.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay2.get_entity(bot_usernameeee)
        await qusay2.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay2.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay2.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay2(ImportChatInviteRequest(bott))
                msg2 = await qusay2.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay2.get_entity(bot_username)
        await qusay2.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay2.get_entity(bot_username)
        await qusay2.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay2.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay2.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay2(ImportChatInviteRequest(bott))
                msg2 = await qusay2.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع البرق"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay2.get_entity(bot_usernamee)
        await qusay2.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay2.get_entity(bot_usernamee)
        await qusay2.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay2.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay2.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay2(ImportChatInviteRequest(bott))
                msg2 = await qusay2.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay2.get_entity(bot_usernameeee)
        await qusay2.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay2.get_entity(bot_usernameeee)
        await qusay2.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay2.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay2.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay2(ImportChatInviteRequest(bott))
                msg2 = await qusay2.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay2.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@qusay2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay2.get_entity(bot_usernameee)
        await qusay2.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay2.get_entity(bot_usernameee)
        await qusay2.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay2.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay2.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay2(ImportChatInviteRequest(bott))
                msg2 = await qusay2.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay2.send_message(event.chat_id, "تم الانتهاء من التجميع !")




##########################################

@qusay3.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝚀𝚄𝚂𝙰𝚈⌯──╮

※ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 -  𝙵_𝙲_𝙰    ※

※ 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 - 𝟭.𝟬 - 𝚁𝙴𝚅𝙸𝚂𝙴𝙳   ※

※ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 - 𝚀𝚄𝚂𝙰𝚈.𝚆𝙰  ※

╰───⌯𝚀𝚄𝚂𝙰𝚈 𝙿𝙾𝙸𝙽𝚃⌯───╯
''')

@qusay3.on(events.NewMessage(outgoing=False, pattern='/billion'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay3.get_entity(bot_username)
        await qusay3.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay3.get_entity(bot_username)
        await qusay3.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay3.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay3.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay3(ImportChatInviteRequest(bott))
                msg2 = await qusay3.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay3.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@qusay3.on(events.NewMessage(outgoing=False, pattern='/bareq'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay3.get_entity(bot_usernamee)
        await qusay3.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay3.get_entity(bot_usernamee)
        await qusay3.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay3.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay3.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay3(ImportChatInviteRequest(bott))
                msg2 = await qusay3.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay3.send_message(event.chat_id, "تم الانتهاء من التجميع !")
        
@qusay3.on(events.NewMessage(outgoing=False, pattern='/oqab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay3.get_entity(bot_usernameee)
        await qusay3.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay3.get_entity(bot_usernameee)
        await qusay3.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay3.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay3.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay3(ImportChatInviteRequest(bott))
                msg2 = await qusay3.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay3.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay3.on(events.NewMessage(outgoing=False, pattern='/arab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay3.get_entity(bot_usernameeee)
        await qusay3.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay3.get_entity(bot_usernameeee)
        await qusay3.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay3.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay3.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay3(ImportChatInviteRequest(bott))
                msg2 = await qusay3.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay3.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay3.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay3.get_entity(bot_username)
        await qusay3.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay3.get_entity(bot_username)
        await qusay3.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay3.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay3.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay3(ImportChatInviteRequest(bott))
                msg2 = await qusay3.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay3.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay3.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع البرق"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay3.get_entity(bot_usernamee)
        await qusay3.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay3.get_entity(bot_usernamee)
        await qusay3.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay3.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay3.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay3(ImportChatInviteRequest(bott))
                msg2 = await qusay3.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay3.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay3.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay3.get_entity(bot_usernameeee)
        await qusay3.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay3.get_entity(bot_usernameeee)
        await qusay3.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay3.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay3.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay3(ImportChatInviteRequest(bott))
                msg2 = await qusay3.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay3.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@qusay3.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay3.get_entity(bot_usernameee)
        await qusay3.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay3.get_entity(bot_usernameee)
        await qusay3.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay3.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay3.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay3(ImportChatInviteRequest(bott))
                msg2 = await qusay3.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay3.send_message(event.chat_id, "تم الانتهاء من التجميع !")




##########################################

@qusay4.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝚀𝚄𝚂𝙰𝚈⌯──╮

※ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 -  𝙵_𝙲_𝙰    ※

※ 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 - 𝟭.𝟬 - 𝚁𝙴𝚅𝙸𝚂𝙴𝙳   ※

※ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 - 𝚀𝚄𝚂𝙰𝚈.𝚆𝙰  ※

╰───⌯𝚀𝚄𝚂𝙰𝚈 𝙿𝙾𝙸𝙽𝚃⌯───╯
''')

@qusay4.on(events.NewMessage(outgoing=False, pattern='/billion'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay4.get_entity(bot_username)
        await qusay4.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay4.get_entity(bot_username)
        await qusay4.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay4.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay4.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay4(ImportChatInviteRequest(bott))
                msg2 = await qusay4.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay4.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@qusay4.on(events.NewMessage(outgoing=False, pattern='/bareq'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay4.get_entity(bot_usernamee)
        await qusay4.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay4.get_entity(bot_usernamee)
        await qusay4.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay4.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay4.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay4(ImportChatInviteRequest(bott))
                msg2 = await qusay4.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay4.send_message(event.chat_id, "تم الانتهاء من التجميع !")
        
@qusay4.on(events.NewMessage(outgoing=False, pattern='/oqab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay4.get_entity(bot_usernameee)
        await qusay4.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay4.get_entity(bot_usernameee)
        await qusay4.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay4.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay4.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay4(ImportChatInviteRequest(bott))
                msg2 = await qusay4.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay4.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay4.on(events.NewMessage(outgoing=False, pattern='/arab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay4.get_entity(bot_usernameeee)
        await qusay4.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay4.get_entity(bot_usernameeee)
        await qusay4.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay4.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay4.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay4(ImportChatInviteRequest(bott))
                msg2 = await qusay4.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay4.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay4.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay4.get_entity(bot_username)
        await qusay4.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay4.get_entity(bot_username)
        await qusay4.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay4.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay4.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay4(ImportChatInviteRequest(bott))
                msg2 = await qusay4.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay4.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay4.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع البرق"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay4.get_entity(bot_usernamee)
        await qusay4.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay4.get_entity(bot_usernamee)
        await qusay4.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay4.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay4.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay4(ImportChatInviteRequest(bott))
                msg2 = await qusay4.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay4.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay4.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay4.get_entity(bot_usernameeee)
        await qusay4.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay4.get_entity(bot_usernameeee)
        await qusay4.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay4.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay4.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay4(ImportChatInviteRequest(bott))
                msg2 = await qusay4.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay4.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@qusay4.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay4.get_entity(bot_usernameee)
        await qusay4.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay4.get_entity(bot_usernameee)
        await qusay4.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay4.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay4.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay4(ImportChatInviteRequest(bott))
                msg2 = await qusay4.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay4.send_message(event.chat_id, "تم الانتهاء من التجميع !")




##########################################

@qusay5.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝚀𝚄𝚂𝙰𝚈⌯──╮

※ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 -  𝙵_𝙲_𝙰    ※

※ 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 - 𝟭.𝟬 - 𝚁𝙴𝚅𝙸𝚂𝙴𝙳   ※

※ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 - 𝚀𝚄𝚂𝙰𝚈.𝚆𝙰  ※

╰───⌯𝚀𝚄𝚂𝙰𝚈 𝙿𝙾𝙸𝙽𝚃⌯───╯
''')

@qusay5.on(events.NewMessage(outgoing=False, pattern='/billion'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay5.get_entity(bot_username)
        await qusay5.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay5.get_entity(bot_username)
        await qusay5.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay5.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay5.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay5(ImportChatInviteRequest(bott))
                msg2 = await qusay5.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay5.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@qusay5.on(events.NewMessage(outgoing=False, pattern='/bareq'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay5.get_entity(bot_usernamee)
        await qusay5.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay5.get_entity(bot_usernamee)
        await qusay5.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay5.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay5.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay5(ImportChatInviteRequest(bott))
                msg2 = await qusay5.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay5.send_message(event.chat_id, "تم الانتهاء من التجميع !")
        
@qusay5.on(events.NewMessage(outgoing=False, pattern='/oqab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay5.get_entity(bot_usernameee)
        await qusay5.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay5.get_entity(bot_usernameee)
        await qusay5.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay5.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay5.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay5(ImportChatInviteRequest(bott))
                msg2 = await qusay5.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay5.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay5.on(events.NewMessage(outgoing=False, pattern='/arab'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay5.get_entity(bot_usernameeee)
        await qusay5.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay5.get_entity(bot_usernameeee)
        await qusay5.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay5.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay5.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay5(ImportChatInviteRequest(bott))
                msg2 = await qusay5.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay5.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@qusay5.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay5.get_entity(bot_username)
        await qusay5.send_message('@zmmbot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay5.get_entity(bot_username)
        await qusay5.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay5.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay5.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay5(ImportChatInviteRequest(bott))
                msg2 = await qusay5.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay5.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay5.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع البرق"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay5.get_entity(bot_usernamee)
        await qusay5.send_message('@Gt_BoT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay5.get_entity(bot_usernamee)
        await qusay5.send_message('@Gt_BoT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay5.get_messages('@Gt_BoT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay5.get_messages('@Gt_BoT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay5(ImportChatInviteRequest(bott))
                msg2 = await qusay5.get_messages('@Gt_BoT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay5.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@qusay5.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay5.get_entity(bot_usernameeee)
        await qusay5.send_message('@xnsex21bot', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay5.get_entity(bot_usernameeee)
        await qusay5.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay5.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay5.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay5(ImportChatInviteRequest(bott))
                msg2 = await qusay5.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay5.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@qusay5.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await qusay5.get_entity(bot_usernameee)
        await qusay5.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | QuSaY ThX')
        channel_entity = await qusay5.get_entity(bot_usernameee)
        await qusay5.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await qusay5.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await qusay5.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await qusay5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | ThX")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay5(ImportChatInviteRequest(bott))
                msg2 = await qusay5.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await qusay5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await qusay5.send_message(event.chat_id, "تم الانتهاء من التجميع !")



##########################################

print("💠 qusay Userbot Running 💠")
qusay1.run_until_disconnected()
qusay2.run_until_disconnected()
qusay3.run_until_disconnected()
qusay4.run_until_disconnected()
qusay5.run_until_disconnected()

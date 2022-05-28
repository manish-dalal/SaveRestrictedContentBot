#Github.com/Vasusen-code

import time, os
import re

from .. import bot as Drone
from .. import userbot, Bot
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_msg
from main.plugins.helpers import get_link, join, screenshot

from telethon import events

from ethon.telefunc import force_sub

ft = f"To use this bot you've to join @{fs}."

message = "Send me the message link you want to start saving from, as a reply to this message."
          
# To-Do:
# Make these codes shorter and clean
# ofc will never do it. 

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    # s, r = await force_sub(event.client, fs, event.sender_id, ft)
    # if s == True:
    #     await event.reply(r)
    #     return

    list_string = event.message.message.splitlines()
    ml_string = ' \n'.join(list_string)
    new_ml_string = list(map(str, ml_string.split(" ")))

    new_join_str = " ".join(new_ml_string)

    urls = re.findall(r'(https?://[^\s]+)', new_join_str)
    u_len = len(urls)

    for j in range(u_len):
        new_link = urls[j]
        edit = await event.reply("Processing!")

        print("new_link", new_link)
        if 't.me/+' in new_link:
            q = await join(userbot, new_link)
            await edit.edit(q)
            return 
        if 't.me/' in new_link:
            await get_msg(userbot, Bot, event.sender_id, edit.id, new_link, 0)        

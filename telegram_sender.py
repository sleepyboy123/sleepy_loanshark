from secrets import *

import asyncio
from datetime import datetime
import sys
from telethon import TelegramClient
from telethon.sessions import StringSession

application = sys.argv[1]

chase_users = ["tanzyzy", "vcwd96", "sleepyboy123"]

current_month = datetime.now().strftime("%B")

application_cost_dict = {"youtube": 18}
application_cost = application_cost_dict[application] / len(chase_users)

async def main():
    async with TelegramClient(StringSession(string_session), api_id, api_hash) as client:
        for user in chase_users:
            await client.send_message(user, "Hello, this is an automated reminder to transfer ${} to Matthew Tan for the {} {} subscription. Thanks!".format(application_cost, current_month, application))
        await client.send_message("me", "Hello, the automated reminders has been sent out for {} {} subscription".format(current_month, application))

asyncio.run(main())

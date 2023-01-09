import config
from pyrogram import Client
import time


#--set---#

#---bot---#
bot = Client(
    name = "xui",
    api_id = user_api_id,
    api_hash = user_api_hash,
    bot_token = user_bot_token
    
)

@bot.on_message()
async def test(Client , message):
    await bot.send_document(user_pv_id, user_path_file, caption=time.strftime("%Y/%m/%d\n%H:%M:%S\nNew BackUp", time.localtime()))


bot.run()


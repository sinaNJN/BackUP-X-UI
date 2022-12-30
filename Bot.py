from pyrogram import Client
import time

#--set---#

user_api_id = input('set api id: ')
user_api_hash = input('set api hash : ')
user_bot_token = input('set bot token : ')
user_pv_id = input('set your Id(usernumber) : ')
user_path_file = input('set (x-ui.db) path : ')

#---bot---#
bot = Client(
    name = "sina",
    api_id = user_api_id,
    api_hash = user_api_hash,
    bot_token = user_bot_token
    
)

@bot.on_message()
async def test(Client , message):
    await bot.send_document(user_pv_id, user_path_file, caption=time.strftime("%Y/%m/%d\n%H:%M:%S\nNew BackUp\n@DeviceOS", time.localtime()))


bot.run()


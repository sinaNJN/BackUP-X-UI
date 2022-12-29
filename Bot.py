from pyrogram import Client

bot = Client(
    session_name = "xui" ,
    api_id = 1110329,
    api_hash = "b90f31f3765a434904767080a25db99a",
    bot_token = '774065700:AAGl_JH0aXzqjUjUxRDvFodPNGI4ASB1PrE'
    
)

@bot.on_message()
async def test(Client , message):
    await bot.send_message(message.chat.id , 'hello world')


bot.run()

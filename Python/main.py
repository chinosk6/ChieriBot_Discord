import discord
import sys
import os
import ctypes


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        global dll
        dll=ctypes.windll.LoadLibrary("C:\\Users\\Administrator\\Desktop\\discordbot\\Chieri_main.dll")#引用易语言dll
        manage = dll.message_main
        userid=str(message.author.id)
        para=ctypes.c_char_p(manage(message.content.encode('gbk'),userid.encode('gbk')))
        result=para.value
        retmsg=str(result,'utf8')

        if retmsg=='chieri_pass':
            return
        else:
            if retmsg[0:4]!='pic=':
                await message.reply(retmsg, mention_author=True)
            else: 
                channel = message.channel
                #print(channel)
                await channel.send(file=discord.File(retmsg[4:]))

        print(str(message.author.id) + ':' + message.content)

   

client = MyClient()
client.run('token')

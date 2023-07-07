import discord
from discord.ext import commands


"""Dicord uses 'intents' as a group of pre defined web socket events which the discord.js client recieves. Theses groups are then sent to the app."""


intents = discord.Intents.default() #calling the default events
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


"""Instantiating commands"""

@bot.event #calling the bot
async def on_ready():
    print(f'Bot is online!')


@bot.event
async def on_message(message):
    if 'espresso' in message.content.lower():
        corrected_content = message.content.replace('espresso', 'expresso', -1)
        await message.channel.send(f'{message.author} meant to say: {corrected_content}')

    await bot.process_commands(message)



bot.run('MTEyNjY5ODI0MjczMDYzNTMzNA.G8UGYQ.UBcIYuG59mDIMYcyQcpcPjtAs1nW6EBEijZX0A')

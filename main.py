import discord
from discord.ext import commands
import re
import os
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


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
    corrected_content = re.sub(r'(?i)\bespresso\b', lambda match: match.group().capitalize(), message.content)
    if corrected_content != message.content:
        await message.channel.send(f'{message.author} meant to say: {corrected_content}')

    await bot.process_commands(message)



bot.run(DISCORD_TOKEN)

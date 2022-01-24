import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(
        f'{client.user} is connected to the following guild:\n'
    )

@client.event
async def on_guild_join(GUILD):
    print(f'{client.user} has joined {GUILD.name} owned by {GUILD.owner_id}!')

@client.event
async def on_message(message):
    if message.content.startswith("!"):
        await passFilter(message)

async def passFilter(message):
    messageContent = message.content
    channel = message.channel
    if messageContent.startswith("!fuckyou") or messageContent.startswith("!fuck you"):
        await channel.send("fuck you too asshole")
    if messageContent.startswith("!join"):
        await joinChannel(message)
    if messageContent.startswith("!leave"):
        await leaveChannel()

async def joinChannel(message):
    author = message.author
    channel = author.voice.channel
    if channel:
        VoiceClient = channel.connect()
        await VoiceClient

async def leaveChannel():
    for x in client.voice_clients:
        return await x.disconnect()

    await channel.guild.change_voice_state(None, False, True)



client.run(TOKEN)
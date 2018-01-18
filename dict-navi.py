# python3 fwew.py
# depends discord.py
import discord
import asyncio
from config import cfg as config

trigger = config["trigger"]
token = config["token"]
client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    # seen the trigger word. also don't allow interactive mode
    if message.content.startswith(trigger) and message.content != trigger:
        link = message.content
        print(link)
        # scrape the page for meta
        m_title = "Test"
        m_description = "This is a test description"
        m_colour = 0x0fa5a6
        em = discord.Embed(title=m_title, description=m_description, colour=m_colour)
        em.set_author(name=message.author, icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=em)

client.run(token)

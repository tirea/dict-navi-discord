# python3 fwew.py
# depends discord.py
import discord
import asyncio
from config import cfg as config
from urllib.request import urlopen
from bs4 import BeautifulSoup

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
    link = message.content
    # seen the trigger word.
    if link.startswith(trigger):
        print(link)
        # scrape the page for meta
        html = urlopen(link)
        soup = BeautifulSoup(html.read(), "html.parser")

        m_title = soup.find("title").get_text(strip=True)
        m_description = soup.find("meta", {"name": "description"})['content']
        m_colour = 0x0fa5a6

        em = discord.Embed(title=m_title, description=m_description, colour=m_colour)

        await client.send_message(message.channel, embed=em)

client.run(token)

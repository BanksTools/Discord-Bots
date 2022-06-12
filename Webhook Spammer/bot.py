#imports
import discord
from discord.ext import commands
import discord.utils
from discord_webhooks import DiscordWebhooks
from discord_webhook import DiscordWebhook

client = commands.Bot(command_prefix="?")


#print if ready
@client.event
async def on_ready():
    print("Ready")


#command that spams a webhook 
@client.command()
async def spam(ctx, webhook=None):
  await ctx.send("Spamming  `"+webhook+"`")
  spamhook = DiscordWebhook(url=webhook, rate_limit_retry=True, content='Message You Want to Spam')
  for i in range(100): 
    response = spamhook.execute()


####!!!!!!!! TOKEN HERE ####!!!!!!!!
client.run("TOKEN")
####!!!!!!!! TOKEN HERE ####!!!!!!!!

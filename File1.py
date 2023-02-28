import discord

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run("MTA4MDA3MzcyNzQ5NDA3ODUxNA.GeNv4c.8G0jU8nLQMr3DqBolCHyAG_yqfOSiuUg-t4Mxs")

import discord

client = discord.Client(intents=discord.Intents.default())
TOKEN = "MTA4MDA3MzcyNzQ5NDA3ODUxNA.GeNv4c.8G0jU8nLQMr3DqBolCHyAG_yqfOSiuUg-t4Mxs"
GUILD = "ECLIPSE"

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')


client.run(TOKEN)

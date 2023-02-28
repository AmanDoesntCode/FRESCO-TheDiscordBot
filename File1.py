import discord

client = discord.Client(intents=discord.Intents.all())
tokenfile = open("Token for fresco.txt","r")
TOKEN = tokenfile.read()
GUILD = "ECLIPSE"

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'esh!':
        response = "Konichiwa Oni Sann!"
        await message.channel.send(response)

client.run(TOKEN)

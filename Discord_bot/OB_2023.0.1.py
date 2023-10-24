import discord


intents = discord.Intents.default()
intents.presences = True  # Enable presence intent
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('$whoareyou'):
        await message.channel.send('I am a server management and assistance tool created by OptiByte Software Solutions.')

    elif message.content.startswith('$help'):
        await message.channel.send('As I am still in development, the list of commands has not yet been published.')

    elif message.content.startswith('$kill'):
        exit()

client.run('MTE2NjE3ODU1ODg5MzM1OTIyNQ.GztKno.f2w7S7WdEGWCDTdermY2_CmFcRvmTd8ikcHO1c')
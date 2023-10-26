import discord
import python_weather
import asyncio
import os

intents = discord.Intents.default()
intents.presences = True
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

    elif message.content.startswith('$about'):
        await message.channel.send('I am a prototype bot created by OptiByte Software Solutions.')

    elif message.content.startswith('$help'):
        await message.channel.send('As I am still in development, the list of commands has not yet been published.')

    elif message.content.startswith('$kill'):
        exit()

    elif message.content.startswith('$gettemp'):
        await get_temp(message)  # await get_weather coroutine

    elif message.content.startswith('$getforecast'):
        await get_forecast(message)

async def get_temp(message):
    client = python_weather.Client()
    response = await client.get('Salmon Arm')

    await message.channel.send(f'Temperature in Salmon Arm: {response.current.temperature}°C')


    await client.close()  #close session

async def get_forecast(message):
    client = python_weather.Client()
    response = await client.get('Salmon Arm')

    for forecast in response.forecasts:
      await message.channel.send(f'Salmon Arm forecast: {forecast}')

    await client.close()


client.run('MTE2NjE3ODU1ODg5MzM1OTIyNQ.GE8gSF.MH1RNPNRBDTgED2xPCeNj8c8U1Ird93g-mTntc')
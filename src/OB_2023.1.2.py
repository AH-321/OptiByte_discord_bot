import discord
import python_weather
import asyncio
import os
import time
import subprocess


intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

def getDirectory():
    # get file's dir
    return os.path.dirname(os.path.realpath(__file__))

try:
    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

        time.sleep(1)
        os.system('clear')

        with open(getDirectory() + "/logo.py") as f:
            exec(f.read())

        print("Starting logging...")
        time.sleep(4)
        print("LOG status:", log_status())
        print("Starting bot...")
        log_status()
        time.sleep(2)
        print("########## Ready ##########")
        #get_time()
except:
    print("ERROR: Could not start bot.")

try:
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        elif message.content.startswith('$about'):
            await message.channel.send('I am a prototype bot created by OptiByte Software Solutions.')

        elif message.content.startswith('$help'):
            print("LOG: user has sent '$help")
            await message.channel.send('You can get weather data (for Salmon Arm) by typing "$gettemp", or "$getforecast". More fetures will be added.')

        elif message.content.startswith('$kill'):
            print("LOG: user has sent '$kill'")
            print("suspending logging...")
            time.sleep(2)
            print("Shutting down...")
            os.system('clear')
            exit()

        elif message.content.startswith('$gettemp'):
            await get_temp(message)  # await get_weather coroutine

        elif message.content.startswith('$getforecast'):
            await get_forecast(message)
except:
    print("ERROR: Could not send message.")

async def get_temp(message):
    print("LOG: user has sent '$gettemp'")
    client = python_weather.Client()
    response = await client.get('Salmon Arm')

    await message.channel.send(f'Temperature in Salmon Arm: {response.current.temperature}°C')


    await client.close()

async def get_forecast(message):
    print("LOG: user has sent '$getforecast'")
    client = python_weather.Client()
    response = await client.get('Salmon Arm')

    for forecast in response.forecasts:
      await message.channel.send(f'Salmon Arm forecast: {forecast}')

    await client.close()

def log_status():
    log_status = "OK"
    return log_status

def global_status():
    print(ProcessLookupError)

def get_time():
    with open(getDirectory() + "/gets_time.py") as f:
        exec(f.read())

client.run('TOKEN') 

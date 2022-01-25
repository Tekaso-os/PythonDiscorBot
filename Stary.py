import discord
import random
import json
import time

with open("config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

TOKEN = jsonObject['token']
prefix = jsonObject['prefix']

client = discord.Client()

@client.event
async def on_ready():
    test = str(client.user).split('#')
    banner = f""" 
    =================================================
                        DICORD BOT
    User: {test[0]}
    hashtag: {test[1]}
    =================================================
    
    """
    print(banner)

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content).split(' ')
    channel = str(message.channel.name)
    print(f'{username}: {user_message}: ({channel})')
    
    if message.author == client.user:
        return
    if user_message[0] == f'{prefix}hello':
        await message.channel.send(f'hi {username}!')
        return
    elif user_message[0] == f'{prefix}bye':
        await message.channel.send(f'see you later {username}')
        return
    elif user_message[0] == f'{prefix}random':
        response = f'This is your random number: {random.randrange(100000)}'
        await message.channel.send(Response)
        return
    elif user_message[0] == f'{prefix}argumento':
        await message.channel.send(f'Agumento 0 = {user_message[0]} Argumento 1 = {user_message[1]} argumento 2 = {user_message[2]}')
    
    elif user_message[0] == f'{prefix}questionario':
        await message.channel.send(f'Qual seu nome?')
        time.sleep(5)
        resposta = user_message[1]
        if user_message == '--questionario':
            return
        
        await message.channel.send(resposta)
        
client.run(TOKEN)
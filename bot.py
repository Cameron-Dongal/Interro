import os
from dotenv import load_dotenv
import discord
import interro_requests as ir

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    if bot.user in message.mentions:
        user_input = message.content
        parse_response = ir.parse_request(user_input)
        words = parse_response.split(",")

        if words[0] == "ON_TOPIC":
            response = ir.generate_on_topic(user_input)
        elif words[0] == "OFF_TOPIC":
            if len(words) > 1 and words[1] == "jailbreak":
                response = ir.generate_off_topic_jailbreak(user_input)
            else:
                response = ir.generate_off_topic(user_input)
        elif words[0] == "ERROR!":
            response = ir.generate_error(words[1])
            
    tag = "</think>"
    before, sep, after = response.partition(tag)
    if sep: 
        response = after.lstrip()

    await message.channel.send(response)

bot.run(TOKEN)

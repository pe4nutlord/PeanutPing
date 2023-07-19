# Install discord.py
# Command: pip install discord.py

import discord

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online and ready to log ghost pings!')

@bot.event
async def on_message_delete(message):
    # Check if the message author is a bot
    if message.author.bot:
        return

    if len(message.mentions) > 0:
        mentions = ', '.join(f'<@{user.id}>' for user in message.mentions)
        ghost_ping_msg = f'Ghost ping detected: <@{message.author.id}> mentioned {mentions}\nMessage Content: {message.content}'
        print(ghost_ping_msg)
        
        # Send the ghost ping message to the same channel where the original message was deleted
        channel = message.channel
        await channel.send(ghost_ping_msg)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = 'YOUR_BOT_TOKEN'
bot.run(bot_token)

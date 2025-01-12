import discord
import re

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Received message: {message.content} from {message.author}')
        
        if message.author == self.user:
            return

        # Check if the message contains an emoji that starts with :snoring
        snoring_emoji_pattern = re.compile(r'<:snoring\w*:\d+>')
        if snoring_emoji_pattern.search(message.content):
            await message.channel.send(message.content)
        else:
            print(f'Ignored message: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('TOKENHERE')
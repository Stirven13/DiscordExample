import os
import tomllib

import discord
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self) -> None:
        with open(r'data/config.toml', 'rb') as file:
            self.config: dict = tomllib.load(file)
        intents: discord.Intents = discord.Intents().all()
        super(Bot, self).__init__(command_prefix=self.config['prefix'], help_command=None, intents=intents)
        super().run(self.config['token'])

    async def setup_hook(self) -> None:
        await self.load_cogs()

    async def load_cogs(self):
        for filename in os.listdir('cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')

    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return  # Ignore messages from bots
        await self.process_commands(message)

    async def on_command_error(self, ctx: commands.Context, exception: commands.CommandError) -> None:
        match exception:
            case commands.CommandNotFound():
                return  # Ignore commands that don't exist
            case commands.MissingRequiredArgument():
                return  # Ignore commands that are missing arguments
            case commands.BadArgument():
                return  # Ignore commands that have bad arguments
            case _:
                print(exception)  # Print the error to the console


if __name__ == '__main__':
    bot = Bot()
else:
    print('This is not a module')

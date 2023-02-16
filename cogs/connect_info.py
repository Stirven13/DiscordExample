import asyncio

import discord
from discord.ext import tasks, commands


class ConnectInfo(discord.ext.commands.Cog):
    def __init__(self, bot: discord.ext.commands.bot.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self) -> None:
        await asyncio.sleep(1)
        print(f"""\rLogin as - {self.bot.user}\n"""
              f"""Ping - {round(self.bot.latency * 1000)} ms\n"""
              f"""Version discord lib - {discord.__version__}\n"""
              f"""Url for add bot - https://discordapp.com/oauth2/authorize?&client_id={self.bot.application_id}&scope=bot""")


async def setup(bot: discord.ext.commands.bot.Bot) -> None:
    await bot.add_cog(ConnectInfo(bot))


if __name__ == "__main__":
    print("This is a module")

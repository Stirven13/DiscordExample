import discord
from discord.ext import commands

class Animals(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="cat")
    async def cat_command(self, ctx):
        await ctx.send('Meow!')

    @commands.command(name="catimg")
    async def cat_image_command(self, ctx):
        var_embed = discord.Embed(title="Cat", color=0x00ff00)
        var_embed.set_image(url="https://cdn2.thecatapi.com/images/cat.jpg")
        var_embed.set_footer(text="Using: https://thecatapi.com/")
        await ctx.send(embed=var_embed)


async def setup(bot: discord.ext.commands.bot.Bot) -> None:
    await bot.add_cog(Animals(bot))


if __name__ == "__main__":
    print("This is a module")

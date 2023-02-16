import discord
from discord.ext import commands


class AboutEmbeds(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name='about')
    async def embed_generation_command(self, ctx):
        var_embed = discord.Embed(title="About", color=0x00ff00)
        var_embed.add_field(name="Field1_name", value="Field1_value", inline=False)
        var_embed.add_field(name="Field2_name", value="Field2_value", inline=False)
        var_embed.add_field(name="Field3_name", value="Field3_value", inline=False)

        var_embed.add_field(name="Field1_name", value="Field1_value", inline=True)
        var_embed.add_field(name="Field2_name", value="Field2_value", inline=True)
        var_embed.add_field(name="Field3_name", value="Field3_value", inline=True)
        var_embed.add_field(name="Field4_name", value="Field4_value", inline=True)
        var_embed.add_field(name="Field5_name", value="Field5_value", inline=True)

        var_embed.set_thumbnail(url="https://discordpy.readthedocs.io/en/latest/api.html#embed")

        await ctx.send(embed=var_embed)

async def setup(bot: discord.ext.commands.bot.Bot) -> None:
    await bot.add_cog(AboutEmbeds(bot))
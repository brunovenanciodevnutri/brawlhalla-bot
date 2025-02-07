from webscraping.status import *
import discord
from discord import app_commands
from apikey import *
import asyncio
import json
import requests
from time import sleep

cor = 0x9910CD
msg_id = None
msg_user = None

class primeirobot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix='/', intents=intents, timeout=None)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f'{self.user} EM EXECUÇÃO')

bot = primeirobot()

@bot.tree.command(name="status", description='Show the status of a brawlhalla player.')
@app_commands.describe(player="Enter player name.")
async def status(interaction: discord.interactions, player: str):
    embed = discord.Embed(
        title="🔍 Searching...",
        color=cor,
        description="")
    await interaction.response.send_message('', embed=embed)
    start(n = player)
    with open('./data/zdata.json') as arquivo:
        playerstats = json.load(arquivo)
    embed = discord.Embed(
        title=f"1v1 Ranked {playerstats['Region']}",
        color=cor,
        description=''
        )
    embed.set_author(name=playerstats['Name'], icon_url='https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/4/44/Bot_VALKRI_MK1.png/revision/latest?cb=20230518210800')
    
    for c in range(1, 6):
        if playerstats['Tier'] == 'Valhallan':
            embed.set_thumbnail(url='https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/1/1c/Banner_Rank_Valhallan.png/revision/latest?cb=20220928135053')
        elif playerstats['Tier'] == 'Diamond':
            embed.set_thumbnail(url='https://www.stats.brawlhalla.fr/assets/img/bannerTier/Diamond-min.png')
        elif playerstats['Clan'] == f'Platinum {c}':
            embed.set_thumbnail(url='https://www.stats.brawlhalla.fr/assets/img/bannerTier/Platinum%200-min.png')
        elif playerstats['Tier'] == f'Gold {c}':
            embed.set_thumbnail(url='https://www.stats.brawlhalla.fr/assets/img/bannerTier/Gold%200-min.png')
        elif playerstats['Tier'] == f'Silver {c}':
            embed.set_thumbnail(url='https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/5/5c/Banner_Rank_Silver.png/revision/latest?cb=20161110140055')
        elif playerstats['Tier'] == f'Bronze {c}':
            embed.set_thumbnail(url='https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/a/a6/Banner_Rank_Bronze.png/revision/latest?cb=20161110140114')
        elif playerstats['Tier'] == f'Tin {c}':
            embed.set_thumbnail(url='https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/e/e1/Banner_Rank_Tin.png/revision/latest?cb=20161110140036')
        elif playerstats['Tier'] == 'Unranked':
            embed.set_thumbnail(url='https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/3/3f/Banner_Rank_Unranked.png/revision/latest?cb=20220928135052')

    embed.add_field(name='Clan', value=f'{playerstats['Clan']}')

    embed.add_field(name='', value='', inline=False)

    embed.add_field(name='Tier', value=f'{playerstats['Tier']}')
    embed.add_field(name='Level', value=f'{playerstats['Level']} | {playerstats['XP']}')
    
    embed.add_field(name='', value='', inline=False)

    embed.add_field(name='World Ranking', value=f'{playerstats['World Ranking']}')

    embed.add_field(name='', value='', inline=False)

    embed.add_field(name='Rate', value=f'{playerstats['Rating']}')
    embed.add_field(name='Peak', value=f'{playerstats['Peak Rating']}')

    embed.add_field(name='', value='', inline=False)

    embed.add_field(name='Winrate Ranked', value=f'{playerstats['Winrate Ranked']}')
    embed.add_field(name='Winrate Unranked', value=f'{playerstats['Winrate Unranked']}')

    embed.set_footer(text='🛡️ Desenvolvido por Bruno Venâncio')


    await interaction.followup.send(f'{interaction.user.mention}', embed=embed)

bot.run(bot_token)
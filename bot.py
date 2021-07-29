import discord, requests, datetime
from discord.ext import commands
from bs4 import BeautifulSoup

token = "ODM2NzQ5MDQ1MjUwM"+"zkyMDc0.YIihRg.48Khv8wV7FNfCvssQzSm9aE0uG0"

app = commands.Bot(command_prefix="!")

@app.event
async def on_ready():
    print("ready")

@app.command()
async def 롤(ctx, *, text):
    url = "https://www.op.gg/summoner/userName=" + text
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    solorank = soup.find("div", attrs={"class":"RankType"})
    tier = soup.find("div", attrs={"class":"TierRank"})
    tierdtl = soup.find("div", attrs={"class":"TierInfo"})
    tierscore = tierdtl.span.get_text()
    score = tierscore.strip()

    if solorank.get_text() == "Ranked Solo":
        await ctx.send("솔로랭크")
    await ctx.send(tier.get_text())
    await ctx.send(score)
    await ctx.send(url)

@app.command()
async def 내정보(ctx):
    user = ctx.author
    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
    await ctx.channel.send(f"{ctx.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
    await ctx.channel.send(f"{ctx.author.mention}의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")


app.run(token)
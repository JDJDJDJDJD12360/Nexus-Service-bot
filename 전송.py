import discord
from discord.ext import commands

# 봇 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def 상품(ctx):
    # 임베드 생성 (제목 및 색상 설정)
    embed = discord.Embed(
        title="Nexus 2 PC EMULATOR",
        description=(
            "restart\n"
            "No Temp ban\n"
            "No van code\n"
            "Fix van -152\n"
            "Zombie vanguard\n"
            "저희 2pc 제품은 빡고 보다는 정지율이 매우 낮은 esp 단품 제품입니다 "
            "esp 성능은 말도 안되게 좋고. esp 또한 정지율이 극하게 낮으며 거의 안먹습니다.. "
            "리셀 문의는 티켓 열어주세요!!"
        ),
        color=0x2b2d31  # 다크 모드 어울리는 색상
    ) # <-- 이 부분에 Embed 괄호가 닫혀야 합니다!

    # 가격 정보 추가 (필드 방식)
    embed.add_field(name="가격", value="```\n영구제 : 5.0\n30일   : 3.5\n1일    : 0.5\n```", inline=False)

    # 푸터 설정
    embed.set_footer(text="2026-11-08 오전 1:23")

    # 메시지 전송
    await ctx.send(embed=embed)

# 봇 토큰 입력
bot.run("MTU2NjEzMjU1OTUwMTU5ODkxMg.GLbMVC.KtcoOsYnE7h1H5Xbi4jCyinqaSgPF99RKsq8V4")
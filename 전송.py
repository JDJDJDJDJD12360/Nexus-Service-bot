import discord
from discord.ext import commands

# 봇 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 관리자 채널 ID 설정
ADMIN_CHANNEL_ID = 1568666516621099040

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 1. 하드리셋 안내 패널과 버튼을 전송하는 명령어 (!패널)
@bot.command()
async def 패널(ctx):
    embed = discord.Embed(
        title="24H HWID RESET",
        description="자동 하드리셋 패널입니다.\n\n"
                    "**[주의사항]**\n"
                    "• **하드리셋은 별도 비용 3,000원(0.3) 부과**됩니다[cite: 3].",
        color=0x2b2d31
    )
    embed.set_footer(text="Nexus Service SYSTEM")

    await ctx.send(embed=embed, view=HardResetView(bot))

# 2. 버튼 뷰 클래스
class HardResetView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="하드리셋 신청하기", style=discord.ButtonStyle.primary, emoji="🔑")
    async def reset_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(HardResetModal(self.bot))

# 3. 제품 이름과 키를 입력받는 모달(팝업창) 클래스
class HardResetModal(discord.ui.Modal, title="하드리셋 신청"):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    product_name = discord.ui.TextInput(
        label="제품 이름",
        placeholder="예: Nexus 2 PC EMULATOR 제품",
        required=True,
        max_length=100
    )
    
    license_key = discord.ui.TextInput(
        label="라이선스 키 (Key)",
        placeholder="사용 중인 인증 키를 입력해주세요.",
        style=discord.TextStyle.short,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        product = self.product_name.value
        key = self.license_key.value
        user = interaction.user

        # 사용자에게 접수 완료 메시지 전송 (본인만 보임)
        await interaction.response.send_message(
            f"✅ **하드리셋 신청이 완료되었습니다!**\n관리자가 확인 후 처리할 예정입니다.", 
            ephemeral=True
        )

        # 관리자 전용 채널로 신청 내역 전송
        admin_channel = self.bot.get_channel(ADMIN_CHANNEL_ID)
        if admin_channel:
            admin_embed = discord.Embed(
                title="🚨 새로운 하드리셋 신청 접수",
                color=0xffcc00,
                description=f"• **신청자:** {user.mention} (`{user}`)\n"
                            f"• **제품명:** `{product}`\n"
                            f"• **라이선스 키:** `{key}`"
            )
            admin_embed.set_footer(text=f"User ID: {user.id}")
            await admin_channel.send(embed=admin_embed)

# 봇 토큰 입력
bot.run("MTU2NjEzMjU1OTUwMTU5ODkxMg.GLbMVC.KtcoOsYnE7h1H5Xbi4jCyinqaSgPF99RKsq8V4")

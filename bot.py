import discord
from discord.ext import commands
import os

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
    # Set the bot's status to "Playing skybattle.fun"
    activity = discord.Game(name="skybattle.fun")
    await bot.change_presence(activity=activity)
    print(f'Status set to: Playing skybattle.fun')

@bot.command(name='dm')
async def send_dm(ctx, user: discord.Member, *, message: str):
    """Send a DM to a specific user. Usage: !dm @user message"""
    
    # Only allow bot owner or admins to use this command
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You don't have permission to use this command.")
        return
    
    try:
        await user.send(message)
        await ctx.send(f"Message sent to {user.display_name}")
        print(f"DM sent to {user.display_name}: {message}")
    except discord.Forbidden:
        await ctx.send(f"Cannot send DM to {user.display_name}. They may have DMs disabled.")
    except Exception as e:
        await ctx.send(f"Error sending message: {str(e)}")

@bot.command(name='announce')
async def announce_channel(ctx, *, message: str):
    """Send an announcement to the current channel. Usage: !announce message"""
    
    # Only allow bot owner or admins to use this command
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You don't have permission to use this command.")
        return
    
    # Delete the command message
    await ctx.message.delete()
    
    # Send the announcement
    embed = discord.Embed(
        title="📢 Server Announcement",
        description=message,
        color=0x00ff00
    )
    embed.set_footer(text=f"Announced by {ctx.author.display_name}")
    
    await ctx.send("@everyone", embed=embed)
    print(f"Announcement sent by {ctx.author.display_name}: {message}")

# Get bot token from environment variable (safer for GitHub)
bot_token = os.getenv('BOT_TOKEN')
if not bot_token:
    print("Error: BOT_TOKEN environment variable not set!")
    exit(1)
bot.run(bot_token)
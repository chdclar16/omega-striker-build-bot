import discord
from discord.ext import commands
import aiohttp
import responses
import asyncio
from config import TOKEN, channel_id

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or('/'), intents=intents)

request_lock = asyncio.Lock()

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    await bot.wait_until_ready()

@bot.command(name='striker')
async def omegastriker(ctx, *, query):
    # Add a delay before sending the response
    await asyncio.sleep(1)  # Adjust the delay duration as needed

    await send_message(ctx, query)

async def send_message(ctx, user_message):
    try:
        async with request_lock:
            response_list = responses.get_response(user_message)

            if len(response_list) >= 1:
                forward_response = response_list[0]
                goalie_response = response_list[1] if len(response_list) >= 2 else None
                forward_description = response_list[2]
                goalie_description = response_list[3]

                if goalie_response is None or not goalie_response.startswith('http'):
                    goalie_response = None

                if forward_response is not None and forward_response.startswith('http'):
                    async with aiohttp.ClientSession() as session:
                        async with session.get(forward_response) as resp:
                            if resp.status == 200:
                                forward_filename = "forward_image.jpg"
                                with open(forward_filename, "wb") as file:
                                    file.write(await resp.read())
                                forward_file = discord.File(forward_filename)
                                forward_embed = discord.Embed()
                                forward_embed.set_image(url=f"attachment://{forward_filename}")
                                forward_embed.set_author(name="Forward")
                                forward_embed.description = forward_description

                                await ctx.author.send(file=forward_file, embed=forward_embed)
                                await ctx.send("Sent Forward build to your DM!")

                if goalie_response is not None and goalie_response.startswith('http'):
                    async with aiohttp.ClientSession() as session:
                        async with session.get(goalie_response) as resp:
                            if resp.status == 200:
                                goalie_filename = "goalie_image.jpg"
                                with open(goalie_filename, "wb") as file:
                                    file.write(await resp.read())
                                goalie_file = discord.File(goalie_filename)
                                goalie_embed = discord.Embed()
                                goalie_embed.set_image(url=f"attachment://{goalie_filename}")
                                goalie_embed.set_author(name="Goalie")
                                goalie_embed.description = goalie_description

                                await ctx.author.send(file=goalie_file, embed=goalie_embed)
                                await ctx.send("Sent Goalie build to your DM!")

                if forward_response is None and goalie_response is None:
                    await ctx.send("No builds yet or check the spelling")

            else:
                await ctx.author.send("Invalid number of responses.")

    except Exception as e:
        print(e)
    finally:
        if request_lock.locked():
            request_lock.release()

@bot.event
async def on_message(message):
    if message.channel.id == channel_id:
        await bot.process_commands(message)


def run_discord_bot():
    bot.run(TOKEN)

run_discord_bot()

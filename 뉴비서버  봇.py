from discord import Client
from discord_components import DiscordComponents, Button, ButtonStyle

bot = Client()

@bot.event
async def on_ready():
    DiscordComponents(bot)

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return

    await msg.channel.send(
        "Content",
        components=[
            Button(style=ButtonStyle.blue, label="Blue"),
            Button(style=ButtonStyle.red, label="Red"),
            Button(style=ButtonStyle.URL, label="url", url="https://example.org"),
        ],
    )

    res = await bot.wait_for("button_click")
    if res.channel == msg.channel:
        await res.respond(
            type=InteractionType.ChannelMessageWithSource,
            content=f'{res.component.label} clicked'
        )


bot.run("OTQyMDUyNzg0OTY1MDI5OTc4.Yge5Bg.9jUZq9gFDh8GlXrYKcmR7n0mKRs")
import discord
from discord.ext import commands
from datetime import datetime
import asyncio

TOKEN = "MTQ4MjIxNzkxMzM2MzczMDQ4NA.Gzma9t.u3PZu70zDexcbgwU8UTPesKnQY8AE3lAAVmeD8"  # Replace with your actual token

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class WorkLogModal(discord.ui.Modal, title="Work Log Entry"):
    task = discord.ui.TextInput(label="Task", placeholder="Describe the work done")
    person = discord.ui.TextInput(label="Person", placeholder="Who did it?")
    status = discord.ui.TextInput(label="Status", placeholder="Successful / Failed")

    async def on_submit(self, interaction: discord.Interaction):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # First acknowledge the interaction
        await interaction.response.defer()

        # Now send a follow-up message and capture it
        message = await interaction.followup.send("Initializing log entry...", wait=True)

        # Animate edits
        await asyncio.sleep(1)
        await message.edit(content="> Accessing system logs...")
        await asyncio.sleep(1)
        await message.edit(content="> Writing entry...")
        await asyncio.sleep(1)

        # Final hacker-style log entry
        log_entry = (
            "```diff\n"
            f"+ Timestamp: {timestamp}\n"
            f"+ By: {self.person}\n"
            f"+ Task: {self.task}\n"
            f"+ Status: {self.status}\n"
            "```"
        )
        await message.edit(content=log_entry)

@bot.tree.command(name="log", description="Add a work log entry")
async def log(interaction: discord.Interaction):
    await interaction.response.send_modal(WorkLogModal())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot is online as {bot.user}")

bot.run(TOKEN)
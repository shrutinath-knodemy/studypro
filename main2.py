import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def ask_ai(prompt):
   try:
       response = client.chat.completions.create(
           model="gpt-4.1-mini",
           messages=[{"role": "user", "content": prompt}]
       )
       return response.choices[0].message.content
   except Exception as e:
       return f"Error: {e}"

@bot.command()
async def explain(ctx, *, topic):
   prompt = f"Explain this topic in simple terms for studying: {topic}"
   await ctx.send(ask_ai(prompt))


@bot.command()
async def question(ctx, *, topic):
   prompt = f"Create 5 study questions about: {topic}"
   await ctx.send(ask_ai(prompt))


@bot.command()
async def answers(ctx, *, topic):
   prompt = f"Provide answers to common questions about: {topic}"
   await ctx.send(ask_ai(prompt))

import asyncio
import discord
import random
import os
from discord.ext import commands
from discord.utils import get
import time
import pickle
import string
from random import choice
from string import punctuation, ascii_letters, digits
intents = discord.Intents.default()
intents2 = discord.Intents(members=True, guilds=True, voice_states=True)

class Main(commands.Cog, name="관리"):

    """
    PR Bot 관리 명령어 카테고리 입니다.
    """

    def __init__(self, app):
        self.app = app


def setup(app):
    app.add_cog(Main(app))

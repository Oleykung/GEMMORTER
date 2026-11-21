#!/usr/bin/env python3
# Fixed starter for Render.com - ensures bot runs 24h with web
import os
import sys

print("=== Granado Espada M - Render 24h Starter ===")
print(f"PORT: {os.getenv('PORT', 'Not set')}")
print(f"TOKEN: {'SET' if os.getenv('DISCORD_TOKEN') else 'NOT SET'}")
print(f"ALERT_CHANNEL: {os.getenv('ALERT_CHANNEL_ID', 'NOT SET')}")

# Check requirements
try:
    import discord
    import aiohttp
    import flask
    print("✅ All requirements installed")
except ImportError as e:
    print(f"❌ Missing requirement: {e}")
    print("Running pip install...")
    os.system("pip install -r requirements.txt")

# Start bot.py which includes web server + discord bot
print("🚀 Starting bot.py (Discord + Web Realtime)...")
import bot
# bot.py will handle its own startup

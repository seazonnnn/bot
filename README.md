# Discord Bot - Skybattle Status

A simple Discord bot that shows "Playing skybattle.fun" in its status and provides DM and announcement commands.

## Features

- Shows "Playing skybattle.fun" status
- `!dm @user message` - Send DM to specific user
- `!announce message` - Send announcement with @everyone ping

## Setup

1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Get your bot token from Discord Developer Portal:
   - Go to https://discord.com/developers/applications
   - Create a new application
   - Go to "Bot" section
   - Copy the token

3. Set up environment variable:
   - Copy `.env.example` to `.env`
   - Add your bot token to `.env` file

4. Run the bot:
   ```
   python bot.py
   ```

## Commands

- `!dm @username message` - Send DM to a user (Admin only)
- `!announce message` - Send server announcement (Admin only)

## Deployment

This bot is ready for deployment on platforms like Railway, Render, or Heroku.

## Invite Bot to Server

Use this URL format (replace CLIENT_ID with your bot's client ID):
```
https://discord.com/api/oauth2/authorize?client_id=CLIENT_ID&permissions=8&scope=bot
```
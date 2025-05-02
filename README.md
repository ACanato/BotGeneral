# Discord Bot - Welcome & Admin

This bot was created to help manage a Discord server with features like welcome messages, message clearing, suggestions, and other useful commands for server administration.

## Features

- **Automatic Welcome Messages**: Sends a personalized welcome message to new members who join the server.
- **Message Clearing**: Allows users to delete a number of messages in a channel.
- **Useful Commands**: A list of commands to assist with server management.
- **Suggestions**: Allows members to submit suggestions that can be voted on.

## Commands

### Administration Commands:

- `!clear <amount>`: Clears a specified number of messages from the current channel.
    - Example: `!clear 10` will delete the last 10 messages.

### Information Commands:

- `!list_commands`: Displays a list of all available commands.
- `!info`: Provides information about the bot’s features.

### General Commands:

- `!say <message>`: The bot will repeat the message you send.
    - Example: `!say Hello, world!`

### Suggestion Command:

- `!suggest <suggestion>`: Sends a suggestion to the suggestions channel.
    - Suggestions can be voted on with reactions of 👍 (Approve) and 👎 (Disapprove).

## Setup

### Prerequisites

1. **Python 3.8 or higher** installed.
2. **discord.py library** installed.
   - You can install the library with the following command:

   ```bash
   pip install discord.py

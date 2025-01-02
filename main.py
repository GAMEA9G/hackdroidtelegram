#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import subprocess

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,
                      InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes, ConversationHandler, MessageHandler, filters)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    cmd = ["./adb", "connect", "192.168.100.107:39119"]
    subprocess.Popen(['cmd.exe', '/c', 'start'] + cmd, shell=True)
    await update.message.reply_html(
        
        
        await update.message.reply_text("Hacked nearby device")

    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text('''Hi I am hack bot i can hack android phones  \ncommands: \n/help - display this message \n/you - open youtube \n /tele - open telegram \n/scr - take screenshot and show it \n/pho - play a video''')


async def you(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("This bot will open youtube in the phone")
    cmd = ["./adb", "shell", "monkey", "-p", "app.revanced.android.youtube" ,"-v", "1"]
    subprocess.Popen(['cmd.exe', '/c', 'start'] + cmd, shell=True)
async def tele(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("This bot will open telegram in the phone")
    cmd = ["./adb", "shell", "monkey", "-p", "org.telegram.messenger" ,"-v", "1"]
    subprocess.Popen(['cmd.exe', '/c', 'start'] + cmd, shell=True)
async def cam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("This bot will open camera in the phone")
    cmd = ["./adb", "shell", "monkey", "-p", "com.oplus.camera" ,"-v", "6"]
    subprocess.Popen(['cmd.exe', '/c', 'start'] + cmd, shell=True)
async def pho(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("This bot will open phonebhootham in the phone")
    cmd = ["./adb", "shell", "am", "start", "-a", "android.intent.action.VIEW",  "-t", "video/mp4", "-d", "file:///sdcard/Download/videoplayback.mp4"]
    subprocess.Popen(['cmd.exe', '/c', 'start'] + cmd, shell=True)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text('Bye! Hope to talk to you again soon.', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
async def screenshort(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Execute ADB command to take screenshot
        subprocess.run(['adb', 'shell', 'screencap', '-p', '/sdcard/screenshot.png'])

        # Pull the screenshot to local machine
        subprocess.run(['adb', 'pull', '/sdcard/screenshot.png'])

        # Send the screenshot to the user
       
        await context.bot.send_document(chat_id=update.message['chat']['id'], document=open(
        'screenshot.png', 'rb'), filename='screenshot.png')
        # Optionally, remove the local screenshot file after sending
        subprocess.run(['rm', 'screenshot.png'])
    except Exception as e:
        logger.error(f"Error taking screenshot: {e}")
        await update.message.reply_text('Failed to take screenshot.')
def main() -> None:
    """Run the bot."""
    application = Application.builder().token().build()

    application.add_handler(CommandHandler("you", you))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("tele", tele))
    application.add_handler(CommandHandler("cam", cam))
    application.add_handler(CommandHandler("pho", pho))
    application.add_handler(CommandHandler("scr", screenshort))
    # Handle the case when a user sends /start but they're not in a conversation
    application.add_handler(CommandHandler('start', start))
    
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

    application.run_polling()


if __name__ == '__main__':
    main()
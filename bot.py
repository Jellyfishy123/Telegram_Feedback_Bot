from typing import Final

# pip install python-telegram-bot
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

print("Starting up bot...")

TOKEN: Final = "6581268911:AAES4rjDrO11ewsSZlylCnhmWkM8IW582Xs"
BOT_USERNAME: Final = "@tweested_games_feedback_bot"

MESSAGES_FILE = "messages.txt"


# Using the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Hello Freshies!
We hope that FOP had been going well so far! If you have any concerns, please let us know through this channel OR you can also directly message your welfies Janelle (@jernihao) or Dezyrae (@dezbez) if you need someone to talk to! 🫶🏻

Click /feedback to start!

We will get back to you as soon as we can! ◡̈ 

(You may use a pseudonym to remain anonymous)
"""
    )


# Using the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"

We will get back to you as soon as we can! ◡̈ 

(You may use a pseudonym to remain anonymous)
"""
    )


# Using the /feedback command
async def feedback_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
What is your OG name?
"""
    )


# Using the /safety command
async def safety_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """What are your concerns? Please be as detailed as possible:
• What: What happened?
• Where: Where did the incident take place?
• When: When was it?
• How: How do you feel?
• Who: Who is involved? """
    )


# Using the /wellbeing command
async def wellbeing_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """What are your concerns? Please be as detailed as possible:        
• What: What happened?
• Where: Where did the incident take place?
• When: When was it?
• How: How do you feel?
• Who: Who is involved? """
    )


# Using the /others command
async def others_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """What are your concerns? Please be as detailed as possible:
• What: What happened?
• Where: Where did the incident take place?
• When: When was it?
• How: How do you feel?
• Who: Who is involved? """
    )


# Using the /done command
async def done_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Thank you for making WKWSCI FOP’23 as safer and better space. We will contact you if necessary ◡̈ """
    )


def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if "celestia" in processed:
        return """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"
"""
    if "kamera" in processed:
        return """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"
"""
    if "kino" in processed:
        return """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"
"""
    if "kiyoshi" in processed:
        return """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"
"""
    if "weros" in processed:
        return """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"
"""
    if "luckigee" in processed:
        return """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"
"""
    if "bonedit" in processed:
        return """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"
"""
    if "azaleah" in processed:
        return """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"
"""
    if "boottega" in processed:
        return """
• If you have any safety concerns, please type "/safety" 
• If you have any well-being concerns, please type “/wellbeing”
• If you have other feedback, please type "/others"
"""
    else:
        return """Thanks for your feedback! Do you wish to submit another concern?
If Yes, please click /safety or /wellbeing or /others
If No, please click /done
    """


# Function to append data to the text file
def append_to_text_file(file_path, data):
    with open(file_path, "a", encoding="utf-8") as textfile:
        textfile.write("\n".join(data) + "\n\n")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == "group":
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print("Bot:", response)
    await update.message.reply_text(response)

    # Save the user message to a text file
    data_to_save = [
        str(update.message.chat.id),
        update.message.from_user.username if update.message.from_user.username else "",
        text,
    ]
    append_to_text_file(MESSAGES_FILE, data_to_save)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


# Run the program
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("safety", safety_command))
    app.add_handler(CommandHandler("wellbeing", wellbeing_command))
    app.add_handler(CommandHandler("others", others_command))
    app.add_handler(CommandHandler("done", done_command))
    app.add_handler(CommandHandler("feedback", feedback_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print("Running...")
    # Run the bot
    app.run_polling(poll_interval=3)

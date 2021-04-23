from telegram.ext import *

def handle_errors(update,context):
    print(f"Update {update} caused error {context.error}")

def start_command_handler(update,context):
    update.message.reply_text("Welcome to the CS Bot 😎🤳")

def main():
    print("Bot is running...")

    updater = Updater("1792469993:AAHtPDcnnsXPS20FI6Top3F-ClKrrnlvwNc",use_context=True)

    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start',start_command_handler))

    dispatcher.add_error_handler(handle_errors)

    updater.start_polling()

    updater.idle()


main()


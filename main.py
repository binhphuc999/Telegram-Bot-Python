from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("Your Bot Token",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir, Welcome to the Binh's Bot write\
        /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :- 
    /love - To get the my love
    /bio - To access my bio
    /gmail - To get gmail URL
    /geeks - To get the GeeksforGeeks URL
    /author - To visit author's website""")


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("Your gmail link here (I am not\
        giving mine one for security reasons)")


def love_url(update: Update, context: CallbackContext):
    update.message.reply_text("Love Link =>\
    http://thuongthuongcute.com/")


def bio_url(update: Update, context: CallbackContext):
    update.message.reply_text("bio URL => \
        https://nguyennangbinh.xyz/")


def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksforGeeks URL => https://www.geeksforgeeks.org/")


def author_url(update: Update, context: CallbackContext):
    update.message.reply_text("Author's URL => https://nguyennangbinh.com/")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" %
                              update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" %
                              update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('love', love_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('bio', bio_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(CommandHandler('author', author_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

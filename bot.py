from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''Hi iam Official bot of fast move 😜
You can't Add me to your group 😂
 
 Join our move channel ❤️ @mrbhiman12
  ''')
def help(updater,context):
 updater.message.reply_text("Add me to your group ")
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hello {member.full_name} , ഞങ്ങളുടെ ഗ്രൂപ്പിൽ ചേരുന്നതിന് നന്ദി ❤️.. ദയവായി ഞങ്ങളുടെ official ഗ്രൂപ്പിൽum ചേരുക @mrbhiman12 ❤..  ')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()

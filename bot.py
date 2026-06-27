from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from openai import OpenAI
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def handle(update: Update, context: CallbackContext):
    text = update.message.text

    if not update.message.reply_to_message:
        return

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "کوتاه جواب بده"},
            {"role": "user", "content": text}
        ]
    )

    update.message.reply_text(response.choices[0].message.content)

updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text, handle))

updater.start_polling()
updater.idle()

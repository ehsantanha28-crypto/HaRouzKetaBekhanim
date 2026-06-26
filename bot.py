from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from openai import OpenAI
import os

TELEGRAM_TOKEN = os.getenv("8855575409:AAHocAg0DziWENO_JPfuG8gNMiRNbEG_m-Y")
OPENAI_API_KEY = os.getenv("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")

client = OpenAI(api_key=OPENAI_API_KEY)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""

    if not update.message.reply_to_message and not update.message.entities:
        return

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "تو یک دستیار تلگرام هستی. کوتاه جواب بده."},
            {"role": "user", "content": text}
        ]
    )

    await update.message.reply_text(response.choices[0].message.content)

app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()

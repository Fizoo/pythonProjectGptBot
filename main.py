import openai
import telebot

openai.api_key = "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"

bot = telebot.TeleBot("5490526869:AAHwwB0DlXSKfD2ykXHUKyb2vIPVXx6ctaA")


@bot.message_handler(func=lambda _: True)
def handle_message(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.5,
    max_tokens=500,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
  )
  bot.send_message(chat_id=message.from_user.id, text=response["choices"][0]["text"])


bot.polling()


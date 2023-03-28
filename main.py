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


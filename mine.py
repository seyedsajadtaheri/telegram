from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import jdatetime, datetime
from keep_alive import keep_alive

BOT_TOKEN = "8170968583:AAFhrZ4Qr63AhvY7A_g4W3n3puz3G2zo6Nc"
OWNER_ID = 1087968824
GROUP_ID = -1002182291058

FOOTER = (
    "\n\n📌 مسیر روشن | آدرس گروه: https://t.me/Masireroshannewsagency"
    "\n📌 ارتباط با مدیران: https://t.me/iranformeandyou"
)

def get_time_info(utc_time):
    tehran_time = utc_time + datetime.timedelta(hours=3, minutes=30)
    shamsi = jdatetime.datetime.fromgregorian(datetime=tehran_time).strftime("%Y/%m/%d")
    saat = tehran_time.strftime("%H:%M")
    return f"{shamsi} | ⏰ {saat}"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg and msg.chat_id == GROUP_ID and msg.from_user.id == OWNER_ID:
        zaman = get_time_info(msg.date)
        footer = f"\n\n📅 تاریخ و ساعت: {zaman}" + FOOTER
        reply = msg.reply_to_message.message_id if msg.reply_to_message else None

        prefix = ""
        text = msg.text or msg.caption or ""

        if text.startswith("#فوری"):
            prefix = "🔷 **فوری**\n\n"
            text = text.replace("#فوری", "", 1).lstrip()
        elif text.startswith("#تحلیل"):
            prefix = "🧠 **#تحلیل**\n\n"
            text = text.replace("#تحلیل", "", 1).lstrip()
        elif text.startswith("#سیاسی"):
            prefix = "🏛 **#موضوع_سیاسی**\n\n"
            text = text.replace("#سیاسی", "", 1).lstrip()
        elif text.startswith("#نظامی"):
            prefix = "🔰 **#گزارش_نظامی**\n\n"
            text = text.replace("#نظامی", "", 1).lstrip()
        elif text.startswith("#ورزشی"):
            prefix = "🏅 **#ورزشی**\n\n"
            text = text.replace("#ورزشی", "", 1).lstrip()
        elif text.startswith("#فرهنگی"):
            prefix = "🎭 **#فرهنگی**\n\n"
            text = text.replace("#فرهنگی", "", 1).lstrip()
        elif text.startswith("#اقتصادی"):
            prefix = "💰 **#اقتصادی**\n\n"
            text = text.replace("#اقتصادی", "", 1).lstrip()
        elif text.startswith("#علمی"):
            prefix = "🔬 **#علمی**\n\n"
            text = text.replace("#علمی", "", 1).lstrip()
        elif text.startswith("#اخبار_جنگ"):
            prefix = "🚀 **#اخبار_جنگ**\n\n"
            text = text.replace("#اخبار_جنگ", "", 1).lstrip()
        elif text.startswith("#جنگ_غزه"):
            prefix = "🚀 **#جنگ_غزه**\n\n"
            text = text.replace("#جنگ_غزه", "", 1).lstrip()
        elif text.startswith("#جنگ_ایران_و_اسراییل"):
            prefix = "🚀 **#جنگ_ایران_و_اسراییل**\n\n"
            text = text.replace("#جنگ_ایران_و_اسراییل", "", 1).lstrip()
        elif text.startswith("#تکمیلی"):
            prefix = "📝 **#تکمیلی**\n\n"
            text = text.replace("#تکمیلی", "", 1).lstrip()
        elif text.startswith("#مهم"):
            prefix = "❗️ **#مهم**\n\n"
            text = text.replace("#مهم", "", 1).lstrip()
        final_text = prefix + text + footer

        if msg.text:
            await context.bot.send_message(chat_id=msg.chat_id, text=final_text, reply_to_message_id=reply)
        elif msg.photo:
            await context.bot.send_photo(chat_id=msg.chat_id, photo=msg.photo[-1].file_id, caption=final_text, reply_to_message_id=reply)
        elif msg.video:
            await context.bot.send_video(chat_id=msg.chat_id, video=msg.video.file_id, caption=final_text, reply_to_message_id=reply)

        await msg.delete()

if __name__ == "__main__":
    keep_alive()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle))
    print("🤖 ربات در حال اجراست...")
    app.run_polling()

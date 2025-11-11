# Bot Telegram Ucapan Selamat Datang
# Dibuat untuk: AWIMEDAN CHANNEL | CPM One
# By: @AWIMEDAN

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from datetime import datetime
import pytz

# ==== GANTI TOKEN DI BAWAH INI ====
BOT_TOKEN = "8245390698:AAE_P8yGHYU9N2nMcmtXjYvtPFjpJRZvRSc"

# Zona waktu Indonesia (WIB)
tz = pytz.timezone('Asia/Jakarta')

# Fungsi untuk menampilkan ucapan selamat datang
async def welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.new_chat_members:
        for member in update.message.new_chat_members:
            waktu = datetime.now(tz).strftime("%H:%M:%S")
            tanggal = datetime.now(tz).strftime("%d/%m/%Y")
            hari = datetime.now(tz).strftime("%A")
            nama = member.first_name
            user_id = member.id
            username = f"@{member.username}" if member.username else "-"

            text = f"""
╔═━━━━───•✧•───━━━━═╗
                  𝗪𝗘𝗟𝗖𝗢𝗠𝗘
╚═━━━━───•✧•───━━━━═╝
WELCOME BROTHER TO GROUP  
★ 𝘼𝙒𝙄𝙈𝙀𝘿𝘼𝙉 𝙂𝙍𝙊𝙐𝙋★

🕒 *Your Time:* `{waktu}`
👤 *NAME:* {nama}
🆔 *INFO ID:* `{user_id}`
💬 *USERNAME:* {username}
📅 *TANGGAL:* {tanggal}
📆 *HARI:* {hari}

⚠️⚠️ *WARNING* ⚠️⚠️
🚫 NO SPAM
🚫 NO PORN
🚫 NO RUSUH
🚫 NO LINK

💎 *BUY SCRIPT VIP*
⭐ *@AWIMEDAN* ⭐
"""
            await update.message.reply_text(text, parse_mode="Markdown")

# Jalankan bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_message))

print("🤖 Bot sedang berjalan...")

app.run_polling()
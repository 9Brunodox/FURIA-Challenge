from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

from outras import get_elenco, get_titulos
from kingsleague.players import get_elenco_furia_kl
from kingsleague.staffs import get_staff_furia_kl
from kingsleague.stats import get_info_furia_kl
from kingsleague.matches import get_jogos_furia_kl

TOKEN = ""

MODALIDADES = {
    "cs": "Counter-Strike",
    "val": "Valorant",
    "rl": "Rocket League",
    "r6": "Rainbow Six",
    "kl": "Kings League"
}

HISTORIA = """
<b>🏆 História da FURIA</b>

Fundada em 2017 por André Akkari, Jaime 'raizen' Pádua e Cris Guedes, a FURIA começou no Counter-Strike e se expandiu para Valorant, League of Legends, Rainbow Six, Rocket League e Kings League.

Com postura agressiva, identidade forte e sede internacional, a FURIA é uma potência do cenário competitivo global.
"""

# Botão para voltar para as modalidades
def voltar_modalidades():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Voltar às Modalidades", callback_data="modalidades")]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📖 História", callback_data="historia")],
        [InlineKeyboardButton("🎮 Modalidades", callback_data="modalidades")]
    ]
    await update.message.reply_text(
        "🔥 <b>Bem-vindo ao Chat da FURIA</b>\n\nEscolha uma opção:",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Botões
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "historia":
        await query.edit_message_text(HISTORIA, parse_mode="HTML", reply_markup=voltar_modalidades())

    elif data == "modalidades":
        buttons = [[InlineKeyboardButton(nome, callback_data=f"mod_{sigla}")] for sigla, nome in MODALIDADES.items()]
        await query.edit_message_text(
            "🎮 <b>Modalidades da FURIA</b>\n\nEscolha uma:", parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("mod_"):
        mod = data.split("_")[1]
        context.user_data["mod"] = mod

        buttons = [[InlineKeyboardButton("👥 Elenco", callback_data="elenco")]]
        if mod == "kl":
            buttons += [
                [InlineKeyboardButton("📊 Informações Gerais", callback_data="info_kl")],
                [InlineKeyboardButton("📅 Jogos", callback_data="jogos_kl")],
                [InlineKeyboardButton("🧠 Comissão Técnica", callback_data="staff_kl")]
            ]
        else:
            buttons += [
                [InlineKeyboardButton("🏆 Títulos", callback_data="titulos")],
                [InlineKeyboardButton("📅 Jogos", callback_data="jogos")]
            ]
        buttons.append([InlineKeyboardButton("🔙 Voltar", callback_data="modalidades")])

        await query.edit_message_text(
            f"📂 <b>{MODALIDADES[mod]}</b>\n\nEscolha uma das opções:",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data == "elenco":
        mod = context.user_data.get("mod")
        texto = get_elenco_furia_kl() if mod == "kl" else get_elenco(mod)
        await query.edit_message_text(texto, parse_mode="HTML", reply_markup=voltar_modalidades())

    elif data == "titulos":
        mod = context.user_data.get("mod")
        texto = get_titulos(mod)
        await query.edit_message_text(texto, parse_mode="HTML", reply_markup=voltar_modalidades())

    elif data == "jogos":
        texto = "📅 <b>Jogos da FURIA</b>\n\nSerá adicionado em breve!"
        await query.edit_message_text(texto, parse_mode="HTML", reply_markup=voltar_modalidades())

    elif data == "info_kl":
        texto = get_info_furia_kl()
        await query.edit_message_text(texto, parse_mode="HTML", reply_markup=voltar_modalidades())

    elif data == "jogos_kl":
        texto = get_jogos_furia_kl()
        await query.edit_message_text(texto, parse_mode="HTML", reply_markup=voltar_modalidades())

    elif data == "staff_kl":
        texto = get_staff_furia_kl()
        await query.edit_message_text(texto, parse_mode="HTML", reply_markup=voltar_modalidades())

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()

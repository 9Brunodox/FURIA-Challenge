from liquipediapy import liquipediapy

SIGLA_TO_GAME = {
    "cs": "counterstrike",
    "val": "valorant",
    "r6": "rainbowsix"
}

def get_jogos_liquipedia(sigla: str) -> str:
    try:
        if sigla not in SIGLA_TO_GAME:
            return "❌ Modalidade não suportada."

        game = SIGLA_TO_GAME[sigla]
        lp = liquipediapy("FuriaBot", game)

        resultados = lp.get_team_results("FURIA")
        if not resultados:
            return f"📭 Nenhum jogo da FURIA encontrado em {game}."

        texto = f"<b>📅 Últimos Jogos da FURIA — {game.capitalize()}</b>\n\n"
        for r in resultados[:5]:
            vs = r.get("opponent", "Adversário")
            score = r.get("score", "?")
            evento = r.get("event", "Evento")
            texto += f"• vs {vs} ({score}) — {evento}\n"

        return texto
    except Exception as e:
        return f"❌ Erro ao buscar jogos da Liquipedia: {e}"

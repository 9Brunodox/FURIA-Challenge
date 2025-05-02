import json
from pathlib import Path
from datetime import datetime

MATCHES_FILE = Path("API/KL/matches.json")

def formatar_data(data_str):
    try:
        dt = datetime.fromisoformat(data_str.replace("Z", "+00:00"))
        return dt.strftime("%d/%m/%Y %H:%M")
    except:
        return "Data desconhecida"

def get_jogos_furia_kl():
    try:
        with open(MATCHES_FILE, encoding="utf-8") as f:
            data = json.load(f)

        matches = data.get("matches", [])
        anteriores = []
        futuros = []

        for jogo in matches:
            status = jogo.get("status")
            data_fmt = formatar_data(jogo.get("date", ""))

            p = jogo.get("participants", {})
            home = p.get("homeTeam", {}).get("shortName", "???")
            away = p.get("awayTeam", {}).get("shortName", "???")

            placar_home = jogo.get("scores", {}).get("homeScore")
            placar_away = jogo.get("scores", {}).get("awayScore")

            if status == "ended" and placar_home is not None and placar_away is not None:
                linha = f"{home} <b>[{placar_home}]</b> x <b>[{placar_away}]</b> {away} — {data_fmt}"
                anteriores.append(f"• {linha}")
            else:
                linha = f"{home} x {away} — {data_fmt}"
                futuros.append(f"• {linha}")

        texto = "<b>📅 Jogos da FURIA - Kings League</b>\n\n"
        texto += "🔙 <b>Jogos Anteriores:</b>\n" + ("\n".join(anteriores) if anteriores else "• Nenhum jogo anterior") + "\n\n"
        texto += "📆 <b>Próximos Jogos:</b>\n" + ("\n".join(futuros) if futuros else "• Nenhum jogo agendado")

        return texto
    except Exception as e:
        return f"❌ Erro ao carregar jogos: {e}"

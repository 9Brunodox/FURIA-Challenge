import json
from pathlib import Path
from collections import defaultdict

PLAYERS_FILE = Path("API/KL/players.json")

POS_TRADUZIDA = {
    "forward": "⚽ Atacantes",
    "midfielder": "🎯 Meio-campistas",
    "goalkeeper": "🧤 Goleiros",
    "defender": "🛡️ Zagueiros"
}

def get_elenco_furia_kl():
    try:
        with open(PLAYERS_FILE, encoding="utf-8") as f:
            jogadores = json.load(f)

        if not jogadores:
            return "❌ Nenhum jogador encontrado."

        posicoes = defaultdict(list)
        for jogador in jogadores:
            nome = jogador.get("shortName", "Desconhecido")
            posicao = jogador.get("role", "").lower()
            posicoes[posicao].append(nome)

        texto = "👥 <b>Elenco da FURIA - Kings League</b>\n\n"
        for ordem in ["forward", "midfielder", "goalkeeper", "defender"]:
            if posicoes.get(ordem):
                titulo = POS_TRADUZIDA[ordem]
                texto += f"{titulo}:\n\n"
                texto += "\n".join(f"– {nome}" for nome in posicoes[ordem]) + "\n\n"

        return texto.strip()
    except Exception as e:
        return f"❌ Erro ao formatar elenco: {e}"

import json
from pathlib import Path

ELENCO_ICON = "👤"
TITULO_ICON = "🏆"

BASE_PATH = Path("API")

def get_elenco(sigla: str) -> str:
    try:
        arquivo = BASE_PATH / modalidade_folder(sigla) / f"{sigla}.json"
        with open(arquivo, encoding="utf-8") as f:
            data = json.load(f)

        elenco = data.get("elenco", [])
        if not elenco:
            return "👥 <b>Elenco:</b>\nSem jogadores informados."

        texto = "👥 <b>Elenco:</b>\n\n"
        for nome in elenco:
            texto += f"{ELENCO_ICON} {nome}\n"

        return texto
    except Exception as e:
        return f"❌ Erro ao obter elenco: {e}"

def get_titulos(sigla: str) -> str:
    try:
        arquivo = BASE_PATH / modalidade_folder(sigla) / f"{sigla}.json"
        with open(arquivo, encoding="utf-8") as f:
            data = json.load(f)

        titulos = data.get("titulos", [])
        if not titulos:
            return "🏆 <b>Títulos:</b>\nNenhum título registrado."

        texto = "🏆 <b>Títulos:</b>\n\n"
        for t in titulos:
            texto += f"{TITULO_ICON} {t}\n"

        return texto
    except Exception as e:
        return f"❌ Erro ao obter títulos: {e}"

# Mapeia siglas para pastas (ajusta se quiser alterar no futuro)
def modalidade_folder(sigla: str) -> str:
    mapping = {
        "cs": "CS",
        "val": "Valorant",
        "rl": "RocketLeague",
        "r6": "R6"
    }
    return mapping.get(sigla, sigla)

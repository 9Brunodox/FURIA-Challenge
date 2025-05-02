import json
from pathlib import Path

STAFFS_FILE = Path("API/KL/staffs.json")

ICONS = {
    "coach": "🎮 Técnico",
    "president": "👑 Presidente",
    "owner": "🎙️ Dono",
    "founder": "🧠 Fundador",
    "": "👤"
}

def get_staff_furia_kl():
    try:
        with open(STAFFS_FILE, encoding="utf-8") as f:
            data = json.load(f)

        staffs = data.get("staffs", [])
        if not isinstance(staffs, list):
            return "❌ Formato inválido em staffs.json."

        texto = "🧠 <b>Comissão Técnica da FURIA - Kings League</b>\n\n"
        for membro in staffs:
            nome = membro.get("shortName", "Desconhecido")
            funcao = membro.get("role", "").lower()
            emoji = ICONS.get(funcao, "👤")
            texto += f"{emoji}: {nome}\n"

        return texto
    except Exception as e:
        return f"❌ Erro ao obter comissão técnica: {e}"

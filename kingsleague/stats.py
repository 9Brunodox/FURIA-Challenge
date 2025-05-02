import json
from pathlib import Path

STATS_FILE = Path("API/KL/stats.json")

def get_info_furia_kl():
    try:
        with open(STATS_FILE, encoding="utf-8") as f:
            data = json.load(f)

        rankings = data.get("rankings", [])
        vit = der = gols_pro = gols_contra = None

        for item in rankings:
            code = item["parameter"].get("code")
            total = item.get("total", 0)
            if code == "WIN":
                vit = total
            elif code == "LOSE":
                der = total
            elif code == "GOL":
                gols_pro = total
            elif code == "GOL-S":
                gols_contra = total

        if None in [vit, der, gols_pro, gols_contra]:
            return "❌ Dados incompletos para mostrar informações gerais."

        saldo = gols_pro - gols_contra

        texto = (
            "📊 <b>Informações da FURIA - Kings League</b>\n\n"
            f"✅ Vitórias: {vit}\n"
            f"❌ Derrotas: {der}\n"
            f"⚽ Gols Pró: {gols_pro}\n"
            f"🚫 Gols Sofridos: {gols_contra}\n"
            f"📈 Saldo de Gols: {saldo}"
        )
        return texto
    except Exception as e:
        return f"❌ Erro ao obter informações gerais: {e}"

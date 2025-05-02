# 🤖 ChatBot da FURIA — Telegram Bot

Este é um projeto de chatbot para fãs da FURIA, desenvolvido voltado para o Telegram. O bot permite que os usuários naveguem por diferentes modalidades esportivas em que a FURIA atua, acessem elenco, títulos, comissão técnica, e muito mais — tudo com uma interface simples e interativa.

---

## 📌 Funcionalidades

- `/start`: Inicia a conversa e apresenta o menu de navegação
- 📖 História: Exibe a história oficial da FURIA
- 🎮 Modalidades: Lista todas as modalidades suportadas
  - Counter-Strike
  - Valorant
  - Rainbow Six
  - Rocket League
  - Kings League

Para cada modalidade, o usuário pode acessar:

- 👥 Elenco (com emojis e divisão por função no caso da Kings League)
- 🏆 Títulos conquistados
- 📅 Jogos (atualmente apenas Kings League — os demais exibirão “em breve”)
- 🧠 Comissão Técnica (somente Kings League)
- 📊 Informações gerais (somente Kings League)

---

## 🧠 Tecnologias utilizadas

- Python 3.11+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v20+
- Dados estruturados em `.json` (API/KL, API/CS, etc)
- Leitura local de informações da Kings League
- Interface em HTML (Telegram) para exibição visual limpa

---

## 🗂️ Estrutura de diretórios

```
API/
├── CS/cs.json
├── KL/
│   ├── matches.json
│   ├── players.json
│   ├── staffs.json
│   └── stats.json
├── R6/r6.json
├── RocketLeague/rl.json
├── Valorant/val.json

kingsleague/
├── players.py
├── staffs.py
├── stats.py
├── matches.py

outras.py
main.py
```

---

## ▶️ Como executar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o bot:
```bash
python main.py
```

3. Inicie uma conversa com seu bot no Telegram e digite `/start`.

---

## 📄 Exemplo de navegação

```
Usuário: /start
Bot:
🔥 Bem-vindo ao Chat da FURIA!

Escolha uma opção:
📖 História
🎮 Modalidades
```

Ao escolher uma modalidade:
```
📂 Valorant

👥 Elenco
🏆 Títulos
📅 Jogos
🔙 Voltar
```

---

## 🚧 Funcionalidades futuras

- Integração com Liquipedia para jogos de CS/VAL/R6
- Busca em tempo real via APIs públicas
- Suporte a /notificações de jogos ao vivo

---

## 👨‍💻 Autor - Bruno Moreira da Silva

Este projeto foi desenvolvido como desafio técnico com foco em modularidade, clareza e UX dentro do Telegram.  
Todos os dados foram organizados manualmente a partir de fontes públicas.

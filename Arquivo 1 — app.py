from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8542014193:AAH_cR1PFHGuvNiXXyLtFlAIcLbbK-hFUE8"
CHAT_ID = "6306616900"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    mensagem = f"""
📊 ATIVO: {data.get('ticker')}
⏰ HORÁRIO: {data.get('time')}
⏳ TEMPO: {data.get('interval')}
📈 OPERAÇÃO: {data.get('side')}
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": mensagem
    })

    return {"status": "ok"}

app.run(host="0.0.0.0", port=10000)

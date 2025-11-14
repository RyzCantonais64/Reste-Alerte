from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = Flask(__name__)

@app.route("/alerte", methods=["POST"])
def alerte():
    data = request.json
    sender = data.get("sender")
    message = data.get("message")
    location = data.get("location")

    print("\nAlerte reçue !")
    print(f"Émetteur : {sender}")
    print(f"Message  : {message}")
    print(f"Localisation : {location}")

    alert_text = f"Alerte de {sender} \n\n{message}\n Localisation: {location}"
    requests.get(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": alert_text}
    )

    return jsonify({"status": "success", "received": data}), 200

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)


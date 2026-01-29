from flask import Flask, jsonify, request
import smart_bot   # ዋና bot file

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🤖 SMART BOT MINI APP</h1>
    <p>Status: <b>{}</b></p>
    <p>Balance: {}</p>
    <p>Trades today: {}</p>

    <a href='/start'>▶️ Start</a> |
    <a href='/stop'>⛔ Stop</a> |
    <a href='/status'>📊 Refresh</a>
    """.format(
        "ON" if smart_bot.BOT_ACTIVE else "OFF",
        smart_bot.get_balance(),
        smart_bot.TRADES_TODAY
    )

@app.route("/start")
def start_bot():
    smart_bot.BOT_ACTIVE = True
    smart_bot.KILL_SWITCH = False
    return "BOT STARTED ✅"

@app.route("/stop")
def stop_bot():
    smart_bot.BOT_ACTIVE = False
    return "BOT STOPPED ⛔"

@app.route("/status")
def status():
    return jsonify({
        "active": smart_bot.BOT_ACTIVE,
        "balance": smart_bot.get_balance(),
        "trades": smart_bot.TRADES_TODAY
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

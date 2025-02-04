from flask import Flask, request, jsonify

app = Flask(__name__)

faq_responses = {
    "designs": "You can explore our latest collections here: [Insert your link]",
    "pricing": "Our rings start from [Insert price] and vary based on design and gemstone selection.",
    "custom": "We specialize in bespoke jewelry! To begin, tell us about your vision, preferred gemstones, and budget.",
    "whatsapp": "For further assistance, please message us on WhatsApp: [Insert WhatsApp link]"
}

@app.route("/", methods=["GET"])
def home():
    return "Kinchos Chatbot is running!"

@app.route("/chat", methods=["POST"])  # <- This is the important line
def chat():
    user_input = request.json.get("message", "").lower()

    if "designs" in user_input:
        return jsonify({"response": faq_responses["designs"]})
    elif "pricing" in user_input:
        return jsonify({"response": faq_responses["pricing"]})
    elif "custom" in user_input:
        return jsonify({"response": faq_responses["custom"]})
    elif "whatsapp" in user_input or "talk to someone" in user_input:
        return jsonify({"response": faq_responses["whatsapp"]})
    else:
        return jsonify({"response": "I'm sorry, I didn't understand that. Can you rephrase?"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

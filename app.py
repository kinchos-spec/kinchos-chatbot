from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"], "allow_headers": ["Content-Type"]}})

@app.route("/", methods=["GET", "HEAD"])
def home():
    if request.method == "HEAD":
        return "", 200  # Return an empty response for HEAD requests
    return "Kinchos Digital Concierge is running!"

# FAQ responses
faq_responses = {
    "1": "✨ We specialize in bespoke fine jewelry featuring diamonds, sapphires, rubies, spinels, aquamarines, peridots, tourmalines, and other precious gemstones. 💍 Explore rings, earrings, pendants, brooches, and wedding jewelry.",
    "2": "📸 Explore our latest designs: \n🔗 Instagram: https://instagram.com/kinchosjewellery \n💎 WhatsApp Catalog: https://wa.me/c/6593354380",
    "3": "✨ We offer both ready-made jewelry and bespoke creations. 🛍️ Ready-made pieces are available for immediate purchase, while our bespoke service lets you craft something uniquely yours.",
    "4": "💎 Our ready-made rings start from SGD $2,500, depending on gemstone selection and design.",
    "5": "💳 We accept Visa, Mastercard, NETS, bank transfers, and PayNow (for Singapore orders).",
    "6": "✔️ We offer an interest-free layaway plan for select orders, on a case-by-case basis. Contact us via WhatsApp to discuss the details: https://wa.me/6593354380",
    "7": "🔹 Our bespoke process:\n💬 Consultation – Share your vision & preferences.\n🎨 Design Approval – We create a design for review.\n💎 Crafting & Completion – Once approved, we bring your piece to life.\n⏳ Custom pieces typically take 3 to 6 weeks.",
    "8": "📞 Yes! You can book a consultation via WhatsApp: https://wa.me/6593354380",
    "9": "💎 Yes! We can repurpose your existing gemstones into a brand-new setting. Our team will assess the gemstone’s condition before confirming the design possibilities.",
    "10": "📦 Yes! We ship worldwide via DHL Express. Shipping costs depend on your location and order value.",
"10-1": "⏳ Ready-made pieces ship within 2 business days.\n✨ Bespoke jewelry takes between 3 to 8 weeks, depending on complexity.",
"10-2": "🏢 We strongly recommend self-collection for all purchases.\n📍 Orders can be collected by appointment only in Singapore.",
"10-3": "📩 Contact us via:\n📞 WhatsApp: https://wa.me/6593354380\n📧 Email: info@kinchosjewellery.com",
"10-4": "💬 Absolutely! Chat with us on WhatsApp for further assistance:\n📩 https://wa.me/6593354380",
    "0": "⬅️ Returning to the main menu..."
}


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "").strip()

    if user_input in faq_responses:
        return jsonify({"response": faq_responses[user_input]})
    else:
        return jsonify({"response": "I'm sorry, I didn't understand that. Please select a number from the menu."})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

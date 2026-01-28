import json

# ================= LOAD DATA =================

with open("faq_toko.json", "r", encoding="utf-8") as f:
    FAQ_LIST = json.load(f)

with open("badwords.json", "r", encoding="utf-8") as f:
    BADWORDS = json.load(f)

# ================= FILTER KATA KASAR =================

def contains_badword(text):
    text = text.lower()
    for word in BADWORDS:
        if word in text:
            return True
    return False

# ================= LOGIC BOT =================

def get_bot_reply(text):
    text = text.lower()

    # filter kata kasar
    if contains_badword(text):
        return "🙏 Mohon gunakan bahasa yang sopan ya kak "

    # cari di FAQ
    for item in FAQ_LIST:
        for kw in item["keywords"]:
            if kw in text:
                return item["answer"]

    # default reply
    return (
        "Halo kak 😊\n"
        "Saya Asisten Virtual Prohana Shoes\n"
        "Silakan tanyakan seputar sepatu, sandal, jaket kulit, harga, atau pemesanan ya "
    )

from flask import Flask, render_template, request, redirect, url_for, abort
import re

app = Flask(__name__)

# Data contoh destinasi wisata Tuban.
# Pada pengembangan berikutnya, data ini dapat dipindahkan ke database.
destinations = [
    {
        "id": 1,
        "name": "Pantai Boom",
        "category": "Pantai",
        "location": "Kutorejo, Tuban",
        "price": 5000,
        "description": "Pantai di pusat kota Tuban dengan pemandangan laut, dermaga, dan suasana matahari terbenam.",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=85",
        "tag": "Favorit kota"
    },
    {
        "id": 2,
        "name": "Air Terjun Nglirip",
        "category": "Alam",
        "location": "Mulyoagung, Singgahan",
        "price": 10000,
        "description": "Air terjun dengan aliran air jernih dan suasana hijau yang menyegarkan.",
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1200&q=85",
        "tag": "Wisata alam"
    },
    {
        "id": 3,
        "name": "Goa Akbar",
        "category": "Sejarah & Alam",
        "location": "Gedongombo, Semanding",
        "price": 7000,
        "description": "Goa alami yang berada tidak jauh dari kawasan pusat kota Tuban.",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=85",
        "tag": "Jelajah goa"
    },
    {
        "id": 4,
        "name": "Pantai Kelapa",
        "category": "Pantai",
        "location": "Panyuran, Palang",
        "price": 10000,
        "description": "Kawasan pantai dengan deretan pohon kelapa dan suasana santai untuk menikmati pesisir.",
        "image": "https://images.unsplash.com/photo-1497250681960-ef046c08a56e?auto=format&fit=crop&w=1200&q=85",
        "tag": "Teduh & santai"
    },
]

# Username yang sudah dipakai untuk simulasi pengecekan.
registered_users = {
    "aksa": {"name": "Aksa", "role": "Penjelajah Tuban"},
    "admin": {"name": "Administrator", "role": "Pengelola Jelajah Wisata"},
    "tubanexplorer": {"name": "Tuban Explorer", "role": "Kontributor"}
}

@app.template_filter("rupiah")
def rupiah(value):
    """Filter Jinja2 untuk menampilkan angka sebagai mata uang rupiah."""
    return "Rp{:,.0f}".format(value).replace(",", ".")

@app.route("/")
def home():
    return render_template("index.html", featured=destinations[:3])

@app.route("/tentang")
def tentang():
    return render_template("tentang.html")

@app.route("/destinasi")
def destinasi():
    return render_template("destinasi.html", destinations=destinations)

@app.route("/kontak")
def kontak():
    return render_template("kontak.html")

@app.route("/cek")
def cek_form():
    # Mengarahkan pengunjung ke halaman pengecekan dengan contoh username.
    return render_template("cek_username.html", username=None, status=None)

@app.route("/cek/<username>", methods=["GET", "POST"])
def cek_username(username):
    username = username.strip().lower()

    # Validasi: 3-20 karakter, huruf/angka/underscore, diawali huruf.
    valid = re.fullmatch(r"[a-z][a-z0-9_]{2,19}", username) is not None

    if not valid:
        status = "invalid"
        message = "Username tidak valid. Gunakan 3–20 karakter, diawali huruf, dan hanya berisi huruf, angka, atau underscore."
    elif username in registered_users:
        status = "taken"
        message = "Username ini sudah dipakai. Silakan coba nama pengguna lain."
    else:
        status = "available"
        message = "Username tersedia dan dapat digunakan!"

    return render_template(
        "cek_username.html",
        username=username,
        status=status,
        message=message
    )

@app.route("/cek-username", methods=["POST"])
def submit_cek_username():
    username = request.form.get("username", "")
    if not username.strip():
        return redirect(url_for("cek_form"))
    return redirect(url_for("cek_username", username=username))

@app.route("/user/<username>")
def user_profile(username):
    username = username.strip().lower()
    user = registered_users.get(username)
    if user is None:
        abort(404)
    return render_template("user.html", username=username, user=user)

@app.route("/produk/<int:id>")
def detail_destinasi(id):
    destination = next((item for item in destinations if item["id"] == id), None)
    if destination is None:
        abort(404)
    return render_template("detail.html", destination=destination)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)

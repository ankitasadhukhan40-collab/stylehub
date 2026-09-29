from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "stylehub_super_secret_key"

USERS_DB = {}

PRODUCTS_DB = [
    {
        "id": 1,
        "name": "Classic Polo Cotton T-Shirt",
        "category": "Men",
        "brand": "Polo",
        "price": 1999,
        "discount": 30,
        "final_price": 1399,
        "sizes": ["S", "M", "L", "XL"],
        "colors": ["Black", "White", "Navy Blue"],
        "image": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500",
    }
]


@app.route("/")
def home():
  return render_template("index.html", products=PRODUCTS_DB)


@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    first_name = request.form.get("first_name")
    email = request.form.get("email")
    password = request.form.get("password")
    if email in USERS_DB:
      return render_template("register.html", error="Email already exists.")
    USERS_DB[email] = {
        "first_name": first_name,
        "password": generate_password_hash(password),
    }
    return redirect(url_for("login"))
  return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form.get("email")
    password = request.form.get("password")
    user = USERS_DB.get(email)
    if user and check_password_hash(user["password"], password):
      session["user"] = email
      session["user_name"] = user["first_name"]
      return redirect(url_for("home"))
    return render_template("login.html", error="Invalid email or password.")
  return render_template("login.html")


@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for("home"))


@app.route("/product/<int:product_id>")
def product(product_id):
  prod = next((p for p in PRODUCTS_DB if p["id"] == product_id), None)
  return render_template("product.html", product=prod)


@app.route("/cart", methods=["GET", "POST"])
def cart():
  if "cart" not in session:
    session["cart"] = []
  if request.method == "POST":
    item_id = int(request.form.get("product_id"))
    prod = next((p for p in PRODUCTS_DB if p["id"] == item_id), None)
    if prod:
      session["cart"].append({
          "name": prod["name"],
          "price": prod["final_price"],
          "size": request.form.get("size", "M"),
          "color": request.form.get("color", "Black"),
          "quantity": int(request.form.get("quantity", 1)),
      })
      session.modified = True
  subtotal = sum(item["price"] * item["quantity"] for item in session["cart"])
  return render_template("cart.html", cart=session["cart"], subtotal=subtotal)


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
  if request.method == "POST":
    session["cart"] = []
    session.modified = True
    return render_template("checkout.html", success=True)
  return render_template("checkout.html", success=False)


if __name__ == "__main__":
  app.run(debug=True, port=5000)
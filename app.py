from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:BgGbddgCeFeGD26556C15-aGDF41bCA2@roundhouse.proxy.rlwy.net:16338/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)

class Productos(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripciom = db.Column(db.String, nullable=False)
    precio = db.Column(db.Integer, nullable=False)

@app.route("/")
def home():
    productos = Productos.query.all()
    return render_template("home.html", productos=productos)

@app.route("/producto/<int:producto_id>", methods=['GET', 'POST'])
def producto(producto_id):
    producto = Productos.query.filter_by(id=producto_id).first()

    if request.method == 'POST':
        return render_template("index.html", producto=producto)
    else:
        return "Producto no encontrado", 404

@app.route("/get_producto_info/<int:producto_id>")
def get_producto_info(producto_id):
    producto = Productos.query.filter_by(id=producto_id).first()

    if producto:
        producto_info = {
            'id': producto.id,
            'nombre': producto.nombre,
            'descripciom': producto.descripciom,
            'precio': producto.precio
        }
        return jsonify(producto_info)
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

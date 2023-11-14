from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Productos(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripciom = db.Column(db.String, nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    
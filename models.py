from datetime import datetime
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    _tablename_ = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    

    def _repr_(self):
        return f'<User {self.username}>'
    
class Contact(db.Model, UserMixin):
    _tablename_ = "contact"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    f_name = db.Column(db.String(255), nullable=False)
    l_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def _repr_(self):
        return f'<Contact {self.name}>'
    

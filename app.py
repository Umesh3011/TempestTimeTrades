from flask import Flask, url_for, render_template, redirect, request, jsonify, session
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from email.message import EmailMessage
import smtplib
from datetime import timedelta
import dotenv
import os

dotenv.load_dotenv()

def newsletter(email_cust):

    email = os.getenv('email')
    password = os.getenv('password')

    SUBJECT = "Newsletter Tempest Time Trades"
    FROM = "s.pratap.4155@gmail.com"
    OWNER = "ut30112001@gmail.com"
    TO = email
    TEXT = f"Dear Sir/Mam, \nWelcome to FurniVerse! We are glad to have you join our family. Thank you for registering with us using the email address {email}.\n\nAt FurniVerse Furniture, we are dedicated to providing you with exceptional Furniture services. Our platform offers two remarkable features: Buy Furniture, create and customize. Whether you need interactive conversational support or Furniture details, we'll help you.\n\nWe understand the importance of safeguarding your personal information. Rest assured, we have implemented robust security measures to ensure that your data remains private and protected. Your trust is our top priority.\n\nWith FurniVerse Furniture, you can enjoy a seamless user experience, exploring the vast Design of Furniture. We believe in simplicity without compromising on quality, making your journey with us both impressive and effortless.\n\nOnce again, thank you for choosing FurniVerse Furniture. We are excited to embark on this Furniture Design with you. Should you have any questions or need assistance, our friendly support team is just a message away.\n\nBest regards,\nFurniVerse Furniture."
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    
    msg = EmailMessage()
    msg['Subject'] = SUBJECT
    msg['From'] = OWNER
    msg['To'] = email_cust
    msg.set_content(TEXT)
    server.send_message(msg)

    msg = EmailMessage()
    msg['Subject'] = SUBJECT
    msg['From'] = email
    msg['To'] = OWNER
    msg.set_content(TEXT)
    server.send_message(msg)
    server.quit()

    return "Success"

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tempest_trade.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "this_is_my_secret_key"
    app.permanent_session_lifetime = timedelta(minutes=10)

    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')
  

    @app.route('/newsletter', methods=['POST', 'GET'])
    def newsletter_post():
        if request.method == 'POST':
            email = request.form.get('email')
            newsletter(email)
        return redirect(url_for('index'))

    @app.route('/explore')
    def explore():
        return render_template('Explore.html')

    @app.route('/collection')
    def collect():
        return render_template('collect.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/contact', methods=['POST', 'GET'])
    def contact_post():
        if request.method == 'POST':
            f_name = request.form.get('f_name')
            l_name = request.form.get('l_name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')

            contact = Contact(f_name=f_name, l_name=l_name, email=email, phone=phone, message=message)

            db.session.add(contact)
            db.session.commit()
            db.session.close()

        return redirect(url_for('index')) 


    login_manager = LoginManager()
    login_manager.login_view = "log_user"
    login_manager.init_app(app)

    from models import User, Contact

    # User loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.before_request
    def make_session_permanent():
        session.permanent = False


    # Create Flask-Admin panel
    admin = Admin(app, name='Control Panel')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Contact, db.session))

    return app
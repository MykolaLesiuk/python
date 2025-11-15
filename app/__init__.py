from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

from .config import DevelopmentConfig, TestingConfig, ProductionConfig
from app.forms import ContactForm

db = SQLAlchemy()
migrate = Migrate()

# Словник конфігурацій
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}

def create_app(config_name="development"):
    """Створення Flask-додатку з вибором конфігурації."""
    app = Flask(__name__)
    
    # Використовуємо клас конфігурації із словника
    app.config.from_object(config[config_name])

    # --- Ініціалізація розширень ---
    db.init_app(app)
    migrate.init_app(app, db)

    # --- Blueprints ---
    from app.posts import posts_bp
    from app.users import users_bp
    from app.auth import auth_bp

    app.register_blueprint(posts_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)
    
    # --- Маршрут головної сторінки (резюме) ---
    @app.route('/')
    def resume():
        return render_template('resume.html', title='Резюме')

    # --- Контакти ---
    @app.route('/contacts', methods=['GET', 'POST'])
    def contacts():
        form = ContactForm()
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            message = form.message.data

            logging.basicConfig(filename='contact_form.log', level=logging.INFO)
            logging.info(f"Name: {name}, Email: {email}, Message: {message}")

            flash(f"Дякуємо, {name}! Ваше повідомлення надіслано.", "success")
            return redirect(url_for('contacts'))
        elif request.method == 'POST':
            flash("Будь ласка, виправте помилки у формі.", "danger")

        return render_template('contacts.html', title='Контакти', form=form)

    # --- Обробка 404 ---
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    return app

from flask import render_template, request, redirect, url_for, flash
import logging
from app.forms import ContactForm

def register_routes(app):

    @app.route('/')
    def resume():
        return render_template('resume.html', title='Резюме')

    @app.route('/contacts', methods=['GET', 'POST'])
    def contacts():
        form = ContactForm()

        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            message = form.message.data

            # Логування у файл
            logging.basicConfig(filename='contact_form.log', level=logging.INFO)
            logging.info(f"Name: {name}, Email: {email}, Message: {message}")

            flash(f"Дякуємо, {name}! Ваше повідомлення надіслано.", "success")
            return redirect(url_for('contacts'))

        elif request.method == 'POST':
            flash("Будь ласка, виправте помилки у формі.", "danger")

        return render_template('contacts.html', title='Контакти', form=form)
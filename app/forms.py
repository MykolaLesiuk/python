from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, TelField
from wtforms.validators import DataRequired, Email, Length, Regexp
from wtforms import BooleanField, PasswordField

class ContactForm(FlaskForm):
    name = StringField('Ім’я', validators=[
        DataRequired(message="Введіть ім’я"),
        Length(min=4, max=10)
    ])
    
    email = StringField('Email', validators=[
        DataRequired(message="Введіть email"),
        Email(message="Некоректний email")
    ])
    
    phone = TelField('Телефон', validators=[
        DataRequired(message="Введіть номер телефону"),
        Regexp(r'^\+?\d{10,15}$', message="Некоректний формат телефону (наприклад: +380501234567)")
    ])
    
    subject = SelectField('Тема', choices=[
        ('general', 'Загальне питання'),
        ('support', 'Підтримка'),
        ('feedback', 'Зворотній зв’язок')
    ], validators=[DataRequired(message="Виберіть тему повідомлення")])
    
    message = TextAreaField('Повідомлення', validators=[
        DataRequired(message="Введіть повідомлення"),
        Length(min=5, max=500)
    ])
    
    submit = SubmitField('Відправити')

class LoginForm(FlaskForm):
    username = StringField('Ім’я користувача', validators=[
        DataRequired(message="Введіть ім’я користувача"),
        Length(min=3, max=25)
    ])
    password = PasswordField('Пароль', validators=[
        DataRequired(message="Введіть пароль"),
        Length(min=4, max=10, message="Пароль повинен бути від 4 до 10 символів")
    ])
    remember = BooleanField('Запам’ятати мене')
    submit = SubmitField('Увійти')
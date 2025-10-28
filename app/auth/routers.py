from flask import render_template, request, redirect, url_for, flash, session, make_response
from app.auth import auth_bp

# Фіктивні дані користувача (заглушка)
VALID_USER = {
    "username": "admin",
    "password": "12345"
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == VALID_USER['username'] and password == VALID_USER['password']:
            session['user'] = username
            flash('Вхід виконано успішно!', 'success')
            return redirect(url_for('auth.profile'))
        else:
            flash('Невірне ім’я користувача або пароль!', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html')


@auth_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user' not in session:
        flash('Будь ласка, увійдіть у систему для доступу до профілю.', 'warning')
        return redirect(url_for('auth.login'))

    username = session['user']
    message = None

    # --- Додавання / видалення кукі ---
    resp = make_response(render_template('auth/profile.html', username=username, cookies=request.cookies))

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            key = request.form.get('key')
            value = request.form.get('value')
            resp.set_cookie(key, value)
            flash(f'Кука "{key}" додана!', 'success')

        elif action == 'delete_one':
            key = request.form.get('key')
            resp.delete_cookie(key)
            flash(f'Кука "{key}" видалена!', 'info')

        elif action == 'delete_all':
            for key in request.cookies.keys():
                resp.delete_cookie(key)
            flash('Усі кукі видалено!', 'info')

    return resp


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Ви вийшли із системи.', 'info')
    return redirect(url_for('auth.login'))

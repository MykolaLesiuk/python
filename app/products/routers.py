from flask import render_template
from app.products import products_bp

@products_bp.route('/')
def product_list():
    products = [
        {'name': 'Навушники', 'price': 1800},
        {'name': 'Мишка', 'price': 1500},
        {'name': 'Пачка дзигарів', 'price': 100},
    ]
    return render_template('products/list.html', title='Товари', products=products)

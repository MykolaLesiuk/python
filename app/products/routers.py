from flask import render_template
from app.products import products_bp

@products_bp.route('/')
def product_list():
    products = [
        {'name': 'Ноутбук', 'price': 35000},
        {'name': 'Мишка', 'price': 700},
        {'name': 'Клавіатура', 'price': 1200},
    ]
    return render_template('products/list.html', title='Товари', products=products)

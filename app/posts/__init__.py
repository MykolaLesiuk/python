from flask import Blueprint

# створюємо blueprint (назва має збігатися зі змінною, яку реєструєш в app)
posts_bp = Blueprint(
    "posts", __name__,
    template_folder="templates",
    static_folder="static"
)

# ⚠️ Імпортуємо routers тільки після створення blueprint
from . import routers
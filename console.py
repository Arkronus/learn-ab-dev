from app import db
from models import *

title = "Подсчет размера выборки"
text = ""
preview_text = """
Разберем базовый статистический аппарат, который понадобится для определения длительности эксперимента"""
is_practice = False
sorting_column = 110
custom_html_file = "sample-size-calculation.html"


post = Post(title = title,
            preview_text = preview_text,
            is_practice = is_practice,
            sorting_column = sorting_column,
            custom_html_file = custom_html_file)

db.session.add(post)
db.session.commit()

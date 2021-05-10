from app import db
from models import *

title = "Подсчет выборки с Python"
text = """        <figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="0202a429-27de-4089-9e0d-8ac7svfhsvd0a">
                <div style="font-size:1.5em"><span class="icon">📌</span></div>
                <div style="width:100%">Для выполнения данного блока познакомьтесь с <a href="https://colab.research.google.com/drive/1b_Rqp-KHJikVsIZZJABxaKKdPj989_FG?usp=sharing">калькулятором размера выборки</a> и выполните задания оттуда</div>
            </figure>"""
preview_text = """
Используем среду Google Colab и базовые статистические пакеты в Python, чтобы рассчитать размер выборки для эксперимента"""
is_practice = True
sorting_column = 120
custom_html_file = None


post = Post(title = title,
            preview_text = preview_text,
            is_practice = is_practice,
            text = text,
            sorting_column = sorting_column,
            custom_html_file = custom_html_file)

db.session.add(post)
db.session.commit()

# =====


q_text = """
<div class="page-body">
   <p class="">Вычислите объем выборки для следующих вводных:</p>
   <div class="indented">
      <p class=""></p>
      <p class="">Метрика теста - это конверсия добавление товара в корзину → покупка.</p>
      <ul class="bulleted-list">
         <li>Ее текущее значение - 25.4%.</li>
      </ul>
      <ul class="bulleted-list">
         <li>Мы ожидаем, что улучшение в тесте позволит выраcтить ее до 30%.</li>
      </ul>
      <ul class="bulleted-list">
         <li>Статистические параметры берем α = 5%, β = 20%</li>
      </ul>
   </div>
   <p></p>
   <p id="d42c62a7-e180-4749-a46b-67a958e19dfc" class=""></p>
</div>
"""

q_answer = "1884"
q_sorting_column = 10

q = Question(text = q_text,
             answer= q_answer,
             sorting_column = q_sorting_column)

db.session.add(q)
db.session.commit()

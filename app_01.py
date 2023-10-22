# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал) 
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def welcome():
     return render_template('base.html')

@app.get('/clothes/')
def clothes():
    assort = [
        {'Type_s': 'Свитер', 'Country': 'Россия', 'Price': 1500, 'Sale': 1350},
        {'Type_s': 'Футболка', 'Country': 'Россия', 'Price': 1000, 'Sale': 900},
        {'Type_s': 'Шорты', 'Country': 'США', 'Price': 1100, 'Sale': 950},
        {'Type_s': 'Носки', 'Country': 'Канада', 'Price': 300, 'Sale': 299}
    ]
    return render_template('clothes.html', assort=assort)

@app.route('/shoes/')
def shoes():
    assort = [
        {'Type_s': 'Ботинки', 'Country': 'Россия', 'Price': 3500, 'Sale': 2350},
        {'Type_s': 'Кеды', 'Country': 'США', 'Price': 2000, 'Sale': 1600},
        {'Type_s': 'Сапоги', 'Country': 'США', 'Price': 1100, 'Sale': 950},
        {'Type_s': 'Валенки', 'Country': 'Россия', 'Price': 10000, 'Sale': 1500}
    ]
    return render_template('shoes.html', assort=assort)

@app.route('/hat/')
def hat():
    assort = [
        {'Type_s': 'Панама', 'Country': 'Бразилия', 'Price': 1500, 'Sale': 1350},
        {'Type_s': 'Кепка', 'Country': 'США', 'Price': 1000, 'Sale': 900},
        {'Type_s': 'Целиндр', 'Country': 'Англия', 'Price': 1100, 'Sale': 950},
        {'Type_s': 'Ушанка', 'Country': 'Россия', 'Price': 300, 'Sale': 299}
    ]
    return render_template('hat.html', assort=assort)

if __name__ == '__main__':
    app.run(debug=True)
# Домашнее задание по теме "План написания админ панели"

# импорт библиотеки SQLite
import sqlite3


# объявление функции initiate_db
def initiate_db():
    # создание и соединение с БД " "
    connection = sqlite3.connect("products.db")
    # создание курсора БД (виртуальная мышь)
    cursor = connection.cursor()

    # создание БД Products через SQL-запросы с полями id, title, description, price
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products
    (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    """)
    # заполнение БД данными
    # for i in range(1, 5):
    #     cursor.execute(
    #         'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #         (f'Продукт {i}', f'Фигура {i}', f'{i * 100}')
    #     )
    # сохраняем изменения БД
    connection.commit()
    # закрываем соединение с БД
    connection.close()


# функция get_all_products возвращающая все записи из таблицы Products
def get_all_products():
    # создание и соединение с БД "products.db"
    connection = sqlite3.connect("products.db")
    # создание курсора БД (виртуальная мышь)
    cursor = connection.cursor()
    # SQL запрос по извлечению всех записей таблицы Products БД products
    cursor.execute('SELECT * FROM Products')
    # присвоение переменной products значений из таблицы (БД)
    # products = cursor.fetchall()
    # закрываем соединение с БД
    # connection.close()
    # возврат функции
    return cursor.fetchall()


# обращение к функции создания БД
initiate_db()

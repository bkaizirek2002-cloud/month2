import sqlite3


def connect():

    return sqlite3.connect("library.db")


# 1️⃣ Создание таблицы
def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS books
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       name
                       TEXT,
                       author
                       TEXT,
                       publication_year
                       INTEGER,
                       genre
                       TEXT,
                       number_of_pages
                       INTEGER,
                       number_of_copies
                       INTEGER
                   )
                   """)

    conn.commit()
    conn.close()


# 2️⃣ Добавление книг
def insert_books():
    conn = connect()
    cursor = conn.cursor()

    books = [
        ('Война и мир', 'Лев Толстой', 1869, 'Роман-эпопея', 1225, 5),
        ('Преступление и наказание', 'Фёдор Достоевский', 1866, 'Психологический роман', 672, 8),
        ('Гарри Поттер и философский камень', 'Джоан Роулинг', 1997, 'Фэнтези', 432, 15),
        ('1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 328, 10),
        ('Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд', 1925, 'Роман', 218, 7),
        ('Убить пересмешника', 'Харпер Ли', 1960, 'Роман', 376, 6),
        ('Маленький принц', 'Антуан де Сент-Экзюпери', 1943, 'Сказка', 96, 12),
        ('Властелин колец', 'Джон Толкин', 1954, 'Фэнтези', 1178, 9),
        ('Над пропастью во ржи', 'Джером Сэлинджер', 1951, 'Роман', 277, 4),
        ('451 градус по Фаренгейту', 'Рэй Брэдбери', 1953, 'Антиутопия', 256, 11)
    ]

    cursor.executemany("""
                       INSERT INTO books
                       (name, author, publication_year, genre, number_of_pages, number_of_copies)
                       VALUES (?, ?, ?, ?, ?, ?)
                       """, books)

    conn.commit()
    conn.close()


# 3️⃣ Получение всех книг
def get_all_books():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books


# 4️⃣ Обновление названия книги по id
def update_book_name(book_id, new_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
                   UPDATE books
                   SET name = ?
                   WHERE id = ?
                   """, (new_name, book_id))
    conn.commit()
    conn.close()


# 5️⃣ Удаление книги по id
def delete_book(book_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
                   DELETE
                   FROM books
                   WHERE id = ?
                   """, (book_id,))
    conn.commit()
    conn.close()


# 🔽 Точка входа
if __name__ == "__main__":
    create_table()
    insert_books()

    print("📚 Все книги:")
    for book in get_all_books():
        print(book)

    update_book_name(1, "1869 (обновлённое издание)")


    delete_book(2)

    print("\n📚 После обновления (id 1) и удаления (id 2):")
    for book in get_all_books():
        print(book)
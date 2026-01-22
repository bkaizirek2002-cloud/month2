import sqlite3

def create_table():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    create_table_query = '''
                         CREATE TABLE IF NOT EXISTS books \
                         ( \
                             name \
                             TEXT, \
                             author \
                             TEXT, \
                             publication_year \
                             INTEGER, \
                             genre \
                             TEXT, \
                             number_of_pages \
                             INTEGER, \
                             number_of_copies \
                             INTEGER
                         ) \
                         '''

    cursor.execute(create_table_query)

    conn.commit()
    conn.close()
    print("Таблица books создана успешно.")

def insert_books():
    conn = sqlite3.connect('library.db')
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

    insert_query = '''
                   INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
                   VALUES (?, ?, ?, ?, ?, ?) \
                   '''

    cursor.executemany(insert_query, books)

    conn.commit()
    conn.close()
    print("Книги добавлены успешно.")


if __name__ == "__main__":
    create_table()
    insert_books()
books = [
    {"id": 1, "title": "Война и мир", "author": "Л. Н. Толстой"},
    {"id": 2, "title": "Преступление и наказание", "author": "Ф. М. Достоевский"},
    {"id": 3, "title": "Мастер и Маргарита", "author": "М. А. Булгаков"}
]

def get_all_books():
    if books:
        print("Список всех книг:")
        for book in books:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}")
    else:
        print("Книг нет в базе.")

def update_book_title(book_id, new_title):
    for book in books:
        if book["id"] == book_id:
            book["title"] = new_title
            print(f"Название книги с ID {book_id} обновлено на '{new_title}'.")
            return
    print(f"Книга с ID {book_id} не найдена.")

def delete_book(book_id):
    global books
    for i, book in enumerate(books):
        if book["id"] == book_id:
            del books[i]
            print(f"Книга с ID {book_id} удалена.")
            return
    print(f"Книга с ID {book_id} не найдена.")

if __name__ == "__main__":
    get_all_books()
    print("\n")

    update_book_title(1, "Война и мир. Том 1-4")
    print("\n")

    get_all_books()
    print("\n")

    delete_book(2)
    print("\n")

    get_all_books()
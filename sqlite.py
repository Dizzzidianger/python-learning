import sqlite3 #импорт библиотеки sql 
#ЭТА СТРОКА СОЗДАЕТ БАЗУ ДАННЫХ (если её нет)
conn = sqlite3.connect("my_libary.db") #база данных ( здесь всё сразу - если не было, создаст, если есть -найдёт)
cursor = conn.cursor()

#Теперь создаем ТАБЛИЦУ внутри этой базы
cursor.execute('''
Create table if not exists books(
    id integer primary key autoincrement,
    title text not null,
    author text,
    pages integer   
)
''')

#Добавляем данные в таблицу
cursor.execute("Insert INTO books (title, author, pages) VALUEs ('Властелин Колец', 'Толкин', 1000)")

# Сохраняем изменения
conn.commit()

#Закрываем соединение
conn.close()
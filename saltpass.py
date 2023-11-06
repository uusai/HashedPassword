import sqlite3 # Импортируем библиотеку для работы с БД
import bcrypt # Импортируем библиотеку для хеширования паролей

db = sqlite3.connect("ulop") # Подключаем БД

cursor = db.cursor() # Создаем курсор для управления БД
cursor.execute("SELECT * FROM users") # Выбираем таблицу в БД

def saltpassword(password): # Создаем функцию для хеширования пароля
    salt = bcrypt.gensalt()
    password = password.encode('utf-8')
    hashedpassword = bcrypt.hashpw(password,salt)
    return hashedpassword

def createaccount(username, password): # Функция для создания аккаунта
    for a in cursor.fetchall():
        if(username == a[0]):
            return print("An account with this login already exists")
    cursor.execute("INSERT INTO users VALUES (?,?)", (username,saltpassword(password)))
    db.commit()
    return print("The account was successfully created")

def authentication(login,password): # Функция для аутентификации
    cursor.execute("SELECT * FROM users")
    for a in cursor.fetchall():
        if(login == a[0]):
            if bcrypt.checkpw(password.encode('utf-8'),a[1]):
                return print("Successfully")
            return print("Incorrect password")
    return print("Incorrect login")

createaccount(input('Write your login: '), input('Write your password: '))
authentication(input('Login: '),input('Password: '))
from pathlib import Path # Імпорт модулів

path = Path('cats.txt') # Файл

def get_cats_info(path): # Функція з параметрами як шлах до файлу
    list_cats = [] # Створюємо пустий список котів 
    if path.is_file(): # Перевірка чи це дійсно файл
        with path.open('r') as file: # Відкриваємо файл для читання 
            lines = file.readlines() # Читаємо рядками
            for line in lines: # Цикл для всіх рядків
                id, name, age = line.strip().split(',') # Розділюємо всі данні
                cat_dict = { 
                'id': id,
                'name' : name,
                'age' : int(age)
                } # Створюємо словник з котами і передаємо всі отримані значення 
                list_cats.append(cat_dict) # Додаємо інформацію про кота
                   
        return list_cats # Повертаємо список котів 
            
    else: # Якщо файл не знайдено повертаємо рядок з помилкою 
        return f'No such file'

# Перевірка функції
assert(get_cats_info(path)) == [{
                                'id': '60b90c1c13067a15887e1ae1',
                                'name' : "Tayson",
                                'age' : 3
                                },
                                {'id': "60b90c2413067a15887e1ae2",
                                'name' : "Vika",
                                'age' : 1},
                                {'id': "60b90c2e13067a15887e1ae3",
                                'name' : "Barsik",
                                'age' : 2
                                },
                                {'id': "60b90c3b13067a15887e1ae4",
                                'name' : "Simon",
                                'age' : 12},
                                {'id' : '60b90c4613067a15887e1ae5',
                                'name' : 'Tessi',
                                'age': 5}]
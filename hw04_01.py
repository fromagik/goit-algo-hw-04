from pathlib import Path # Імпортуємо модуль

def total_salary(path): # Функція яка приймає параметр шлях до файлу з заробітньою платою 
    salary_count = [] # Створюємо пустий список
    if path.is_file(): # Перевірки чи переданий файл є файлом
        with path.open('r') as file: # Відкриваємо файл для читання 
            lines = file.readlines() # Файл читаємо рядками
            for line in lines: # Цикл для читання файлу
                _,salary = line.split(',') # Розділяємо імя та заробітню плату
                salary = int(salary) # Перетворюємо заробітню плату в число
                salary_count.append(salary) # Дадаємо до списку
            
            sum_salary = str(sum(salary_count)) # Знаходимо сумму ЗП для всіх працівників 
            avg_salary = str(sum(salary_count) // len(salary_count)) # Знаходимо середню ЗП
            min_salary = str(min(salary_count)) # Мінімальна ЗП
            max_salary = str(max(salary_count)) # Максимольна ЗП
            
            # Повертаємо рядок з усією інформацією
            return f'Загальна сума заробітної плати: {sum_salary},\nСередня заробітна плата: {avg_salary},\nМінімальна заробітня плата: {min_salary},\nМаксимальна заробітня плата: {max_salary}'
    else: # Якщо файл не знайдемо, виводимо відповідний рядок
        return f'No such file'

path = Path('salary.txt')

# Перевірка вірності функції
assert(total_salary(path)) == '''Загальна сума заробітної плати: 6000,
Середня заробітна плата: 2000,
Мінімальна заробітня плата: 1000,
Максимальна заробітня плата: 3000'''
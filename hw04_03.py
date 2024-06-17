from colorama import Fore #Імпротуємо модулі
import sys
import os

def catalog(path, lvl = 0): # Функція з параметрами патчу на нашу теку, та рівень відступів, який на початку дорівнює 0 
    if os.path.isdir(path): # Перевіряємо чи пареданий патч є текою
        for el in os.listdir(path): # Ітерація по всім файлам в теці
            if os.path.isdir(path + '/' + el): # Перевірка чи файл в теці є папкою
                print(' ' * lvl, Fore.BLUE + el) # Виводимо назву теки синім кольором 
                catalog(path + '/' + el, lvl + 2) # Рекурсивно викликаємо функцію 
            elif el != '.DS_Store': # Якщо файл не є текою (Для зручності я прибрав файл який створюється автоматично для MacOS) 
                print(' ' * lvl , Fore.RED + el) # Виводимо назву файлу червоним кольором для зручності ідентифікації
    else: # Якщо переданий патч не тека, повертаємо False 
        print(False)

if len(sys.argv) > 1: # Перевіряємо чи користувач передав шлях до теки
    path = sys.argv[1]
else: # Якщо ні то використовується поточна тека
    path = os.getcwd()

catalog(path) 
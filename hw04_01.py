from pathlib import Path

def total_salary(path):
    if path.is_file():
        with path.open('r') as file:
            lines = file.readlines()
            count_salary = 0
            for line in lines:
                _,salary = line.split(',')
                salary = int(salary)
                count_salary += salary
    
    return count_salary
path = Path('salary.txt')
total_salary(path)
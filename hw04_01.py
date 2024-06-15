from pathlib import Path

def total_salary(path):
    salary_count = []
    if path.is_file():
        with path.open('r') as file:
            lines = file.readlines()
            for line in lines:
                _,salary = line.split(',')
                salary = int(salary)
                salary_count.append(salary)
            
            sum_salary = sum(salary_count)
            avg_salary = sum(salary_count) // len(salary_count)
            min_salary = min(salary_count)
            max_salary = max(salary_count)

            return f'Загальна сума заробітної плати: {sum_salary},\nСередня заробітна плата: {avg_salary},\nМінімальна заробітня плата: {min_salary},\nМаксимальна заробітня плата: {max_salary}'
    else:
        return f'No such file'

path = Path('salary.txt')

from pathlib import Path

path = Path('cats.txt')

def get_cats_info(path):
    list_cats = []
    if path.is_file():
        with path.open('r') as file:
            lines = file.readlines()
            cat_dict = {
                'id': None,
                'name' : None,
                'age' : None
            }
            for line in lines:
                id, name, age = line.split(',')
                cat_dict['id'], cat_dict['name'], cat_dict['age'] = id, name, age
                list_cats.append(cat_dict)
            return list_cats
            
    else:
        return f'No such file'
    
print(get_cats_info(path))
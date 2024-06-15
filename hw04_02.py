from pathlib import Path

path = Path('cats.txt')

def get_cats_info(path):
    list_cats = []
    id, name, age = "", "", 0
    if path.is_file():
        with path.open('r') as file:
            lines = file.readlines()
            for line in lines:
                id, name, age = line.strip().split(',')
                cat_dict = {
                'id': id,
                'name' : name,
                'age' : int(age)
                }
                list_cats.append(cat_dict)
                   
        return list_cats
            
    else:
        return f'No such file'


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
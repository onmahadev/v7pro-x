import os
from collections.abc import Iterable
 
 
def strings_count(directory: str) -> Iterable[tuple]:
    for root, dirs, files in os.walk(directory):
        for file in files:
            count = 0
            # if os.path.join(root, file).endswith('.py'):
            if os.path.join(root, file).endswith('.html'):
                curr_file = open(os.path.join(root, file), 'r', encoding='utf-8')
                for line in curr_file.readlines():
                    if not (line == '\n' or line.strip().startswith(('"', '#', "'"))):
                        count += 1
                yield os.path.join(root, file), count
 
 
for element in strings_count(directory='..'):
    print('Файл "{}": строк кода - {}'.format(element[0], element[1]))
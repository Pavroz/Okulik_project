import os


# data_file = open('data.txt', 'r')
# data_file.read()
# print('qwewqeqw' + 1)
# data_file.close()


base_path = os.path.dirname(__file__) # Выдает расположение файла, в котором работаем на данный момент
# file_path = f'{base_path}\data.txt'
file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'new_data.txt')
print(file_path)

# Менеджер контекста, который гарантирует, что файл будет закрыт в конце независимо от ошибок и прерываний
def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines(): # readlines вычитывает файл построчно
            yield line

for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        data_line = data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)


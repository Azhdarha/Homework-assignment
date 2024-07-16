#б)Напишите пример приложения на input, которое получает текст от пользователя и 
#создаёт word-файл с этим текстом.

with open('filename.txt', 'w') as file: 
    file.write('\n'.join(iter(input, '')))
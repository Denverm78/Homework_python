# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

def Read_file(path_of_file): # Чтение данных из файла
    try:
        with open (path_of_file, "r") as data:
            source_str = data.readlines()
            return source_str
    except:
        print("Ошибка работы с файлом")


def Write_file(path_of_write, my_str): # Запись данных в файл
    try:
        with open (path_of_write, "w") as data:
            data.write(my_str)
    except:
        print("Ошибка работы с файлом")


def Compress_str(source_str): # Сжатие файла
    new_compress_string = ""
    count = 1
    symbol = source_str[2]
    for i in range(3, len(source_str)-1):
        if source_str[i] == symbol:
            count += 1
        else:
            new_compress_string = new_compress_string + str(count) + symbol
            symbol = source_str[i]
            count = 1
    return new_compress_string


def Decompress_str(comress_string): # Восстановление файла
    new_decompress_str = ''
    symbol_in_str = ''
    for i in range(2,len(comress_string)-2):
        if comress_string[i].isdigit():
            symbol_in_str += comress_string[i]
        else:
            new_decompress_str += (comress_string[i] * int(symbol_in_str))
            symbol_in_str = ''
    return new_decompress_str


path_decompress_file_1 = r"decompress_file_1.txt" # Для проверки сжатия
path_compress_file_1 = r"compress_file.txt_1"

path_decompress_file_2 = r"decompress_file_2.txt" # Для проверки восстановления
path_compress_file_2 = r"compress_file.txt_2"

decompress_str = str(Read_file(path_decompress_file_1)) # 1. Сжатие
print("\nАлгоритм сжатия:")
print(f"Исходная строка: {decompress_str} содержится в файле {path_decompress_file_1}")
my_compress_str = Compress_str(decompress_str)
print(f"Сжатая строка:   ['{my_compress_str}'] содержится в файле {path_compress_file_1}")
Write_file(path_compress_file_1, my_compress_str)
print()

compress_str = str(Read_file(path_compress_file_2)) # 2. Восстановление
print("Алгоритм восстановления:")
print(f"Сжатая строка:           {compress_str} содержится в файле {path_compress_file_2}")
my_decompress_str = Decompress_str(compress_str)
print(f"Восстановленная строка:  ['{my_decompress_str}'] содержится в файле {path_decompress_file_2}")
Write_file(path_decompress_file_2, my_decompress_str)
print()








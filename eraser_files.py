import os
import shutil

path = 'D:/Project_University/Noita_Neuro/Image_Enemy_Lilies/img'  # файлы в этой папке будут удалены после перемещения файлов

# Создаем словарь, где ключом будет имя файла без расширения, а значением список файлов с данным именем
files_dict = {}

# Получаем список файлов в текущей директории
files = os.listdir(path=path)

# Проходим по списку файлов и заполняем словарь
for file in files:
    filename, file_extension = os.path.splitext(file)
    if filename in files_dict:
        files_dict[filename].append(file)
    else:
        files_dict[filename] = [file]

new_dir = 'D:/Project_University/Noita_Neuro/Image_Enemy_Lilies/images_speed'  # Путь к новой директории

# Перемещение файлов с одинаковыми именами, но разными расширениями
for key, value in files_dict.items():
    if len(value) > 1:
        for filesl in value:  # value[1:] переместит ТОЛЬКО файлы xml
            shutil.move(os.path.join(path, filesl), new_dir)

print("Файлы успешно перемещены в новую директорию")

for delete in files:
    hud = os.path.join(path, delete)
    os.unlink(hud)  # unlink or remove

print("Все файлы в целевой папке удалены")

#
#
#
#
# file_png = glob.glob('*.PNG',root_dir=path)
# file_xml = glob.glob('*.XML',root_dir=path)
#
# # Создаем словарь, где ключом будет имя файла без расширения, а значением список файлов с данным именем
# files_dict = {}
#
# # Получаем список файлов в текущей директории
# files = os.listdir(path=path)
#
# # Проходим по списку файлов и заполняем словарь
# for file in files:
#     filename, file_extension = os.path.splitext(file)
#     if filename in files_dict:
#         files_dict[filename].append(file)
#     else:
#         files_dict[filename] = [file]
#
# # Выводим список файлов с одинаковыми именами, но разными расширениями
#
# def files():
#     for key, value in files_dict.items():
#         if len(value) > 1:
#             return value
#
#
#
#
# source_dir = 'D:/Project_University/Noita_Neuro/Image_Enemy_Lilies/img'
# target_dir =
# file_names =    os.listdir(files())
#
# for file_name in file_names:
#     shutil.move(os.path.join(source_dir, file_name), target_dir)
#
#
# # file = os.remove()

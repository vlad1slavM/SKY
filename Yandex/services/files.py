from Yandex.transport.files import get_list_files_dirs, get_file_content


#TODO
# Возможен трабл с тем, что человек попытается скачать файл до того как запустит get_files

class YandexFiles:
    def __init__(self):
        self.files = {}

    def get_files(self, path: str) -> None:
        print("\n")
        print(f"Спустился в директорию {path}")
        print("<---------------------------->" + '\n')
        files_directories = get_list_files_dirs(path)
        items = files_directories['_embedded']['items']
        for item in items:
            type_item = item['type']
            name_item = item['name']
            path_item = item['path']
            if type_item == 'file':
                if name_item not in self.files:
                    self.files[path_item] = name_item
            elif type_item == 'dir':
                self.get_files(path_item)
            print(f"type = {item['type']}, path = {item['path']}, name = {item['name']}")

    def download_file(self, path: str) -> None:
        file_content = get_file_content(path)
        name = self.files[path]

        with open(name, 'wb') as file:
            file.write(file_content)


y = YandexFiles()
print(y.get_files('/'))
y.download_file('disk:/Загрузки/ILSpy.rar')

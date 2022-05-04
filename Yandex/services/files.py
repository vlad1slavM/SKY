from collections import namedtuple
from colorama import Fore
import time

from Yandex.transport.web import get_list_files_dirs, get_file_content
#from Yandex.DB.db import add_info

DEBUG = False

File = namedtuple('File', 'name preview_link media_type md5')


class YandexFiles:
    def __init__(self):
        self.files = {}

    @property
    def get_files(self):
        return self.files

    def get_files_list_from_cloud(self, path: str) -> None:
        if DEBUG:
            print("\n Спустился в директорию {path}\n <---------------------------->\n")
        files_directories = get_list_files_dirs(path)
        items = files_directories['_embedded']['items']
        for item in items:
            type_item = item['type']
            name_item = item['name']
            path_item = item['path']
            if type_item == 'file':
                if path_item not in self.files:
                    preview_item = item['preview']
                    media_type_item = item['media_type']
                    md5_item = item['md5']
                    self.files[path_item] = File(name_item, preview_item, media_type_item, md5_item)
            elif type_item == 'dir':
                if DEBUG:
                    print(f"{path_item = }")
                self.get_files_list_from_cloud(path_item)
            if DEBUG:
                print(f"type = {item['type']},"
                      f" path = {item['path']},"
                      f" name = {item['name']}")

    def download_file(self, path: str) -> None:
        file_content = get_file_content(path)
        name = self.files[path]

        with open(name, 'wb') as file:
            file.write(file_content)

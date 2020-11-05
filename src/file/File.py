import os.path


class File:
    @staticmethod
    def file_exist(path):
        return os.path.exists(path) and os.path.isfile(path)

    def __init__(self, file):
        self.__check_file(file)
        self.file_path = file
        self.elements = []
        self.file = None
        self.__load()

    def __check_file(self, file):
        if not File.file_exist(file):
            assert False, 'File not exist'

    def __open_file(self, mode):
        self.file = open(self.file_path, mode)

    def ___close_file(self):
        self.file.close()

    def __load(self):
        self.__open_file('r')
        elements = self.file.read().split('\n')
        self.elements = elements
        self.___close_file()

    def exist(self, element):
        return element in self.elements

    def save(self):
        self.__open_file('w')
        for element in self.elements:
            self.file.write(element + "\n")
        self.___close_file()
        self.__load()

    def add(self, element: str):
        if not self.exist(element) and element != '':
            self.elements.append(element)

    def clear(self):
        self.elements.clear()

    def get(self):
        return self.elements

    def get_first(self):
        return self.elements[0] if not self.is_empty() else ""

    def pop(self):
        return self.elements.pop(0) if not self.is_empty() else ""

    def is_empty(self):
        return len(self.elements) == 0





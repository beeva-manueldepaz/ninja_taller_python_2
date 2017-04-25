# con una clase nos permite abstraer cosas en varios
class MyContextManager:

    def file_to_upper(self, name:str):
        return name.upper()

    def __init__(self):
        self.file_name = file_name
        self.file_handler = None


    def __enter__(self):
        self.file_handler = open(
            self.file_handler
        )
